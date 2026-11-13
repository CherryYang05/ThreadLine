# OpenSpec 架构

本仓库使用官方 OpenSpec 2.0.0 的 `spec-driven` schema。当前只有框架：`specs/` 与 `changes/archive/` 留空，没有产品能力拆分或活动实施变更。

## 各层保存什么

| 层 | 位置 | 语义 |
| --- | --- | --- |
| 证据与假设 | `docs/research/` | 发现、来源、推测、待验证问题 |
| 产品工作稿 | `docs/prd/` | 产品意图与仍在完善的需求，不因入库就视为确认 |
| 探索性设计 | `docs/design/` | 数据、评分、接口方案与示例，仍待讨论 |
| 变更提案 | `openspec/changes/<id>/proposal.md` | 某次具体改动的动机、范围与影响 |
| 设计与任务 | 同一 change 的 `design.md`、`tasks.md` | 技术取舍及实施/验收状态 |
| 规格差异 | 同一 change 的 `specs/<capability>/spec.md` | 本次新增、修改、移除或重命名的行为 |
| 当前主规格 | `openspec/specs/<capability>/spec.md` | 已实现并验证、当前有效的系统行为 |
| 已完成变更 | `openspec/changes/archive/` | 变更提案、差异、设计与完成证据的历史 |

路径中的 `<id>` 和 `<capability>` 是格式占位，不是预定的产品模块。

早期材料按用途整理在[文档索引](../docs/README.md)，使用 `.draft.md` 标识。探索性设计留在 `docs/design/`；具体开发变更确定后，相关设计取舍写入该 change 的 `design.md`，已采纳的架构选择再记录为 ADR。

## 未来规格的格式

主规格使用 `## Purpose`、`## Requirements`、`### Requirement: ...` 与 `#### Scenario: ...`。需求含 SHALL/MUST，场景含 WHEN/THEN；正文可用中文。需求命名应稳定、可追踪，并引用对应来源。

差异按官方格式使用 ADDED/MODIFIED/REMOVED/RENAMED Requirements。修改项包含完整需求和场景，避免仅有一句修改说明而无法合并。

不在此提供具体产品示例，以免示例被当作已确认需求。创建变更时通过 CLI `instructions` 获取固定版本的模板和依赖关系，完整命令见[工作流](../docs/development/workflow.md)。

## 框架边界

- 当前 PRD 仍在完善；不从它批量生成主规格。
- 只有明确进入一个具体开发变更，才建立对应 proposal、delta、design 和 tasks。
- 只有实际实现并验证完成，才同步主规格并归档。
- 本仓库未安装客户端专用技能或 slash commands；通用 CLI 是可用入口。
- 主规格与活动变更为空时，检查会明确跳过；未来存在内容时使用官方严格验证。
