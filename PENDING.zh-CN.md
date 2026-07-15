# 待审核条目

[返回主目录](README.zh-CN.md) · [English](PENDING.md)

这些候选项目不计入主目录。只有在官方实现及所需资格证据均可核验后，条目才会移入主目录。

## 等待官方代码的论文

| 工作 | Venue | 状态 | 待核验问题 |
|---|---|---|---|
| [BacktrackAgent](https://aclanthology.org/2025.emnlp-main.212/) | EMNLP 2025 | `code-pending` | 显式进行结果条件化错误检测与回退，但截至审计日未发现官方公开实现。 |
| [Agent-SAMA](https://ojs.aaai.org/index.php/AAAI/article/view/40187) | AAAI 2026 | `code-pending` | 移动端稳定状态恢复证据很强，但未发现官方公开代码仓库。 |
| [VeriGUI](https://aclanthology.org/2026.acl-long.1335/) | ACL 2026 | `code-pending` | 直接研究动作效果验证与失败恢复训练，但未发现已发布的官方实现。 |
| [MobileExplorer](https://arxiv.org/abs/2605.26546) | arXiv 2026 | `code-announced` | 用两级 UI 回滚支持推测式并行探索；论文说明代码将在发表后发布。 |
| [D-Artemis](https://aclanthology.org/2026.findings-acl.681/) | Findings of ACL 2026 | `public-repository-pending` | 提供面向恢复的移动 GUI Agent 执行证据，但未核验到稳定的官方公开仓库。 |

## 等待资格确认的仓库

| 项目 | 状态 | 待核验问题 |
|---|---|---|
| [AppAgent v2](https://github.com/TencentQQGYLab/AppAgent) | `implementation-not-identifiable` | 所链接仓库只可辨识出原版 AppAgent runner，没有 v2 分支、tag 或独立入口。 |
| [CoCo-Agent](https://github.com/xbmxb/CoCo-Agent) | `license-pending` | 研究代码已公开且可运行，但根仓库没有明确软件许可证。 |
| [MobA](https://github.com/OpenDFM/MobA) | `license-pending` | 官方仓库有代码与依赖文件，但没有明确根许可证。 |
| [AppAgentX](https://github.com/Westlake-AGI-Lab/AppAgentX) | `license-pending` | 官方仓库可运行，但可见许可证仅属于嵌套的第三方组件。 |
| [InfiGUIAgent](https://github.com/InfiXAI/InfiGUIAgent) | `implementation-pending` | 官方仓库目前只有 README 与图片，没有对应 Agent 实现。 |
| [UI-Venus](https://github.com/inclusionAI/UI-Venus) | `license-pending` | Agent 与模型代码已存在，但未核验到明确的根软件许可证。 |
| [OMG-Agent](https://github.com/Safphere/OMG-Agent) | `source-available` | 其 Apache 加 Commons Clause 条款包含商业与修改限制，因此不按 OSI 开源许可证处理。 |
| [OpenGUI](https://github.com/Core-Mate/OpenGUI) | `source-available` | 仓库采用 BUSL-1.1，要到 2030 年才转换为开源许可证。 |

主目录要求见 [METHODOLOGY.md](METHODOLOGY.md)，新增或更新条目的流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。
