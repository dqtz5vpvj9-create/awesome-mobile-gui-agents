<div align="center">

# Awesome Mobile GUI Agents

**A manually curated collection of high-quality, open-source Mobile GUI Agents.**

Verified papers, official implementations, benchmark evidence, and transparent project metadata.

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

> Metrics snapshot: **2026-07-15** (retrieved 2026-07-15T09:34:53Z). Main catalog: **20 agents**. This file is generated from [data/agents.yaml](data/agents.yaml); do not edit the tables by hand.

## Why this list exists

Mobile GUI Agent work is split across research prototypes, model releases, automation frameworks, benchmarks, and product repositories. Large general GUI-agent lists are useful for discovery, but they do not consistently answer three practical questions: Is the implementation official and open-source? Can it operate a real or emulated mobile GUI? When were its paper citations and repository stars measured?

This catalog answers those questions with manually reviewed entries and reproducible snapshots. **It is not a recovery-only list.** Error detection and recovery are recorded as one capability dimension alongside planning, memory, platform coverage, perception, action interfaces, packaging, and evaluation.

## Inclusion bar

A main-list entry must satisfy all of the following:

1. It is a complete agent or a meaningfully runnable agent loop, not only a model, dataset, training recipe, or benchmark.
2. It operates Android, iOS, or HarmonyOS through the graphical interface on a real device, emulator, simulator, or a faithful live environment.
3. Its official source repository is public and carries an explicit open-source software license.
4. It has a documented installation or execution path.
5. It provides mobile benchmark evidence or a concrete real-device demo.
6. Its links, runnable path, license, and metadata have an audit date.

See [METHODOLOGY.md](METHODOLOGY.md) for exclusions, audit levels, paper deduplication, and ordering.

## Established agents

Released on or before **2025-07-15** (at least 12 months old at the snapshot). These 12 entries are ordered by a deterministic impact score: the equal-weight mean of percentile ranks over <code>log1p(OpenAlex citations)</code> and <code>log1p(GitHub stars)</code>. The score orders the table; it is not a quality tier.

