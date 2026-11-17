import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STAGES=[('ai','01 AI 产品经理与工作流包','把单个 PM 任务转为有证据的工作产物。'),('discovery','02 用户发现与需求证据','访谈、问卷、客服反馈与问题验证。'),('strategy','03 产品策略、立项与对齐','知识沉淀、方案比较和决策汇报。'),('spec','04 PRD、需求规范与流程','让需求、状态和验收条件可追溯。'),('design','05 UI/UX、原型与设计交付','从草图和语义规范到组件与工作界面。'),('review','06 公司评审、RFC 与风险','立项、需求、设计、技术、安全和正式决定。'),('planning','07 优先级、路线图与排期','将已确认范围组织为任务和交付计划。'),('delivery','08 开发协作与接口','按契约实现并检验真实交付。'),('qa','09 测试、可访问性与验收','检查用户成功、失败与恢复路径。'),('experiment','10 实验与验证','用适当设计判断假设与效果。'),('launch','11 发布、运行与回滚','可观察地发布，并能识别故障与采取行动。'),('analytics','12 数据分析与业务复盘','定义正确指标，再从结果形成决定。'),('retro','13 团队回顾与改进','将反馈转为少量可执行行动。'),('similar','14 已有同类资源合集','查找相似索引与学习资料。')]

def cell(text):return str(text or '').replace('|',' / ').replace('\n',' ')
def build():
    data=json.loads((ROOT/'catalog/repos.json').read_text(encoding='utf-8'))
    repos=data['repositories']; by_id={r['repo']:r for r in repos}
    lines=['# 产品经理工作流 GitHub 合集','',f"按产品经理从发现到复盘的工作流，收录 **{len(repos)} 个公开 GitHub 项目**：Agent Skills、可运行软件、组件/SDK、评审方法与资源索引。核验日期：**{data['checked_on']}**。",'', '每项都有用途、采用边界、累计 Star、近期推送和来源记录。已核验仓库元数据与 README；未逐个安装或部署。','', '“热门”以关注度快照和任务相关性呈现；累计 Star 不是近期 Trending，也不代表实际 PM 使用量。归档、迁移、研究预览和许可差异另行标明。','', '## 从这里开始','', '- [完整公司评审流程](docs/company-reviews.md)：八类决策点、参与者、输入、输出及对应仓库。','- [按实际工作组合工具](docs/integration.md)：个人验证、团队迭代、企业交付和效果分析。','- [同类仓库对照](docs/similar-collections.md)：哪些仓库已经很像，差别在哪里。','- [评审记录模板](templates/decision-review.md)：可按任务缩减。','- [机器可读目录](catalog/repos.json)：元数据、许可识别、README 来源与核验日期。','', '## 工作流导航','', '| 阶段 | 产出 / 用途 | 项目数 |','| --- | --- | --- |']
    for sid,title,purpose in STAGES:
        count=sum(r['stage']==sid and not r['archived'] for r in repos)
        lines.append(f'| [{title}](#stage-{sid}) | {purpose} | {count} |')
    lines+=['','各阶段内按累计 Star 排序，类型单独标注；归档项目统一放到末尾。一个仓库可服务多个阶段，主目录只放一次，评审文档做交叉引用。']
    for sid,title,purpose in STAGES:
        lines+=['',f'<a id="stage-{sid}"></a>',f'## {title}','',purpose,'','| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |','| --- | --- | ---: | --- | --- |']
        for r in sorted([r for r in repos if r['stage']==sid and not r['archived']],key=lambda r:r['stars'] or 0,reverse=True):
            note=f"{r['use']}。{r['limits']}。"
            if r.get('review_note'):note+=r['review_note']
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['kind']} | {r['stars']:,} | {r['pushed_at'][:10]} | {cell(note)} |")
    lines+=['','## 归档与迁移记录','','| 历史仓库 | 状态 | 当前处理 |','| --- | --- | --- |']
    for r in repos:
        if r['archived']:lines.append(f"| [{r['repo']}]({r['url']}) | 已归档，历史 Star {r['stars']:,} | {r.get('review_note',r['limits'])} |")
    lines+=['','## 维护与引用','','目录引用上游，不复制整套代码或付费资产。各项目的代码、内容、社区版与商业版分别受其原许可约束；`NOASSERTION` 表示 GitHub 未识别单一许可，不表示可无条件使用。细节见 catalog 中的许可及 README 记录。','','更新方法与收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)。这是一份按任务使用的目录，不要求把所有工具安装进同一项目。']
    (ROOT/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    comparisons=[('phuryn/pm-skills','最接近 AI PM 方法与任务库','发现、策略、执行、分析、上市与增长','能力已很完整；本合集补上软件选型、许可、维护与公司评审的交叉映射。'),('deanpeters/Product-Manager-Skills','可复用 PM Skills','PRD、问题、利益相关方和 PM 工作产物','适合选用单个技能；不等于项目管理或原型软件。'),('menkesu/awesome-pm-skills','名称叫 awesome，实际是可执行工作流集','25 个 PM 工作流和示例交付','按任务诊断与工作产物组织，值得直接参考，不能仅当链接列表。'),('garrytan/gstack','角色化产品到工程评审与交付','方向、工程、设计、QA、安全、发布、复盘','公司评审最相关；代理角色仍不能替代真实责任人和授权。'),('dend/awesome-product-management','传统 PM 综合资源索引','策略、发现、管理、学习与职业资料','适合广泛学习；本合集更强调 GitHub 上可引用的具体包与评审产物。'),('aza-ali/awesome-ai-product-management','AI PM 资源索引','AI 产品实践、资料与工具','相近的检索入口；逐项覆盖与维护情况需要继续核验。'),('bjpcjp/awesome-product-management','较早的 PM 个人资源集','产品管理长期积累与参考','最近推送较早，README 也提示部分链接老旧；作为历史参考。'),('bradtraversy/design-resources-for-developers','设计资源索引','字体、UI、素材和开发者设计工具','覆盖设计资源，当前不接收新增资源；缺少公司全流程评审。')]
    out=['# 相似 GitHub 仓库对照','',f"核验日期：{data['checked_on']}。下表比较实际 README 声明与目录用途，不是下载量或质量排名。",'','| 仓库 | 类型 / 定位 | 主要覆盖 | 与本合集的关系 | Star / 最近推送 |','| --- | --- | --- | --- | --- |']
    for rid,kind,coverage,difference in comparisons:
        r=by_id[rid];out.append(f"| [{rid}]({r['url']}) | {kind} | {coverage} | {difference} | {r['stars']:,} / {r['pushed_at'][:10]} |")
    out+=['','结论：已有相当接近的 PM Skills、AI 评审工作流和传统资源索引。无需重写它们；可在其基础上按具体任务引用，并补齐公开软件、真实评审责任、元数据与选择边界。','','另见 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)：它更接近视觉规范库，能约束视觉词汇，不能覆盖立项、权限、发布和业务复盘的全部决定。']
    (ROOT/'docs/similar-collections.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(json.dumps({'repositories':len(repos),'active':sum(not r['archived'] for r in repos),'stages':len(STAGES)},ensure_ascii=False))
if __name__=='__main__':build()
