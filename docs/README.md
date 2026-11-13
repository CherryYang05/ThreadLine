# 文档索引

项目仍在调研和需求完善阶段。以下五份文件是早期草稿，按材料用途归档；其中的方案、分期、评分口径与验收设想仍可修改。

| 类别 | 草稿 | 内容 |
| --- | --- | --- |
| 产品需求 | [ThreadLine 产品需求](prd/threadline.draft.md) | 产品问题、整体流程、页面与分期设想 |
| 产品需求 | [领域能力追踪需求](prd/domain-assessment.draft.md) | 能力基准、计划目标、证据与学习档案的产品设想 |
| 调研依据 | [学习评估调研](research/learning-assessment.draft.md) | 相关研究、设计推测与待验证问题 |
| 设计方案 | [评分与数据设计](design/scoring-and-data.draft.md) | 拟议的计分口径、对象关系、接口和纠错方案 |
| 设计示例 | [RSI 基准与计划样例](design/rsi-benchmark-example.draft.md) | 合成量表与预期行为示例 |

了解整体产品先读产品需求草稿；讨论评估方案时再结合调研、领域需求和设计草稿阅读。

## 命名与位置

- `research/` 放证据、假设和待验证问题。
- `prd/` 放产品意图、使用场景和需求工作稿。
- `design/` 放探索中的数据、评分、接口方案及示例。
- `architecture/decisions/` 放已作出的技术或流程选择及理由，使用 ADR 编号。
- `development/` 放协作与开发流程。

文件名用描述性的英文小写与连字符，草稿使用 `.draft.md` 后缀；日期放在文内并通过 Git 保留修订历史。不以 01–04 这样的阅读顺序编号代替内容名称，ADR 的决策编号保留。

## 与 OpenSpec 的关系

这里的草稿用于研究和讨论。后续进入具体开发变更时，再由 change 引用相关依据，写出本次行为差异、设计与任务；完成实施和验证后同步主规格。草稿移动或改名不会使其成为当前系统行为。

框架见 [OpenSpec 架构](../openspec/README.md)，开发方式见[工作流](development/workflow.md)，当前阶段见 [STATUS](../STATUS.md)。
