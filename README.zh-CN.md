<div align="center">

# Awesome Mobile GUI Agents

**人工精选的高质量开源 Mobile GUI Agent 合集。**

核验论文、官方实现、benchmark 证据与透明的项目元数据。

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

> 指标快照：**2026-07-15**（抓取时间 2026-07-15T09:34:53Z）。主目录：**20 个 Agent**。本文件由 [data/agents.yaml](data/agents.yaml) 生成，请勿手工修改表格。

## 为什么要做这个列表

Mobile GUI Agent 工作分散在研究原型、模型发布、自动化框架、benchmark 与产品仓库中。大型通用 GUI Agent 列表适合发现工作，但通常不能稳定回答三个实践问题：实现是否官方且真正开源？是否能操作真实或模拟的移动 GUI？论文引用数与仓库 star 是在什么时候测量的？

本目录通过人工审核条目和可复现快照回答这些问题。**它不是只关注错误恢复的列表。** 错误检测与恢复只是一个能力维度；我们同时记录规划、记忆、平台覆盖、感知与动作接口、工程封装和评测。

## 收录门槛

主榜条目必须同时满足：

1. 是完整 Agent 或具有实质可运行闭环的 Agent，而不只是模型、数据集、训练方案或 benchmark。
2. 能在真机、模拟器或可信动态环境中，通过 GUI 操作 Android、iOS 或 HarmonyOS。
3. 官方源码仓库公开，并带有明确的开源软件许可证。
4. 有文档化的安装或执行路径。
5. 提供移动 benchmark 证据或具体真机演示。
6. 链接、可运行路径、许可证与元数据都有审计日期。

排除规则、审计等级、论文去重和排序方法见 [METHODOLOGY.md](METHODOLOGY.md)。

## Established Agents

发布时间不晚于 **2025-07-15**，即快照时至少已发布 12 个月。以下 12 个条目按确定性的 impact score 排序：分别对 <code>log1p(OpenAlex citations)</code> 与 <code>log1p(GitHub stars)</code> 计算百分位秩，再等权平均。该分数只用于稳定排序，不是主观质量分级。

