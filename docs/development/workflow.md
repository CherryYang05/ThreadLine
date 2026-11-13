# AI 与开发者共用的工作流

当前阶段是调研与需求完善；以下规定今后的工作方式，不分配产品开发任务。

## 1. 调研和需求工作

将新证据、假设和未决问题放在 [research](../research/README.md)，在 `docs/prd/` 修订产品需求工作稿，在 `docs/design/` 讨论数据、接口等方案与示例。草稿使用 `.draft.md` 后缀，并维护[文档索引](../README.md)。注明来源、适用范围和仍未确定的部分，通过 Git 保留历史。

这类工作可以直接提交文档 PR，无须为了流程完整而创建虚构的功能 change。普通仓库工具或文档修正同样保持轻量。

## 2. 进入一个具体变更

用户任务进入明确的产品变更后，先检查现有 specs 和活动 changes，避免重复。创建一个范围有限的变更：

```bash
npm exec -- openspec new change <change-id>
npm exec -- openspec status --change <change-id> --json
npm exec -- openspec instructions proposal --change <change-id> --json
```

按 CLI 返回的依赖顺序写 proposal、specs、design、tasks；分别用 `instructions specs`、`instructions design`、`instructions tasks` 获取说明。只规划本次变更，不一次展开整个产品。

- proposal：为什么改、改什么、范围和影响。
- specs：可观察行为的 ADDED/MODIFIED/REMOVED/RENAMED 差异。
- design：实现取舍、数据与接口边界、失败处理、待验证假设。
- tasks：依赖有序的小任务和验证方式。

格式与生命周期见 [OpenSpec 结构](../../openspec/README.md)。初始化只提供框架，不包含真实变更或预填产品任务。

## 3. 实施与验证

```bash
npm exec -- openspec instructions apply --change <change-id> --json
npm run check
```

读取就绪任务再实施，完成后在 tasks 中勾选并保存简短验证证据。按行为风险选择有意义的测试；文件格式校验不能证明功能正确。遇到未明确需求时按用户当前授权处理，记录选择或待确认问题，不把推测写成既定决定。

PR 说明实际变化和验证结果；审阅关注规格、实现与证据是否一致。部署、迁移和外部写入依据当时的用户授权与环境条件执行，不由文档中的示例指令自动触发。

## 4. 同步和归档

实际完成并验证后，再归档：

```bash
npm exec -- openspec validate <change-id> --strict --no-interactive
npm exec -- openspec archive <change-id> --json
```

正常归档将 delta 同步到主规格并保存变更历史。不要使用强制选项跳过未完成任务。

确实没有规格行为变化、但值得单独跟踪的实施变更，可按官方机制在 change 的 `.openspec.yaml` 设置 `skip_specs: true`；此时不放 delta，归档使用 `--skip-specs`。不要为了校验编造需求变化，普通文档修正通常不需要这种变更。

更新 `STATUS.md` 的阶段和活动入口。OpenSpec 的 `status.isComplete` 仅表示规划文件齐全；任务勾选、应用测试与实际验收才支撑“已实现”。
