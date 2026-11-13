# ThreadLine

一个用于跨会话接续学习、管理计划与学习记录的私人工作台。GPT 负责自然语言交互，工作台承载可查看、可纠正的数据；产品范围仍在调研和完善。

**当前仅完成仓库与 AI 开发流程初始化。** 现有 PRD 是工作草稿，尚未拆分能力规格、安排产品实施任务或选择应用技术栈。

## 文档入口

| 内容 | 入口 |
| --- | --- |
| 产品需求工作稿 | [总 PRD](docs/prd/PRD.md) |
| 能力追踪研究与需求 | [研究说明](docs/prd/01-assessment-research.md) · [领域能力 PRD](docs/prd/02-research-maturity-prd.md) |
| 数据与评分设计工作稿 | [数据契约](docs/prd/03-scoring-and-data-spec.md) · [RSI 样例](docs/prd/04-rsi-benchmark-fixture.md) |
| 当前阶段与接手入口 | [STATUS.md](STATUS.md) · [AGENTS.md](AGENTS.md) |
| 规格架构与开发流程 | [OpenSpec 结构](openspec/README.md) · [工作流](docs/development/workflow.md) |
| 框架选择理由 | [ADR 0001](docs/architecture/decisions/0001-spec-driven-development.md) |

## AI 开发框架

采用 **OpenSpec + 通用 AGENTS.md + Git/PR 审阅 + 自动检查**。使用官方 `spec-driven` schema 和精确固定的 CLI 版本，不依赖某一种 AI 客户端。

```text
AGENTS.md                 AI 协作规则
STATUS.md                 当前阶段与交接入口
docs/
  prd/                    用户上传的需求工作稿，保留原文
  research/               后续调研材料与待验证结论
  architecture/decisions/ 框架与技术决策记录
  development/            开发工作流
openspec/
  config.yaml             共享配置与通用约束
  specs/                  当前系统行为规格，目前为空
  changes/
    archive/              已完成变更，目前为空
scripts/                  仓库与规格检查
.github/                  CI、Issue 和 PR 模板
```

调研和 PRD 不会自动变成已确认规格。后续进入具体开发时，再创建包含方案、设计、任务与必要规格差异的 change；实现并验证后同步主规格、归档变更。目录语义见 [OpenSpec 说明](openspec/README.md)。

## 本地检查

需要 Node.js 22.12 或更高版本（CI 使用 Node 24）、npm、Python 3.9 或更高版本，以及 Git。

```bash
npm ci --ignore-scripts
npm run check
npm exec -- openspec list
```

`npm run check` 检查文本和仓库内链接；有规格或活动变更时执行 OpenSpec 严格校验。目前规格目录为空，会明确报告跳过。

npm 依赖只用于规格工具，尚无应用启动、数据库或部署配置。后续产品开发沿用这套框架，应用技术选型另记 ADR。
