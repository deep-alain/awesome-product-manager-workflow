# 本轮核验记录

日期：2026-11-17。

- 60 个仓库均读取 GitHub 元数据与默认分支的 README，目录记录原始来源与日期。
- 59 个仓库未归档；旧 `gsd-build/get-shit-done` 已归档，其 README 明确指向 `open-gsd/gsd-core`，已把新地址加入当前交付阶段。
- Typebot 修正为 `baptisteArno/typebot.io`，scrumlr 修正为 `inovex/scrumlr.io`，ADR 修正为 `architecture-decision-record/architecture-decision-record`，Taiga 选择当前 Docker 部署入口。
- 15 个仓库的 GitHub 许可识别为 NOASSERTION 或未识别；这不是没有许可。已对若干存在社区/商业范围或专门许可的项目补充 README 说明，采用时仍以具体文件和版本为准。
- 校验通过：60 个唯一条目、必需元数据、README 证据、合法分类、README 覆盖与 7 个本地文件引用。
- 四个维护脚本通过 Python 编译检查；目录生成和验证脚本已实际运行；README 读取流程已读取全部条目；元数据刷新函数完成一次真实成功请求，并验证错误时保留旧值与旧核验日期。
- 工作流分类、采用边界及公司评审映射为本次整理判断，区别于上游自己的描述。

这些检查验证了引用目录的完整性，不意味着已经逐个部署、安装 Agent Skills、运行其软件、审计代码或验证商业使用许可。没有采集 Star 增长时序，因此不发布“本周涨幅”或 GitHub Trending 排名。

原始 README 缓存属于本地研究资料，不放进合集正文；合集提供原始链接与简要用途，避免把第三方长文复制成自有内容。
