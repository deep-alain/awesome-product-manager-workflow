# 产品经理工作流 GitHub 合集

按产品经理从发现到复盘的工作流，收录 **60 个公开 GitHub 项目**：Agent Skills、可运行软件、组件/SDK、评审方法与资源索引。核验日期：**2026-11-17**。

**公开维护、持续更新热门工具。** [每周自动刷新仓库数据](.github/workflows/refresh-catalog.yml)，人工筛选新增项目与工作流分类；欢迎提交 Issue 补充工具或纠正信息。

每项都有用途、采用边界、累计 Star、近期推送和来源记录。已核验仓库元数据与 README；未逐个安装或部署。

“热门”以关注度快照和任务相关性呈现；累计 Star 不是近期 Trending，也不代表实际 PM 使用量。归档、迁移、研究预览和许可差异另行标明。

## 从这里开始

- [完整公司评审流程](docs/company-reviews.md)：八类决策点、参与者、输入、输出及对应仓库。
- [按实际工作组合工具](docs/integration.md)：个人验证、团队迭代、企业交付和效果分析。
- [同类仓库对照](docs/similar-collections.md)：哪些仓库已经很像，差别在哪里。
- [评审记录模板](templates/decision-review.md)：可按任务缩减。
- [机器可读目录](catalog/repos.json)：元数据、许可识别、README 来源与核验日期。

## 工作流导航

