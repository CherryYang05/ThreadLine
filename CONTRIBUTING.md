# 贡献指南

ThreadLine 当前处于需求整理阶段。开始前请阅读 [README](README.md)、[需求来源](docs/requirements/sources.md) 和 [首版需求梳理](docs/requirements/mvp.md)。

## 提交改动

1. 查看现有 Issue 与分支，说明要解决的具体问题。
2. 从最新的默认分支创建独立分支。当前默认分支为 master。
3. 保持改动范围清晰，需求和行为变化同步更新相关文档与验收场景。
4. 提交 Pull Request，写明改动原因、验证方式和待解决的问题。

需求问题可使用[功能建议模板](.github/ISSUE_TEMPLATE/feature_request.yml)；文档、配置或实现缺陷可使用[问题反馈模板](.github/ISSUE_TEMPLATE/bug_report.yml)。

## 验证

目前没有应用测试或构建命令。文档及配置改动至少检查：

- git diff --check 无空白错误；暂存后也检查 git diff --cached --check。
- Markdown 相对链接指向现有文件。
- GitHub Issue 表单的 YAML 可解析，字段 ID 唯一，必填项合理。
- 项目状态、功能描述和执行结果与仓库实际内容一致。

引入代码时，随实现提供适用的验证命令，并在 PR 中记录实际执行结果。

## 资料与示例

使用合成学习记录和脱敏日志。不要提交真实用户数据、私有对话或凭据。引用新需求时说明来源版本，并将提案与已经明确的需求区分开。