| Agent | 发布时间 | 平台 | 主要能力 | 证据 | 引用数 | GitHub stars | Impact | 审计 |
|---|---:|---|---|---|---:|---:|---:|---|
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1)<br><sub>[论文](https://arxiv.org/abs/2401.16158) · ICLR 2024 Workshop; CCL 2024 demo</sub> | 2024-01-29 | Android | 结合 OCR、图标检测与多模态推理的纯视觉 Android Agent。 | [Mobile-Eval](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#mobile-eval) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#quick_start) | 13 | 8,939<sup>family</sup> | 77.3 | links-verified<br><sub>2026-07-15</sub> |
| [AppAgent](https://github.com/TencentQQGYLab/AppAgent)<br><sub>[论文](https://arxiv.org/abs/2312.13771) · CHI 2025</sub> | 2023-12-21 | Android | 先学习应用交互知识、再复用于任务执行的 Android Agent。 | [Deployment demo](https://github.com/TencentQQGYLab/AppAgent#demo) · [Evaluation tasks](https://github.com/TencentQQGYLab/AppAgent/blob/main/assets/testset.md) | 47 | 6,812 | 72.7 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v2](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2)<br><sub>[论文](https://arxiv.org/abs/2406.01014) · NeurIPS 2024</sub> | 2024-06-03 | Android | 将规划、决策、反思与焦点记忆分离的多 Agent Android 系统。 | [Run guide](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2#run) · [Paper results](https://arxiv.org/abs/2406.01014) | 12 | 8,939<sup>family</sup> | 72.7 | links-verified<br><sub>2026-07-15</sub> |
| [AutoDroid](https://github.com/MobileLLM/AutoDroid)<br><sub>[论文](https://arxiv.org/abs/2308.15272) · MobiCom 2024</sub> | 2023-08-29 | Android | 基于 DroidBot，将自动探索与应用专属 LLM 记忆结合的 Android 任务 Agent。 | [Installation](https://github.com/MobileLLM/AutoDroid#how-to-install) · [Paper evaluation](https://doi.org/10.1145/3636534.3649379) | 88 | 480 | 68.2 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-E](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E)<br><sub>[论文](https://arxiv.org/abs/2501.11733) · arXiv 2025</sub> | 2025-01-20 | Android | 将动作结果反思转化为可复用任务经验的自进化 Android 助手。 | [Mobile-Eval-E](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#mobile-eval-e-benchmark) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#quick-start) | 3 | 8,939<sup>family</sup> | 68.2 | links-verified<br><sub>2026-07-15</sub> |
| [Midscene.js](https://github.com/web-infra-dev/midscene) | 2024-07-23 | Android, iOS, HarmonyOS | 覆盖 Android、iOS、HarmonyOS、Web 与桌面的工程化视觉自动化 Agent。 | [Mobile showcases](https://midscenejs.com/showcases) · [Android guide](https://midscenejs.com/android-getting-started) · [iOS guide](https://midscenejs.com/ios-getting-started) | — | 14,076 | 59.1 | links-verified<br><sub>2026-07-15</sub> |
| [M3A](https://github.com/google-research/android_world/tree/main/android_world/agents)<br><sub>[论文](https://arxiv.org/abs/2405.14573) · ICLR 2025</sub> | 2024-05-23 | Android | 随 AndroidWorld 动态 benchmark 发布的可运行多模态默认 Agent。 | [AndroidWorld](https://google-research.github.io/android_world/) · [Minimal M3A runner](https://github.com/google-research/android_world#quickstart) | 1 | 821 | 45.5 | links-verified<br><sub>2026-07-15</sub> |
| [MobileGPT](https://github.com/mobilegptsys/MobileGPT)<br><sub>[论文](https://arxiv.org/abs/2312.03003) · MobiCom 2024</sub> | 2023-12-04 | Android | 通过服务端与 Android 客户端协作、学习可复用应用流程的记忆型 Agent。 | [Server and client run guide](https://github.com/mobilegptsys/MobileGPT#run) · [Benchmark dataset](https://github.com/mobilegptsys/MobileGPT#benchmark-dataset) | 17 | 26 | 45.5 | links-verified<br><sub>2026-07-15</sub> |
| [Mobilerun](https://github.com/droidrun/mobilerun) | 2025-04-12 | Android, iOS | 为 LLM Agent 提供原生 Android/iOS 感知与控制工具的高采用度本地框架。 | [Project benchmark](https://mobilerun.ai/benchmark) · [Quick start](https://github.com/droidrun/mobilerun#quickstart) | — | 8,769 | 40.9 | links-verified<br><sub>2026-07-15</sub> |
| [MobileUse](https://github.com/MadeAgents/mobile-use)<br><sub>[论文](https://arxiv.org/abs/2507.16853) · NeurIPS 2025</sub> | 2025-02-27 | Android | 集成分层反思、主动探索与 benchmark 运行器的完整 Android Agent。 | [AndroidWorld and AndroidLab](https://github.com/MadeAgents/mobile-use#benchmark) · [Python API](https://github.com/MadeAgents/mobile-use#use-in-python) | 0 | 167 | 22.7 | links-verified<br><sub>2026-07-15</sub> |
| [App Use](https://github.com/erickjtorres/app-use) | 2025-05-16 | Android, iOS | 基于 Appium、用于控制真实 Android 与 iOS 应用的紧凑 Agent API。 | [iOS demos](https://github.com/erickjtorres/app-use#demos) · [Quick start](https://github.com/erickjtorres/app-use#quick-start) | — | 69 | 18.2 | links-verified<br><sub>2026-07-15</sub> |
| [CHOP](https://github.com/Yuqi-Zhou/CHOP)<br><sub>[论文](https://arxiv.org/abs/2503.03743) · arXiv 2025</sub> | 2025-02-12 | Android, HarmonyOS | 围绕可复用高频子任务约束规划的真机移动助手。 | [CHOP demo usage](https://github.com/Yuqi-Zhou/CHOP#chop-demo-usage) · [CHOP-En and CHOP-ZH](https://github.com/Yuqi-Zhou/CHOP#chop-en--chop-zh) | 0 | 8 | 9.1 | links-verified<br><sub>2026-07-15</sub> |

## Emerging Agents

发布时间晚于 **2025-07-15**。以下 8 个条目只按发布时间从新到旧列出，**不做排名**。我们仍展示 citation 与 star，但不假装新项目拥有相同的指标积累时间。

| Agent | 发布时间 | 平台 | 主要能力 | 证据 | 引用数 | GitHub stars | 审计 |
|---|---:|---|---|---|---:|---:|---|
| [TopoClaw](https://github.com/MadeAgents/TopoClaw) | 2026-04-23 | Android | 新近开源、具备 Android 客户端、skills 与主动执行能力的跨设备个人 Agent。 | [Project demos](https://github.com/MadeAgents/TopoClaw#-demo) · [Developer build](https://github.com/MadeAgents/TopoClaw#developer-build--run-commands) | — | 22 | links-verified<br><sub>2026-07-15</sub> |
| [Ghost in the Droid](https://github.com/ghost-in-the-droid/android-agent) | 2026-04-08 | Android | 融合 LLM Phone Agent、可复用 skills、MCP 工具与设备集群操作的 Android 框架。 | [Quick start](https://github.com/ghost-in-the-droid/android-agent#quick-start) · [MCP tools](https://github.com/ghost-in-the-droid/android-agent#mcp-server--give-any-ai-agent-an-android-body) | — | 240 | links-verified<br><sub>2026-07-15</sub> |
| [AppClaw](https://github.com/appclawhq/AppClaw) | 2026-03-23 | Android, iOS | 支持 Android 与 iOS 的新兴 TypeScript 移动 Agent 与测试运行器。 | [Demo and quick start](https://github.com/appclawhq/AppClaw#quickstart) · [Agent package](https://github.com/appclawhq/AppClaw/tree/main/packages/agent) | — | 94 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v3.5](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5)<br><sub>[论文](https://arxiv.org/abs/2602.16855) · arXiv 2026</sub> | 2026-02-15 | Android | 围绕 GUI-Owl-1.5 构建、已发布 Android 手机 runner 的最新 Mobile-Agent。 | [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#evaluation-on-androidworld) · [Mobile runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#deploy-gui-owl-15-on-your-mobile-device) | 0 | 8,939<sup>family</sup> | links-verified<br><sub>2026-07-15</sub> |
| [Open-AutoGLM Phone Agent](https://github.com/zai-org/Open-AutoGLM)<br><sub>[论文](https://arxiv.org/abs/2411.00820) · arXiv 2024</sub> | 2025-12-08 | Android, iOS, HarmonyOS | 围绕 AutoGLM 构建、覆盖 Android、iOS 与 HarmonyOS 的官方视觉 Phone Agent 运行时。 | [Phone Agent quick start](https://github.com/zai-org/Open-AutoGLM#快速开始) · [iOS setup](https://github.com/zai-org/Open-AutoGLM/blob/main/docs/ios_setup/ios_setup.md) | 1 | 25,781 | links-verified<br><sub>2026-07-15</sub> |
| [AgenticX-GUIAgent](https://github.com/DemonDamon/AgenticX-GUIAgent) | 2025-09-16 | Android | 显式划分 Manager、Executor、Reflector 与 Notetaker 的 Android 多 Agent 实现。 | [Run guide](https://github.com/DemonDamon/AgenticX-GUIAgent#run) · [Architecture](https://github.com/DemonDamon/AgenticX-GUIAgent#system-architecture) | — | 11 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v3](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3)<br><sub>[论文](https://arxiv.org/abs/2508.15144) · arXiv 2025</sub> | 2025-08-21 | Android | 基于 GUI-Owl、具备规划、进度管理、反思与记忆的多 Agent 框架。 | [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#evaluation-on-androidworld) · [Real-device runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#deploy-mobile-agent-v3-on-your-mobile-device) | 0 | 8,939<sup>family</sup> | links-verified<br><sub>2026-07-15</sub> |
| [mobile-use](https://github.com/minitap-ai/mobile-use)<br><sub>[论文](https://arxiv.org/abs/2602.07787) · arXiv 2026</sub> | 2025-08-16 | Android, iOS | 以任务分解和可复用 skills 为核心的本地 Android/iOS Agent 框架。 | [AndroidWorld report](https://minitap.ai/benchmark) · [Local quick start](https://github.com/minitap-ai/mobile-use#local-quick-start) | 0 | 2,680 | links-verified<br><sub>2026-07-15</sub> |

<sup>family</sup> 同一仓库包含多个已收录 Agent 代际，因此 star 是 family-level 指标，不能归因于某一个版本。

<details>
<summary><strong>运行时审计细节与局限</strong></summary>

| Agent | 感知 | 动作 | 恢复类型 | 可运行路径 | 许可证 | 最近 push | 主要局限 |
|---|---|---|---|---|---|---:|---|
| Mobile-Agent | screenshots, OCR, icon detection, visual grounding | ADB tap, swipe, text input, back, home | **none-documented** | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v1/run.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | 依赖多个外部模型，且没有独立的错误恢复模块。 |
| AppAgent | screenshots, OCR, visual element descriptions | ADB tap, swipe, text input, back, home | **none-documented** | [entrypoint](https://github.com/TencentQQGYLab/AppAgent/blob/main/run.py) | [MIT](https://github.com/TencentQQGYLab/AppAgent/blob/main/LICENSE) | 2025-03-19 | 公开仓库中可辨识的是原版 AppAgent，无法单独确认 AppAgent v2 实现。 |
| Mobile-Agent-v2 | screenshots, OCR, visual grounding | ADB tap, swipe, text input, back, home | **reflection** | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v2/run.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | 反思可能陷入循环，部署仍依赖多个模型服务。 |
| AutoDroid | UI hierarchy, screenshots, dynamic app exploration | ADB and DroidBot UI events | **none-documented** | [entrypoint](https://github.com/MobileLLM/AutoDroid/blob/main/batch_testing.py) | [MIT](https://github.com/MobileLLM/AutoDroid/blob/main/LICENSE) | 2024-03-22 | 仓库近期活跃度较低，且依赖主机侧 ADB，不能独立运行在端侧。 |
| Mobile-Agent-E | screenshots, OCR, visual grounding, action outcomes | ADB tap, swipe, text input, back, home | **reflection** | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-E/scripts/run_task.sh) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | 其反思主要提供高层指导，并非显式状态回滚或有保证的恢复。 |
| Midscene.js | screenshots, optional DOM, multimodal visual grounding | ADB Android actions, WebDriverAgent iOS actions, HarmonyOS actions | **replanning** | [entrypoint](https://github.com/web-infra-dev/midscene/blob/main/packages/android/src/cli.ts) | [MIT](https://github.com/web-infra-dev/midscene/blob/main/LICENSE) | 2026-07-15 | 它同时是测试与自动化平台，Agent 行为高度取决于所选多模态模型。 |
| M3A | screenshots, accessibility tree | AndroidEnv tap, swipe, text input, navigation and app actions | **retry** | [entrypoint](https://github.com/google-research/android_world/blob/main/minimal_task_runner.py) | [Apache-2.0](https://github.com/google-research/android_world/blob/main/LICENSE) | 2026-07-10 | 它主要是研究基线，默认配置模型较旧且依赖 API。 |
| MobileGPT | Android accessibility tree, app exploration state | Android accessibility actions | **none-documented** | [entrypoint](https://github.com/mobilegptsys/MobileGPT/blob/main/Server/main.py) | [Apache-2.0](https://github.com/mobilegptsys/MobileGPT/blob/main/LICENSE) | 2024-10-02 | 配置涉及多个组件、代码较旧，安装新应用后还需重新初始化记忆。 |
| Mobilerun | accessibility tree, screenshots, device state | Android portal actions, iOS portal actions, text and gestures, app launch | **replanning** | [entrypoint](https://github.com/droidrun/mobilerun/blob/main/mobilerun/cli/main.py) | [MIT](https://github.com/droidrun/mobilerun/blob/main/LICENSE) | 2026-07-06 | benchmark 结果由项目方维护，恢复也主要依赖迭代推理而非经过审计的状态还原。 |
| MobileUse | screenshots, multimodal model observations, repeated-state signals | ADB tap, swipe, text input, app launch, navigation keys | **replanning** | [entrypoint](https://github.com/MadeAgents/mobile-use/blob/master/pyproject.toml) | [MIT](https://github.com/MadeAgents/mobile-use/blob/master/LICENSE) | 2026-07-10 | 较强结果依赖大型外部 VLM，且没有采用统一的专用恢复 benchmark。 |
| App Use | Appium UI tree, screenshots, app state | Appium tap, swipe, text input, mobile gestures | **retry** | [entrypoint](https://github.com/erickjtorres/app-use/blob/main/examples/android_app_example.py) | [MIT](https://github.com/erickjtorres/app-use/blob/main/LICENSE) | 2026-07-10 | 它没有论文或标准 benchmark，可靠性受 Appium 与模型能力制约。 |
| CHOP | screenshots, Aria-UI grounding, task context | ADB tap, swipe, text input, navigation keys | **replanning** | [entrypoint](https://github.com/Yuqi-Zhou/CHOP/blob/main/src/run.py) | [MIT](https://github.com/Yuqi-Zhou/CHOP/blob/main/LICENSE) | 2025-03-08 | 评测规模较小，部分中文任务数据未发布，仓库也已较少维护。 |
| TopoClaw | mobile screenshots, desktop observations, proactive sensor events | Android client GUI actions, cross-device tools, desktop tools | **replanning** | [entrypoint](https://github.com/MadeAgents/TopoClaw/blob/main/TopoClaw/topoclaw/service/runtime.py) | [Apache-2.0](https://github.com/MadeAgents/TopoClaw/blob/main/LICENSE) | 2026-05-12 | 部署组件较多，iOS 尚在规划中，也未报告标准化移动 benchmark。 |
| Ghost in the Droid | screenshots, ADB UI hierarchy, live device stream | ADB tap, swipe, text input, app launch, device controls | **retry** | [entrypoint](https://github.com/ghost-in-the-droid/android-agent/blob/main/run.py) | [MIT](https://github.com/ghost-in-the-droid/android-agent/blob/main/LICENSE) | 2026-07-11 | 许多流程以 skill 驱动，通用 Agent 能力尚无学术移动 benchmark 支撑。 |
| AppClaw | screenshots, device UI observations | tap, type, swipe, mobile test actions | **retry** | [entrypoint](https://github.com/appclawhq/AppClaw/blob/main/packages/agent/src/cli.ts) | [Apache-2.0](https://github.com/appclawhq/AppClaw/blob/main/LICENSE) | 2026-07-13 | 项目较新、没有学术论文，也缺少独立 benchmark 证据。 |
| Mobile-Agent-v3.5 | screenshots, GUI-Owl-1.5 grounding, action history | ADB mobile actions, browser actions, desktop actions | **reflection** | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3.5/mobile_use/run_gui_owl_1_5_for_mobile.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | 已发布的手机 runner 是基于 ADB 的 Android 代码，不应把其他多平台表述理解为已发布 iOS 控制器。 |
| Open-AutoGLM Phone Agent | screenshots, vision-language model observations | ADB Android actions, HDC HarmonyOS actions, WebDriverAgent iOS actions | **retry** | [entrypoint](https://github.com/zai-org/Open-AutoGLM/blob/main/main.py) | [Apache-2.0](https://github.com/zai-org/Open-AutoGLM/blob/main/LICENSE) | 2026-03-06 | 当前代码仓库晚于论文发布，最强操作质量也依赖模型可用性。 |
| AgenticX-GUIAgent | screenshots, UI state, multimodal model observations | ADB basic actions, smart GUI tools | **reflection** | [entrypoint](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/main.py) | [MIT](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/LICENSE) | 2026-01-15 | 它是小型新兴项目，缺少论文、独立 benchmark 和长期维护记录。 |
| Mobile-Agent-v3 | screenshots, native GUI-Owl grounding, action history | ADB tap, swipe, text input, back, home | **reflection** | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | 运行最强配置需要大型 GUI-Owl 模型与较重的推理基础设施。 |
| mobile-use | screenshots, accessibility metadata, agent observations | ADB Android actions, iOS IDB actions | **replanning** | [entrypoint](https://github.com/minitap-ai/mobile-use/blob/main/minitap/mobile_use/main.py) | [Apache-2.0](https://github.com/minitap-ai/mobile-use/blob/main/LICENSE) | 2026-07-09 | AndroidWorld 100% 是项目方自报结果，也不是独立的错误恢复评测。 |

</details>

## Notable / Code Pending

这些论文相关性强、质量高，但只有在官方实现可公开核验后，才会进入开源 Agent 主榜；当前不排名、不计数。

| 工作 | Venue | 状态 | 待定原因 |
|---|---|---|---|
| [BacktrackAgent](https://aclanthology.org/2025.emnlp-main.212/) | EMNLP 2025 | code-pending | 显式进行结果条件化错误检测与回退，但截至审计日未发现官方公开实现。 |
| [Agent-SAMA](https://ojs.aaai.org/index.php/AAAI/article/view/40187) | AAAI 2026 | code-pending | 移动端稳定状态恢复证据很强，但未发现官方公开代码仓库。 |
| [VeriGUI](https://aclanthology.org/2026.acl-long.1335/) | ACL 2026 | code-pending | 直接研究动作效果验证与失败恢复训练，但未发现已发布的官方实现。 |
| [MobileExplorer](https://arxiv.org/abs/2605.26546) | arXiv 2026 | code-announced | 用两级 UI 回滚支持推测式并行探索；论文说明代码将在发表后发布。 |
| [D-Artemis](https://aclanthology.org/2026.findings-acl.681/) | Findings of ACL 2026 | public-repository-pending | 提供面向恢复的移动 GUI Agent 执行证据，但未核验到稳定的官方公开仓库。 |

## 公开仓库待资格确认

“代码公开”本身不等于满足主榜要求。下列项目需要解决许可证、实现身份或运行时完整性问题。

| 项目 | 状态 | 原因 |
|---|---|---|
| [AppAgent v2](https://github.com/TencentQQGYLab/AppAgent) | implementation-not-identifiable | 所链接仓库只可辨识出原版 AppAgent runner，没有 v2 分支、tag 或独立入口。 |
| [CoCo-Agent](https://github.com/xbmxb/CoCo-Agent) | license-pending | 研究代码已公开且可运行，但根仓库没有明确软件许可证。 |
| [MobA](https://github.com/OpenDFM/MobA) | license-pending | 官方仓库有代码与依赖文件，但没有明确根许可证。 |
| [AppAgentX](https://github.com/Westlake-AGI-Lab/AppAgentX) | license-pending | 官方仓库可运行，但可见许可证仅属于嵌套的第三方组件。 |
| [InfiGUIAgent](https://github.com/InfiXAI/InfiGUIAgent) | implementation-pending | 官方仓库目前只有 README 与图片，没有对应 Agent 实现。 |
| [UI-Venus](https://github.com/inclusionAI/UI-Venus) | license-pending | Agent 与模型代码已存在，但未核验到明确的根软件许可证。 |
| [OMG-Agent](https://github.com/Safphere/OMG-Agent) | source-available | 其 Apache 加 Commons Clause 条款包含商业与修改限制，因此不按 OSI 开源许可证处理。 |
| [OpenGUI](https://github.com/Core-Mate/OpenGUI) | source-available | 仓库采用 BUSL-1.1，要到 2030 年才转换为开源许可证。 |

## 相关资源

有用的模型、训练方法、数据集和环境会保留在这里，但**不计入主榜 Agent 数量**。

| 资源 | 类别 | 范围说明 |
|---|---|---|
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | Agent model and training | 公开模型推理、RFT 与离线评测代码；未核验到真机控制闭环，因此不计为完整 Agent。 |
| [Auto-UI](https://github.com/cooelf/Auto-GUI) | Agent model and training | 面向多模态动作链预测的训练与离线推理，并非已发布的实时移动控制器。 |
| [UI-S1](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1) | Training method | 半在线强化学习、数据集与模型资源，不作为独立运行时 Agent 条目。 |
| [MobileGym](https://github.com/Purewhiter/mobilegym) | Environment and benchmark | 面向 Agent 研究的浏览器托管 Android 仿真与评测环境。 |
| [AndroidWorld](https://github.com/google-research/android_world) | Environment and benchmark | 动态 Android benchmark 与环境；主榜仅计入其中可运行的 M3A 基线。 |

## 快照与审计语义

- **引用数：**只使用 OpenAlex。若预印本与正式发表版对应不同 OpenAlex work，快照计算引用任一版本的唯一 work 并集。
- **Stars：**抓取时官方 GitHub 仓库的 stargazer 数。共享 monorepo 标为 family-level。
- **links-verified：**已检查官方仓库、许可证、论文、证据和可运行路径。
- **code-inspected：**在上述基础上进一步检查相关 Agent loop 的实现。
- **install-smoke-tested：**实际执行文档化安装并成功完成最小启动。
- 没有论文时显示破折号；仅在计算 Established 表排序时按零引用处理。

所有历史快照保存在 [snapshots/](snapshots/)。

## 本地复现

~~~bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
python scripts/catalog.py validate
python scripts/catalog.py check
~~~

抓取新的在线快照并重新生成中英文 README：

~~~bash
GITHUB_TOKEN=... python scripts/catalog.py refresh --date YYYY-MM-DD
python scripts/catalog.py render
python scripts/catalog.py validate
pytest
~~~

每月 GitHub Actions 会创建指标刷新 PR，由人工复核后合并。

## 相关目录

- [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents) 是覆盖面很广、以论文为主的 GUI Agent 阅读列表。
- [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) 提供了广泛的结构化论文覆盖和配套网站。

它们都是很有价值的发现来源。本仓库采用不同的收录单位：高质量、开源、具有移动端运行闭环的 Agent，并提供带日期的 citation 与 GitHub 快照。从其他列表获得的候选链接仍会在这里独立核验。

## 贡献

新增 Agent 建议必须先提交 issue，而不是直接提交目录 PR，以便明确记录收录判断。对应 issue 被接受后，欢迎提交元数据纠错与工具改进。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

目录数据、文档与生成的 README 采用 [CC BY 4.0](LICENSES/CC-BY-4.0.txt)；脚本与测试采用 [MIT](LICENSES/MIT.txt)。上游项目保留各自许可证。
