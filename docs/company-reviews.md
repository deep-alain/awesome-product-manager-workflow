# 公司产品评审：从证据到决策

以下按常见产品团队工作定义决策点，并非任一公司的内部制度，也不要求每项召开一次会议。小改动可以合并、异步完成；高风险变更才需要对应负责人参与。AI 给出的角色意见不能替代有权限的实际负责人。

| 决策环节 | 进入评审前的输入 | 要回答的问题 | 退出时应留下什么 | 典型参与者 | 对应 GitHub 参考 |
| --- | --- | --- | --- | --- | --- |
| 机会与立项 | 用户问题、现状、价值假设、资源边界 | 值不值得做？最弱假设是什么？是否有更小的验证？ | 继续/验证/暂缓的决定、目标与非目标、责任人 | PM、业务负责人、技术/设计代表 | [PM Skills](https://github.com/phuryn/pm-skills)、[Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)、[gstack](https://github.com/garrytan/gstack) |
| 需求与范围 | PRD、用户流程、支持情境、数据定义 | 用户真正获得什么？哪些要求有依据？完成如何判断？ | 核心流程、验收条件、不做项、未定问题 | PM、设计、开发、QA | [Spec Kit](https://github.com/github/spec-kit)、[OpenSpec](https://github.com/Fission-AI/OpenSpec)、[Awesome PM Skills](https://github.com/menkesu/awesome-pm-skills) |
| 交互与视觉 | 可查看原型、真实长度内容、核心状态 | 主任务能否完成？失败是否可恢复？是否把工作要求写成多余文案？ | 关键状态、行为说明、视觉/组件约定和待验证假设 | PM、设计、前端、可访问性相关人员 | [Penpot](https://github.com/penpot/penpot)、[Storybook](https://github.com/storybookjs/storybook)、[GOV.UK Design System](https://github.com/alphagov/govuk-design-system)、[gstack](https://github.com/garrytan/gstack) |
| 技术方案与接口 | 方案选项、受影响系统、接口和数据变化 | 为什么选此方案？失败/权限/一致性如何处理？维护成本是否合理？ | 简短 ADR 或 RFC、接口契约、风险与验证计划 | 技术负责人、开发、PM、QA | [ADR](https://github.com/architecture-decision-record/architecture-decision-record)、[Rust RFCs](https://github.com/rust-lang/rfcs)、[工程手册](https://github.com/microsoft/code-with-engineering-playbook)、[Prism](https://github.com/stoplightio/prism) |
| 安全、隐私与 AI 风险 | 数据流、权限、采集范围、模型/供应商依赖 | 谁能访问什么？收集是否必要？AI 结果如何复核？ | 实际适用的控制、残余风险、风险接受责任人 | 安全、隐私/法务、技术、业务负责人 | [OWASP ASVS](https://github.com/OWASP/ASVS)、[Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)；这些材料不能替代法律意见 |
| 测试与验收 | 验收标准、测试环境、真实运行证据 | 核心成功/失败路径是否可复现？哪些尚未验证？ | 缺陷处理决定、通过证据、准确的未测范围 | QA、开发、PM；相关业务验收者 | [Playwright](https://github.com/microsoft/playwright)、[Vitest](https://github.com/vitest-dev/vitest)、[axe-core](https://github.com/dequelabs/axe-core)、[Hoppscotch](https://github.com/hoppscotch/hoppscotch) |
| 发布 Go / No-Go | 上述重要问题的结论、发布/回滚方案、监控与负责人 | 能否在支持条件下交付？如何发现并处理失败？ | 发布或延期、观察窗口、回滚条件与执行人 | 发布负责人、技术、PM、运维/支持 | [Unleash](https://github.com/Unleash/unleash)、[Sentry](https://github.com/getsentry/sentry)、[Uptime Kuma](https://github.com/louislam/uptime-kuma)、[OpenStatus](https://github.com/openstatusHQ/openstatus) |
| 效果、业务与团队复盘 | 目标指标、实际数据、用户反馈、事件时间线 | 结果是否支持假设？哪里有返工/浪费？下一步改什么？ | 继续/调整/停止的决定、少量有负责人的行动项 | PM、数据、设计、开发、业务/支持 | [PostHog](https://github.com/PostHog/posthog)、[Metabase](https://github.com/metabase/metabase)、[GrowthBook](https://github.com/growthbook/growthbook)、[scrumlr.io](https://github.com/inovex/scrumlr.io) |

## 怎样引用 AI 评审包

gstack README 当前列出 `/plan-ceo-review`、`/plan-eng-review`、`/plan-design-review`、`/design-review`、`/review`、`/qa`、`/ship`、`/retro` 等角色工作。它们提供不同视角，不能据此认定公司已批准上线。特别是 `/ship` 可涉及推送或 PR，应按本次任务授权使用。原仓库还提供扩张/保持范围/缩减等不同模式，不能把扩张模式设为所有 MVP 的默认。

PM Skills 和 Product Manager Skills 更接近产品方法与工作产物；Spec Kit / OpenSpec 接近需求到变更执行；ADR / RFC 负责记录重要决定与理由。可以组合它们，但先确定本次决定，再加载对应能力，避免同时装入所有方法导致输出相互冲突。

## 一份可直接复制的简短评审记录

见 [decision-review.md](../templates/decision-review.md)。每项写事实、假设、决定和责任。没有证据时记录未知，会议数量和文档长度不代表质量。

正式签署另有需要时可参考 [DocuSeal](https://github.com/docusealco/docuseal)，但电子签字只是签署工具，不等于需求合理或审批权限正确。