| 阶段 | 产出 / 用途 | 项目数 |
| --- | --- | --- |
| [01 AI 产品经理与工作流包](#stage-ai) | 把单个 PM 任务转为有证据的工作产物。 | 5 |
| [02 用户发现与需求证据](#stage-discovery) | 访谈、问卷、客服反馈与问题验证。 | 3 |
| [03 产品策略、立项与对齐](#stage-strategy) | 知识沉淀、方案比较和决策汇报。 | 3 |
| [04 PRD、需求规范与流程](#stage-spec) | 让需求、状态和验收条件可追溯。 | 6 |
| [05 UI/UX、原型与设计交付](#stage-design) | 从草图和语义规范到组件与工作界面。 | 10 |
| [06 公司评审、RFC 与风险](#stage-review) | 立项、需求、设计、技术、安全和正式决定。 | 9 |
| [07 优先级、路线图与排期](#stage-planning) | 将已确认范围组织为任务和交付计划。 | 3 |
| [08 开发协作与接口](#stage-delivery) | 按契约实现并检验真实交付。 | 3 |
| [09 测试、可访问性与验收](#stage-qa) | 检查用户成功、失败与恢复路径。 | 3 |
| [10 实验与验证](#stage-experiment) | 用适当设计判断假设与效果。 | 1 |
| [11 发布、运行与回滚](#stage-launch) | 可观察地发布，并能识别故障与采取行动。 | 4 |
| [12 数据分析与业务复盘](#stage-analytics) | 定义正确指标，再从结果形成决定。 | 4 |
| [13 团队回顾与改进](#stage-retro) | 将反馈转为少量可执行行动。 | 1 |
| [14 已有同类资源合集](#stage-similar) | 查找相似索引与学习资料。 | 4 |

各阶段内按累计 Star 排序，类型单独标注；归档项目统一放到末尾。一个仓库可服务多个阶段，主目录只放一次，评审文档做交叉引用。

<a id="stage-ai"></a>
## 01 AI 产品经理与工作流包

把单个 PM 任务转为有证据的工作产物。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Skills | 141,854 | 2026-11-17 | 产品方向、设计、工程评审与发布工作流。角色视角是辅助评审，不替代公司审批权限。 |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Skills | 28,080 | 2026-11-08 | 产品发现、策略、PRD、增长的 AI 工作流。按任务选用单个技能；框架输出仍需真实证据。 |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | Skills | 8,051 | 2026-11-13 | PM 方法、访谈、需求与优先级技能。先检查输入证据和 Agent 适配。 |
| [phuryn/product-engineering](https://github.com/phuryn/product-engineering) | Skills | 615 | 2026-11-16 | 将需求推进至工程交付与验证。核对与 pm-skills 的迁移关系；不自动接受生成结果。 |
| [menkesu/awesome-pm-skills](https://github.com/menkesu/awesome-pm-skills) | Skills | 460 | 2026-10-06 | 25 个产品管理工作流，从定价、PRD 到研究与决策。按具体工作流选用；来源经验不等于当前项目的用户证据。 |

<a id="stage-discovery"></a>
## 02 用户发现与需求证据

访谈、问卷、客服反馈与问题验证。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | 可运行软件 | 40,015 | 2026-11-17 | 客服对话、客户反馈与支持闭环。客户支持系统不等于研究洞察，仍需归因和分析。README 称 MIT；API 未识别单一 SPDX，需核对各目录。 |
| [formbricks/formbricks](https://github.com/formbricks/formbricks) | 可运行软件 | 13,248 | 2026-11-17 | 站内调研、问卷与用户反馈。需要部署或服务配置；涉及用户数据。README 称核心为 AGPLv3，部署与扩展仍核对原许可。 |
| [baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io) | 可运行软件 | 10,633 | 2026-11-07 | 对话表单与需求收集。对话形式应服务问题；注意许可证和采集信息。README 明确称 Functional Source License；属于 Fair Source，不能按 MIT 理解。 |

<a id="stage-strategy"></a>
## 03 产品策略、立项与对齐

知识沉淀、方案比较和决策汇报。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [slidevjs/slidev](https://github.com/slidevjs/slidev) | 文档工具 | 49,530 | 2026-11-05 | 产品立项、方案和业务评审演示。用真实证据支撑论点，幻灯片不代表批准。 |
| [marp-team/marp](https://github.com/marp-team/marp) | 文档工具 | 12,759 | 2026-11-07 | 用 Markdown 维护评审汇报。适合版本化演示；需约定源文件和交付格式。 |
| [phuryn/pm-brain](https://github.com/phuryn/pm-brain) | 知识工作流 | 973 | 2026-05-20 | 产品经理知识沉淀与复用。将项目事实与可复用方法分开维护。README 明确标为 research preview。 |

<a id="stage-spec"></a>
## 04 PRD、需求规范与流程

让需求、状态和验收条件可追溯。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [github/spec-kit](https://github.com/github/spec-kit) | 开发工作流 | 150,175 | 2026-11-16 | 规范驱动的需求、计划和开发任务。适合需求到工程；对小改动控制文档负担。 |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 图示工具 | 91,132 | 2026-11-17 | 用户流程、系统关系与状态图。图需要明确真实来源和更新责任。 |
| [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 可运行软件 | 79,064 | 2026-11-15 | 项目知识和文档协作。适合知识管理；不能把文档存在当需求已评审。 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 开发工作流 | 75,037 | 2026-11-17 | 以变更规范组织实现和验收。先适配既有流程；避免规范与实现脱节。 |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 可运行软件 | 74,595 | 2026-11-17 | 文档、白板和知识协作。明确协作与自托管功能边界。README 区分社区版等许可范围，不能把仓库所有内容统一视为 MIT。 |
| [outline/outline](https://github.com/outline/outline) | 可运行软件 | 41,280 | 2026-11-16 | 协作知识库与产品文档。需账号、部署及权限配置，核对源可用许可证。README 明确称 BSL 1.1。 |

<a id="stage-design"></a>
## 05 UI/UX、原型与设计交付

从草图和语义规范到组件与工作界面。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 可运行软件 | 135,843 | 2026-11-17 | 流程草图、讨论白板和低保真方案。草图不证明可用性或已实现。 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 组件库 | 128,376 | 2026-11-17 | 实现界面基础组件。复用需要的组件，避免整套示例变功能需求。 |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 视觉规范合集 | 127,881 | 2026-10-28 | 按语义 token 约束视觉生成。营销视觉与实际产品工作流分开选择。 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 组件库 | 100,244 | 2026-11-17 | 企业后台与复杂数据交互。示例工具栏不等于首版范围。 |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | 开发工具 | 91,601 | 2026-11-17 | 组件状态、视觉与设计交付评审。围绕实际组件；不默认启动全套设计系统工程。 |
| [penpot/penpot](https://github.com/penpot/penpot) | 可运行软件 | 62,454 | 2026-11-17 | 界面设计、原型、协作与交付。核对设计稿与真实交互契约。 |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | SDK | 51,450 | 2026-11-17 | 白板与视觉协作应用能力。重点核对商业使用和 SDK 许可证。README 称 SDK 生产使用需要许可证密钥，部分 starter kits 单独为 MIT。 |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | 规范与工具 | 28,911 | 2026-11-06 | 以 token 和理由描述视觉身份。格式校验不证明产品需求或交互可用性。 |
| [carbon-design-system/carbon](https://github.com/carbon-design-system/carbon) | 设计系统 | 9,628 | 2026-11-17 | 企业产品组件、交互与可访问性。检查宿主设计语言与许可证。 |
| [primer/react](https://github.com/primer/react) | 组件库 | 3,937 | 2026-11-17 | 产品工作界面的 React 组件。采用任务适配组件；不能替代行为测试。 |

<a id="stage-review"></a>
## 06 公司评审、RFC 与风险

立项、需求、设计、技术、安全和正式决定。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | 可运行软件 | 40,334 | 2026-11-13 | 数据结构与关系评审。ER 图仍需工程确认与迁移验证。 |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) | 可运行软件 | 19,059 | 2026-11-16 | 需要正式签署时的审批文档。电子签署不替代产品决策；核对适用法律和部署。README 指出 AGPLv3 外还有附加条款。 |
| [architecture-decision-record/architecture-decision-record](https://github.com/architecture-decision-record/architecture-decision-record) | 决策模板 | 17,476 | 2026-11-16 | 记录架构决策、备选与后果。选短模板，保留决策责任与变更理由。 |
| [plantuml/plantuml](https://github.com/plantuml/plantuml) | 图示工具 | 13,422 | 2026-11-17 | 技术评审的时序、组件和部署图。用于沟通真实契约，避免无依据架构。 |
| [rust-lang/rfcs](https://github.com/rust-lang/rfcs) | RFC 实例 | 6,643 | 2026-11-14 | 提案、讨论、采纳与追踪的真实流程。学习机制，避免复制语言治理的全部审批负担。 |
| [OWASP/ASVS](https://github.com/OWASP/ASVS) | 验证标准 | 3,794 | 2026-11-16 | 安全需求与验收项映射。按实际风险和版本选级别，不声称自动合规。 |
| [microsoft/code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook) | 工程手册 | 2,760 | 2026-02-03 | 工程协作、评审、测试与交付实践。按团队规模选择实践，不将整本手册强制成流程。 |
| [microsoft/responsible-ai-toolbox](https://github.com/microsoft/responsible-ai-toolbox) | 可运行工具 | 1,858 | 2026-11-16 | AI 系统责任风险与分析评审。需要合适的数据与模型，不等于法律合规结论。 |
| [alphagov/govuk-design-system](https://github.com/alphagov/govuk-design-system) | 设计系统 | 690 | 2026-11-16 | 表单、错误恢复和服务完成的模式。公共服务约束不能机械推广到所有产品。 |

<a id="stage-planning"></a>
## 07 优先级、路线图与排期

将已确认范围组织为任务和交付计划。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [makeplane/plane](https://github.com/makeplane/plane) | 可运行软件 | 62,549 | 2026-11-17 | 需求、任务、迭代与路线图协作。区分产品发现与项目进度；核对付费版边界。 |
| [opf/openproject](https://github.com/opf/openproject) | 可运行软件 | 17,457 | 2026-11-17 | 项目计划、协作与组织级交付。较重，先核对流程与部署成本。 |
| [taigaio/taiga-docker](https://github.com/taigaio/taiga-docker) | 可运行软件 | 2,177 | 2025-10-13 | 敏捷任务、看板与迭代。明确看板状态及完成定义，避免流程装饰。 |

<a id="stage-delivery"></a>
## 08 开发协作与接口

按契约实现并检验真实交付。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 可运行软件 | 80,835 | 2026-11-05 | API 协作、请求检查与接口验收。接口成功不等于用户界面流程通过。 |
| [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | Agent 工作流 | 11,630 | 2026-11-17 | GSD 当前主仓库的任务执行与工程交付。由旧仓库明确指向的新地址；关注新项目成熟度和实际执行权限。 |
| [stoplightio/prism](https://github.com/stoplightio/prism) | 开发工具 | 5,070 | 2026-11-13 | 按 API 描述模拟与验证契约。模拟接口必须与真实集成验证区分。 |

<a id="stage-qa"></a>
## 09 测试、可访问性与验收

检查用户成功、失败与恢复路径。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 测试框架 | 100,374 | 2026-11-17 | 核心路径与浏览器端到端验收。测试实际用户结果，不只检查按钮是否出现。 |
| [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | 测试框架 | 17,383 | 2026-11-17 | 业务规则和组件逻辑回归。选择重要行为，避免重复实现细节。 |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | 测试库 | 7,838 | 2026-11-16 | 自动检查可访问性问题。自动检测之外仍需键盘与辅助技术等适用验证。 |

<a id="stage-experiment"></a>
## 10 实验与验证

用适当设计判断假设与效果。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | 可运行软件 | 8,603 | 2026-11-17 | 实验、功能发布与效果分析。需要正确指标、样本与实验设计。README 区分 MIT 核心与商业许可目录。 |

<a id="stage-launch"></a>
## 11 发布、运行与回滚

可观察地发布，并能识别故障与采取行动。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 可运行软件 | 94,519 | 2026-11-17 | 服务可用性监控。服务可达不等于用户流程成功。 |
| [getsentry/sentry](https://github.com/getsentry/sentry) | 可运行软件 | 45,787 | 2026-11-17 | 上线错误、性能与故障定位。需配置采集和数据治理；平台许可需检查。 |
| [Unleash/unleash](https://github.com/Unleash/unleash) | 可运行软件 | 14,330 | 2026-11-17 | 功能开关和渐进发布。建立开关责任与清理机制，不代替回滚验证。 |
| [openstatusHQ/openstatus](https://github.com/openstatusHQ/openstatus) | 可运行软件 | 9,272 | 2026-11-17 | 监控、状态页与运行状态沟通。检查部署模式和告警责任。 |

<a id="stage-analytics"></a>
## 12 数据分析与业务复盘

定义正确指标，再从结果形成决定。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [apache/superset](https://github.com/apache/superset) | 可运行软件 | 75,538 | 2026-11-17 | 数据探索与企业分析。依赖数据接入与权限，图表不自动形成结论。 |
| [metabase/metabase](https://github.com/metabase/metabase) | 可运行软件 | 50,374 | 2026-11-17 | 业务指标探索与产品复盘看板。统一指标口径；注意社区与商业功能差异。README 区分 AGPL 开源版与商业版。 |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 可运行软件 | 40,836 | 2026-11-17 | 产品事件、漏斗、回放与实验。埋点含义与隐私采集规则必须先明确。 |
| [umami-software/umami](https://github.com/umami-software/umami) | 可运行软件 | 40,188 | 2026-11-17 | 网站流量和访问分析。流量指标不能直接当作产品价值验证。 |

<a id="stage-retro"></a>
## 13 团队回顾与改进

将反馈转为少量可执行行动。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [inovex/scrumlr.io](https://github.com/inovex/scrumlr.io) | 可运行软件 | 350 | 2026-11-17 | 团队回顾、收集意见与行动项。回顾要产生负责人和后续动作。 |

<a id="stage-similar"></a>
## 14 已有同类资源合集

查找相似索引与学习资料。

| 项目 | 类型 | Star 快照 | 最近推送（UTC） | 用途与采用边界 |
| --- | --- | ---: | --- | --- |
| [bradtraversy/design-resources-for-developers](https://github.com/bradtraversy/design-resources-for-developers) | 合集 | 67,416 | 2026-10-18 | 设计素材、UI 资源和工具合集。侧重设计资源，缺少完整公司评审流程。README 当前不接收新增资源，仍可修正既有链接。 |
| [dend/awesome-product-management](https://github.com/dend/awesome-product-management) | 合集 | 2,471 | 2026-11-07 | 产品管理资料与方法的综合索引。以阅读学习为主，不是可直接安装的工具套装。 |
| [aza-ali/awesome-ai-product-management](https://github.com/aza-ali/awesome-ai-product-management) | 合集 | 280 | 2026-05-24 | AI 产品经理相关方法和工具。与传统 PM 全流程覆盖分别比较。 |
| [bjpcjp/awesome-product-management](https://github.com/bjpcjp/awesome-product-management) | 合集 | 206 | 2019-05-13 | PM 主题、资源和工具索引。检查二次链接与适用阶段。 |

## 归档与迁移记录

| 历史仓库 | 状态 | 当前处理 |
| --- | --- | --- |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | 已归档，历史 Star 64,129 | 已归档；README 指向 open-gsd/gsd-core，作为迁移历史保留，不列为当前推荐。 |

## 维护与引用

目录引用上游，不复制整套代码或付费资产。各项目的代码、内容、社区版与商业版分别受其原许可约束；`NOASSERTION` 表示 GitHub 未识别单一许可，不表示可无条件使用。细节见 catalog 中的许可及 README 记录。

更新方法与收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)。这是一份按任务使用的目录，不要求把所有工具安装进同一项目。