| Agent | Released | Platforms | What it provides | Evidence | Citations | GitHub stars | Impact | Audit |
|---|---:|---|---|---|---:|---:|---:|---|
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1)<br><sub>[paper](https://arxiv.org/abs/2401.16158) · ICLR 2024 Workshop; CCL 2024 demo</sub> | 2024-01-29 | Android | A screen-only Android agent combining OCR, icon detection, and multimodal reasoning. | [Mobile-Eval](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#mobile-eval) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#quick_start) | 13 | 8,939<sup>family</sup> | 77.3 | links-verified<br><sub>2026-07-15</sub> |
| [AppAgent](https://github.com/TencentQQGYLab/AppAgent)<br><sub>[paper](https://arxiv.org/abs/2312.13771) · CHI 2025</sub> | 2023-12-21 | Android | An Android agent that first learns app-specific interaction knowledge, then reuses it for task execution. | [Deployment demo](https://github.com/TencentQQGYLab/AppAgent#demo) · [Evaluation tasks](https://github.com/TencentQQGYLab/AppAgent/blob/main/assets/testset.md) | 47 | 6,812 | 72.7 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v2](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2)<br><sub>[paper](https://arxiv.org/abs/2406.01014) · NeurIPS 2024</sub> | 2024-06-03 | Android | A multi-agent Android system separating planning, decision, reflection, and focus memory. | [Run guide](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2#run) · [Paper results](https://arxiv.org/abs/2406.01014) | 12 | 8,939<sup>family</sup> | 72.7 | links-verified<br><sub>2026-07-15</sub> |
| [AutoDroid](https://github.com/MobileLLM/AutoDroid)<br><sub>[paper](https://arxiv.org/abs/2308.15272) · MobiCom 2024</sub> | 2023-08-29 | Android | A DroidBot-based Android task agent that combines automated exploration with app-specific LLM memory. | [Installation](https://github.com/MobileLLM/AutoDroid#how-to-install) · [Paper evaluation](https://doi.org/10.1145/3636534.3649379) | 88 | 480 | 68.2 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-E](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E)<br><sub>[paper](https://arxiv.org/abs/2501.11733) · arXiv 2025</sub> | 2025-01-20 | Android | A self-evolving Android assistant that converts outcome reflection into reusable task experience. | [Mobile-Eval-E](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#mobile-eval-e-benchmark) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#quick-start) | 3 | 8,939<sup>family</sup> | 68.2 | links-verified<br><sub>2026-07-15</sub> |
| [Midscene.js](https://github.com/web-infra-dev/midscene) | 2024-07-23 | Android, iOS, HarmonyOS | A production-oriented visual automation agent spanning Android, iOS, HarmonyOS, web, and desktop. | [Mobile showcases](https://midscenejs.com/showcases) · [Android guide](https://midscenejs.com/android-getting-started) · [iOS guide](https://midscenejs.com/ios-getting-started) | — | 14,076 | 59.1 | links-verified<br><sub>2026-07-15</sub> |
| [M3A](https://github.com/google-research/android_world/tree/main/android_world/agents)<br><sub>[paper](https://arxiv.org/abs/2405.14573) · ICLR 2025</sub> | 2024-05-23 | Android | The runnable multimodal default agent shipped with the AndroidWorld live benchmark. | [AndroidWorld](https://google-research.github.io/android_world/) · [Minimal M3A runner](https://github.com/google-research/android_world#quickstart) | 1 | 821 | 45.5 | links-verified<br><sub>2026-07-15</sub> |
| [MobileGPT](https://github.com/mobilegptsys/MobileGPT)<br><sub>[paper](https://arxiv.org/abs/2312.03003) · MobiCom 2024</sub> | 2023-12-04 | Android | A server-plus-Android-client agent that learns reusable app procedures with human-like memory. | [Server and client run guide](https://github.com/mobilegptsys/MobileGPT#run) · [Benchmark dataset](https://github.com/mobilegptsys/MobileGPT#benchmark-dataset) | 17 | 26 | 45.5 | links-verified<br><sub>2026-07-15</sub> |
| [Mobilerun](https://github.com/droidrun/mobilerun) | 2025-04-12 | Android, iOS | A widely adopted local framework giving LLM agents native Android and iOS inspection and control tools. | [Project benchmark](https://mobilerun.ai/benchmark) · [Quick start](https://github.com/droidrun/mobilerun#quickstart) | — | 8,769 | 40.9 | links-verified<br><sub>2026-07-15</sub> |
| [MobileUse](https://github.com/MadeAgents/mobile-use)<br><sub>[paper](https://arxiv.org/abs/2507.16853) · NeurIPS 2025</sub> | 2025-02-27 | Android | A complete Android agent with hierarchical reflection, proactive exploration, and benchmark integrations. | [AndroidWorld and AndroidLab](https://github.com/MadeAgents/mobile-use#benchmark) · [Python API](https://github.com/MadeAgents/mobile-use#use-in-python) | 0 | 167 | 22.7 | links-verified<br><sub>2026-07-15</sub> |
| [App Use](https://github.com/erickjtorres/app-use) | 2025-05-16 | Android, iOS | A compact Appium-backed Agent API for controlling real Android and iOS applications. | [iOS demos](https://github.com/erickjtorres/app-use#demos) · [Quick start](https://github.com/erickjtorres/app-use#quick-start) | — | 69 | 18.2 | links-verified<br><sub>2026-07-15</sub> |
| [CHOP](https://github.com/Yuqi-Zhou/CHOP)<br><sub>[paper](https://arxiv.org/abs/2503.03743) · arXiv 2025</sub> | 2025-02-12 | Android, HarmonyOS | A real-device mobile assistant that constrains planning around reusable high-frequency subtasks. | [CHOP demo usage](https://github.com/Yuqi-Zhou/CHOP#chop-demo-usage) · [CHOP-En and CHOP-ZH](https://github.com/Yuqi-Zhou/CHOP#chop-en--chop-zh) | 0 | 8 | 9.1 | links-verified<br><sub>2026-07-15</sub> |

## Emerging agents

Released after **2025-07-15**. These 8 entries are listed newest first and are intentionally **not ranked**. Citation and star counts remain visible without pretending that a young project has had the same time to accumulate them.

| Agent | Released | Platforms | What it provides | Evidence | Citations | GitHub stars | Audit |
|---|---:|---|---|---|---:|---:|---|
| [TopoClaw](https://github.com/MadeAgents/TopoClaw) | 2026-04-23 | Android | A newly open-sourced cross-device personal agent with an Android client, skills, and proactive execution. | [Project demos](https://github.com/MadeAgents/TopoClaw#-demo) · [Developer build](https://github.com/MadeAgents/TopoClaw#developer-build--run-commands) | — | 22 | links-verified<br><sub>2026-07-15</sub> |
| [Ghost in the Droid](https://github.com/ghost-in-the-droid/android-agent) | 2026-04-08 | Android | An Android automation framework combining an LLM phone agent, reusable skills, MCP tools, and fleet operations. | [Quick start](https://github.com/ghost-in-the-droid/android-agent#quick-start) · [MCP tools](https://github.com/ghost-in-the-droid/android-agent#mcp-server--give-any-ai-agent-an-android-body) | — | 240 | links-verified<br><sub>2026-07-15</sub> |
| [AppClaw](https://github.com/appclawhq/AppClaw) | 2026-03-23 | Android, iOS | An emerging TypeScript mobile agent and test runner with Android and iOS support. | [Demo and quick start](https://github.com/appclawhq/AppClaw#quickstart) · [Agent package](https://github.com/appclawhq/AppClaw/tree/main/packages/agent) | — | 94 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v3.5](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5)<br><sub>[paper](https://arxiv.org/abs/2602.16855) · arXiv 2026</sub> | 2026-02-15 | Android | The current Mobile-Agent generation built around GUI-Owl-1.5, with a released Android phone runner. | [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#evaluation-on-androidworld) · [Mobile runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#deploy-gui-owl-15-on-your-mobile-device) | 0 | 8,939<sup>family</sup> | links-verified<br><sub>2026-07-15</sub> |
| [Open-AutoGLM Phone Agent](https://github.com/zai-org/Open-AutoGLM)<br><sub>[paper](https://arxiv.org/abs/2411.00820) · arXiv 2024</sub> | 2025-12-08 | Android, iOS, HarmonyOS | An official visual Phone Agent runtime for Android, iOS, and HarmonyOS built around AutoGLM. | [Phone Agent quick start](https://github.com/zai-org/Open-AutoGLM#快速开始) · [iOS setup](https://github.com/zai-org/Open-AutoGLM/blob/main/docs/ios_setup/ios_setup.md) | 1 | 25,781 | links-verified<br><sub>2026-07-15</sub> |
| [AgenticX-GUIAgent](https://github.com/DemonDamon/AgenticX-GUIAgent) | 2025-09-16 | Android | An Android multi-agent implementation with explicit manager, executor, reflector, and notetaker roles. | [Run guide](https://github.com/DemonDamon/AgenticX-GUIAgent#run) · [Architecture](https://github.com/DemonDamon/AgenticX-GUIAgent#system-architecture) | — | 11 | links-verified<br><sub>2026-07-15</sub> |
| [Mobile-Agent-v3](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3)<br><sub>[paper](https://arxiv.org/abs/2508.15144) · arXiv 2025</sub> | 2025-08-21 | Android | A GUI-Owl-based multi-agent framework with planning, progress tracking, reflection, and memory. | [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#evaluation-on-androidworld) · [Real-device runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#deploy-mobile-agent-v3-on-your-mobile-device) | 0 | 8,939<sup>family</sup> | links-verified<br><sub>2026-07-15</sub> |
| [mobile-use](https://github.com/minitap-ai/mobile-use)<br><sub>[paper](https://arxiv.org/abs/2602.07787) · arXiv 2026</sub> | 2025-08-16 | Android, iOS | A local Android and iOS agent framework centered on task decomposition and reusable skills. | [AndroidWorld report](https://minitap.ai/benchmark) · [Local quick start](https://github.com/minitap-ai/mobile-use#local-quick-start) | 0 | 2,680 | links-verified<br><sub>2026-07-15</sub> |

<sup>family</sup> The repository hosts multiple cataloged agent generations, so its GitHub star count is family-level and is not attributed to one generation.

<details>
<summary><strong>Audited runtime details and limitations</strong></summary>

| Agent | Perception | Actions | Recovery evidence | Runnable path | License | Last push | Main limitation |
|---|---|---|---|---|---|---:|---|
| Mobile-Agent | screenshots, OCR, icon detection, visual grounding | ADB tap, swipe, text input, back, home | **none-documented** — The public v1 workflow executes iteratively but does not document a dedicated outcome verifier or recovery controller. | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v1/run.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | Requires several external models and exposes no dedicated error-recovery module. |
| AppAgent | screenshots, OCR, visual element descriptions | ADB tap, swipe, text input, back, home | **none-documented** — The public implementation reuses learned app documentation but does not expose a dedicated outcome-verification or recovery controller. | [entrypoint](https://github.com/TencentQQGYLab/AppAgent/blob/main/run.py) | [MIT](https://github.com/TencentQQGYLab/AppAgent/blob/main/LICENSE) | 2025-03-19 | The public repository contains the original AppAgent implementation; AppAgent v2 code is not separately identifiable. |
| Mobile-Agent-v2 | screenshots, OCR, visual grounding | ADB tap, swipe, text input, back, home | **reflection** — The Reflection Agent observes each action outcome and can request correction when an operation is judged unsuccessful. | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v2/run.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | Reflection can enter loops, and deployment still depends on several model services. |
| AutoDroid | UI hierarchy, screenshots, dynamic app exploration | ADB and DroidBot UI events | **none-documented** — The implementation emphasizes exploration memory and task generation, with no dedicated execution-error recovery module documented. | [entrypoint](https://github.com/MobileLLM/AutoDroid/blob/main/batch_testing.py) | [MIT](https://github.com/MobileLLM/AutoDroid/blob/main/LICENSE) | 2024-03-22 | The repository has seen little recent activity and requires host-side ADB rather than an on-device deployment. |
| Mobile-Agent-E | screenshots, OCR, visual grounding, action outcomes | ADB tap, swipe, text input, back, home | **reflection** — Its Action Reflector checks outcomes and updates reusable Tips and Shortcuts, while the runner supports sequential self-evolution. | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-E/scripts/run_task.sh) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | Its reflection is high-level guidance rather than explicit state rollback or guaranteed recovery. |
| Midscene.js | screenshots, optional DOM, multimodal visual grounding | ADB Android actions, WebDriverAgent iOS actions, HarmonyOS actions | **replanning** — The action loop feeds execution errors and updated screenshots back into bounded planning; no transactional device rollback is documented. | [entrypoint](https://github.com/web-infra-dev/midscene/blob/main/packages/android/src/cli.ts) | [MIT](https://github.com/web-infra-dev/midscene/blob/main/LICENSE) | 2026-07-15 | It is also a testing and automation platform, so agent behavior depends strongly on the selected multimodal model. |
| M3A | screenshots, accessibility tree | AndroidEnv tap, swipe, text input, navigation and app actions | **retry** — M3A observes the live state after every action and can issue a revised next action, but has no explicit backtracking controller. | [entrypoint](https://github.com/google-research/android_world/blob/main/minimal_task_runner.py) | [Apache-2.0](https://github.com/google-research/android_world/blob/main/LICENSE) | 2026-07-10 | It is primarily a research baseline and the default configured model is legacy and API-dependent. |
| MobileGPT | Android accessibility tree, app exploration state | Android accessibility actions | **none-documented** — Human-like app memory improves reuse, but the public system does not document a dedicated runtime recovery controller. | [entrypoint](https://github.com/mobilegptsys/MobileGPT/blob/main/Server/main.py) | [Apache-2.0](https://github.com/mobilegptsys/MobileGPT/blob/main/LICENSE) | 2024-10-02 | Setup is multi-component, the code is aging, and newly installed apps require memory reinitialization. |
| Mobilerun | accessibility tree, screenshots, device state | Android portal actions, iOS portal actions, text and gestures, app launch | **replanning** — Reasoning mode repeatedly inspects updated UI state and can revise multi-step workflows; explicit rollback semantics are not documented. | [entrypoint](https://github.com/droidrun/mobilerun/blob/main/mobilerun/cli/main.py) | [MIT](https://github.com/droidrun/mobilerun/blob/main/LICENSE) | 2026-07-06 | Published benchmark results are maintained by the project, and recovery is implemented as iterative reasoning rather than audited state restoration. |
| MobileUse | screenshots, multimodal model observations, repeated-state signals | ADB tap, swipe, text input, app launch, navigation keys | **replanning** — Action, trajectory, and global reflection operate at different temporal scales, with retries and revised execution after detected failures. | [entrypoint](https://github.com/MadeAgents/mobile-use/blob/master/pyproject.toml) | [MIT](https://github.com/MadeAgents/mobile-use/blob/master/LICENSE) | 2026-07-10 | Strong reported results use large external VLMs, and no common dedicated recovery benchmark is used. |
| App Use | Appium UI tree, screenshots, app state | Appium tap, swipe, text input, mobile gestures | **retry** — The agent loop can act again from refreshed Appium state and records execution history, but no explicit backtracking mechanism is documented. | [entrypoint](https://github.com/erickjtorres/app-use/blob/main/examples/android_app_example.py) | [MIT](https://github.com/erickjtorres/app-use/blob/main/LICENSE) | 2026-07-10 | It has no paper or standardized benchmark, and reliability inherits Appium and model constraints. |
| CHOP | screenshots, Aria-UI grounding, task context | ADB tap, swipe, text input, navigation keys | **replanning** — Constrained subtask planning can revise execution at subtask boundaries, but the paper does not present explicit state rollback. | [entrypoint](https://github.com/Yuqi-Zhou/CHOP/blob/main/src/run.py) | [MIT](https://github.com/Yuqi-Zhou/CHOP/blob/main/LICENSE) | 2025-03-08 | Evaluation is small, some Chinese task data is unreleased, and the repository is no longer active. |
| TopoClaw | mobile screenshots, desktop observations, proactive sensor events | Android client GUI actions, cross-device tools, desktop tools | **replanning** — The core agent loop and skills can re-evaluate tasks across devices, but no dedicated mobile recovery benchmark or rollback contract is documented. | [entrypoint](https://github.com/MadeAgents/TopoClaw/blob/main/TopoClaw/topoclaw/service/runtime.py) | [Apache-2.0](https://github.com/MadeAgents/TopoClaw/blob/main/LICENSE) | 2026-05-12 | Deployment is multi-component, iOS is only planned, and no standardized mobile benchmark is reported. |
| Ghost in the Droid | screenshots, ADB UI hierarchy, live device stream | ADB tap, swipe, text input, app launch, device controls | **retry** — Skills and agent chat can retry device actions and re-read state, while no general semantic backtracking controller is documented. | [entrypoint](https://github.com/ghost-in-the-droid/android-agent/blob/main/run.py) | [MIT](https://github.com/ghost-in-the-droid/android-agent/blob/main/LICENSE) | 2026-07-11 | Many workflows are skill-driven automation, and general-agent quality is not backed by an academic mobile benchmark. |
| AppClaw | screenshots, device UI observations | tap, type, swipe, mobile test actions | **retry** — The runtime can continue from updated observations after action failures, but no explicit backtracking mechanism is documented. | [entrypoint](https://github.com/appclawhq/AppClaw/blob/main/packages/agent/src/cli.ts) | [Apache-2.0](https://github.com/appclawhq/AppClaw/blob/main/LICENSE) | 2026-07-13 | The project is young, has no scholarly paper, and lacks independent benchmark evidence. |
| Mobile-Agent-v3.5 | screenshots, GUI-Owl-1.5 grounding, action history | ADB mobile actions, browser actions, desktop actions | **reflection** — Thinking variants and the Mobile-Agent controller support planning and reflection; no explicit state rollback guarantee is documented. | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3.5/mobile_use/run_gui_owl_1_5_for_mobile.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | The released phone runner is ADB-based Android code; other platform claims should not be read as a released iOS controller. |
| Open-AutoGLM Phone Agent | screenshots, vision-language model observations | ADB Android actions, HDC HarmonyOS actions, WebDriverAgent iOS actions | **retry** — The runner handles failed actions and human takeover cases, but the public documentation does not claim explicit long-range recovery. | [entrypoint](https://github.com/zai-org/Open-AutoGLM/blob/main/main.py) | [Apache-2.0](https://github.com/zai-org/Open-AutoGLM/blob/main/LICENSE) | 2026-03-06 | The current code repository appeared well after the paper and strongest operation quality depends on model availability. |
| AgenticX-GUIAgent | screenshots, UI state, multimodal model observations | ADB basic actions, smart GUI tools | **reflection** — A dedicated ActionReflectorAgent evaluates execution outcomes and coordinates revised actions through the multi-agent workflow. | [entrypoint](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/main.py) | [MIT](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/LICENSE) | 2026-01-15 | It is a small emerging project without a paper, independent benchmark, or long maintenance history. |
| Mobile-Agent-v3 | screenshots, native GUI-Owl grounding, action history | ADB tap, swipe, text input, back, home | **reflection** — The framework documents reflection and progress-management agents, but not transactional rollback to a prior device state. | [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py) | [MIT](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE) | 2026-07-07 | Running the strongest configurations requires large GUI-Owl models and substantial serving infrastructure. |
| mobile-use | screenshots, accessibility metadata, agent observations | ADB Android actions, iOS IDB actions | **replanning** — The framework decomposes goals among agents and can revise the next subtask from updated device observations; it does not claim state rollback. | [entrypoint](https://github.com/minitap-ai/mobile-use/blob/main/minitap/mobile_use/main.py) | [Apache-2.0](https://github.com/minitap-ai/mobile-use/blob/main/LICENSE) | 2026-07-09 | The 100 percent AndroidWorld claim is self-reported on the project benchmark page and is not an independent recovery evaluation. |

</details>

## Notable / code pending

These papers are directly relevant and high quality, but are not ranked or counted as open-source agents until an official implementation is publicly verifiable.

| Work | Venue | Status | Why it is pending |
|---|---|---|---|
| [BacktrackAgent](https://aclanthology.org/2025.emnlp-main.212/) | EMNLP 2025 | code-pending | Explicit outcome-conditioned error detection and backtracking, but no official public implementation was found at the audit date. |
| [Agent-SAMA](https://ojs.aaai.org/index.php/AAAI/article/view/40187) | AAAI 2026 | code-pending | Strong mobile stable-state restoration results, but no official public code repository was found. |
| [VeriGUI](https://aclanthology.org/2026.acl-long.1335/) | ACL 2026 | code-pending | Direct action-effect verification and failure-recovery training, with no official released implementation found. |
| [MobileExplorer](https://arxiv.org/abs/2605.26546) | arXiv 2026 | code-announced | Uses two-level UI rollback for speculative parallel exploration; the paper says code will be released after publication. |
| [D-Artemis](https://aclanthology.org/2026.findings-acl.681/) | Findings of ACL 2026 | public-repository-pending | A mobile GUI agent with recovery-oriented execution evidence, but no durable official public repository was verified. |

## Public repositories pending qualification

Public code alone is not enough. These projects remain outside the main list until licensing, implementation identity, or runtime completeness is resolved.

| Project | Status | Reason |
|---|---|---|
| [AppAgent v2](https://github.com/TencentQQGYLab/AppAgent) | implementation-not-identifiable | The linked repository exposes the original AppAgent runner, with no v2 branch, tag, or separately identifiable v2 entrypoint. |
| [CoCo-Agent](https://github.com/xbmxb/CoCo-Agent) | license-pending | Runnable research code is public, but the root repository has no explicit software license. |
| [MobA](https://github.com/OpenDFM/MobA) | license-pending | The official repository has code and requirements but no explicit root license. |
| [AppAgentX](https://github.com/Westlake-AGI-Lab/AppAgentX) | license-pending | The official repository is runnable, but only a nested third-party component carries a visible license. |
| [InfiGUIAgent](https://github.com/InfiXAI/InfiGUIAgent) | implementation-pending | The official repository currently contains a README and images, not the claimed agent implementation. |
| [UI-Venus](https://github.com/inclusionAI/UI-Venus) | license-pending | Agent and model code is present, but no explicit root software license was verified. |
| [OMG-Agent](https://github.com/Safphere/OMG-Agent) | source-available | Its Apache-plus-Commons-Clause terms add commercial and modification restrictions and are not treated as an OSI open-source license. |
| [OpenGUI](https://github.com/Core-Mate/OpenGUI) | source-available | The repository uses BUSL-1.1 and does not convert to an open-source license until 2030. |

## Associated resources

Useful models, training methods, datasets, and environments are kept visible but are **not counted as main agent entries**.

| Resource | Category | Scope note |
|---|---|---|
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | Agent model and training | Open model inference, RFT, and offline evaluation code; no verified live device-control loop, so it is not counted as a complete agent. |
| [Auto-UI](https://github.com/cooelf/Auto-GUI) | Agent model and training | Training and offline inference for multimodal chain-of-action prediction, not a released live mobile controller. |
| [UI-S1](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1) | Training method | Semi-online reinforcement learning, dataset, and model resources; not a separate runtime agent entry. |
| [MobileGym](https://github.com/Purewhiter/mobilegym) | Environment and benchmark | A browser-hosted Android simulation and evaluation environment for agent research. |
| [AndroidWorld](https://github.com/google-research/android_world) | Environment and benchmark | A live Android benchmark and environment; only its runnable M3A baseline is counted in the main agent catalog. |

## Snapshot and audit semantics

- **Citations:** OpenAlex only. When a preprint and published version are separate OpenAlex works, the snapshot counts the union of unique works citing either identity.
- **Stars:** official GitHub repository stargazer count at retrieval time. Shared monorepositories are marked family-level.
- **links-verified:** official repository, license, paper, evidence, and runnable paths were checked.
- **code-inspected:** the above plus implementation-level inspection of the relevant agent loop.
- **install-smoke-tested:** the documented installation and a minimal launch were executed successfully.
- A missing paper is shown as an em dash and contributes zero citations only when computing the established-table ordering.

Every historical snapshot is preserved under [snapshots/](snapshots/).

## Reproduce locally

~~~bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
python scripts/catalog.py validate
python scripts/catalog.py check
~~~

To capture a new live snapshot and regenerate both languages:

~~~bash
GITHUB_TOKEN=... python scripts/catalog.py refresh --date YYYY-MM-DD
python scripts/catalog.py render
python scripts/catalog.py validate
pytest
~~~

The monthly GitHub Actions workflow opens a refresh pull request; a human reviews and merges it.

## Related catalogs

- [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents) is a broad, paper-oriented GUI Agent reading list.
- [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) provides broad structured coverage and a companion website.

They are valuable discovery sources. This repository has a different unit of inclusion: high-quality open-source **mobile runtime agents**, with dated citation and GitHub snapshots. Candidate links seeded from other lists are independently re-verified here.

## Contributing

New-agent suggestions start as an issue, not an unsolicited catalog pull request. This keeps inclusion judgments explicit and auditable. Metadata corrections and tooling fixes are welcome after the corresponding issue is accepted. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licenses

Catalog data, documentation, and generated READMEs are licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Scripts and tests are licensed under [MIT](LICENSES/MIT.txt). Upstream projects retain their own licenses.
