<div align="center">

# Awesome Mobile GUI Agents

**A manually curated collection of high-quality, open-source Mobile GUI Agents.**

Verified papers, official implementations, benchmark evidence, and transparent project metadata.

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

> Metrics snapshot: **2026-07-15** (retrieved 2026-07-15T09:34:53Z). Main catalog: **20 agents**. This file is generated from [data/agents.yaml](data/agents.yaml); do not edit the tables by hand.

## Why this list exists

Mobile GUI Agent work is split across research prototypes, model releases, automation frameworks, benchmarks, and product repositories. Large general GUI-agent lists are useful for discovery, but they do not consistently answer three practical questions: Is the implementation official and open-source? Can it operate a real or emulated mobile GUI? When were its paper citations and repository stars measured?

This catalog answers those questions with manually reviewed entries and reproducible snapshots. Each entry documents platform coverage, perception, action interfaces, planning, memory, recovery behavior, packaging, and evaluation evidence.

## Inclusion bar

A main-list entry must satisfy all of the following:

1. It is a complete agent or a meaningfully runnable agent loop, not only a model, dataset, training recipe, or benchmark.
2. It operates Android, iOS, or HarmonyOS through the graphical interface on a real device, emulator, simulator, or a faithful live environment.
3. Its official source repository is public and carries an explicit open-source software license.
4. It has a documented installation or execution path.
5. It provides mobile benchmark evidence or a concrete real-device demo.
6. Its links, runnable path, license, and metadata have an audit date.

See [METHODOLOGY.md](METHODOLOGY.md) for exclusions, audit levels, paper deduplication, and metric semantics.

## Established agents

Released on or before **2025-07-15** (at least 12 months old at the snapshot). These 12 entries are listed by release date, newest first.

| Agent | Released | Platform | Snapshot | Links |
|---|:---:|---|---:|---|
| **App Use** | 2025&#8209;05&#8209;16 | Android, iOS | Citations&nbsp;—<br>Stars&nbsp;69 | [Code](https://github.com/erickjtorres/app-use) · [iOS demos](https://github.com/erickjtorres/app-use#demos) · [Quick start](https://github.com/erickjtorres/app-use#quick-start) |
| **Mobilerun** | 2025&#8209;04&#8209;12 | Android, iOS | Citations&nbsp;—<br>Stars&nbsp;8,769 | [Code](https://github.com/droidrun/mobilerun) · [Project benchmark](https://mobilerun.ai/benchmark) · [Quick start](https://github.com/droidrun/mobilerun#quickstart) |
| **MobileUse**<br><sub>NeurIPS 2025</sub> | 2025&#8209;02&#8209;27 | Android | Citations&nbsp;0<br>Stars&nbsp;167 | [Code](https://github.com/MadeAgents/mobile-use) · [Paper](https://arxiv.org/abs/2507.16853) · [AndroidWorld and AndroidLab](https://github.com/MadeAgents/mobile-use#benchmark) · [Python API](https://github.com/MadeAgents/mobile-use#use-in-python) |
| **CHOP**<br><sub>arXiv 2025</sub> | 2025&#8209;02&#8209;12 | Android, HarmonyOS | Citations&nbsp;0<br>Stars&nbsp;8 | [Code](https://github.com/Yuqi-Zhou/CHOP) · [Paper](https://arxiv.org/abs/2503.03743) · [CHOP demo usage](https://github.com/Yuqi-Zhou/CHOP#chop-demo-usage) · [CHOP-En and CHOP-ZH](https://github.com/Yuqi-Zhou/CHOP#chop-en--chop-zh) |
| **Mobile-Agent-E**<br><sub>arXiv 2025</sub> | 2025&#8209;01&#8209;20 | Android | Citations&nbsp;3<br>Stars&nbsp;8,939<sup>family</sup> | [Code](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E) · [Paper](https://arxiv.org/abs/2501.11733) · [Mobile-Eval-E](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#mobile-eval-e-benchmark) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-E#quick-start) |
| **Midscene.js** | 2024&#8209;07&#8209;23 | Android, iOS, HarmonyOS | Citations&nbsp;—<br>Stars&nbsp;14,076 | [Code](https://github.com/web-infra-dev/midscene) · [Mobile showcases](https://midscenejs.com/showcases) · [Android guide](https://midscenejs.com/android-getting-started) · [iOS guide](https://midscenejs.com/ios-getting-started) |
| **Mobile-Agent-v2**<br><sub>NeurIPS 2024</sub> | 2024&#8209;06&#8209;03 | Android | Citations&nbsp;12<br>Stars&nbsp;8,939<sup>family</sup> | [Code](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2) · [Paper](https://arxiv.org/abs/2406.01014) · [Run guide](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2#run) · [Paper results](https://arxiv.org/abs/2406.01014) |
| **M3A**<br><sub>ICLR 2025</sub> | 2024&#8209;05&#8209;23 | Android | Citations&nbsp;1<br>Stars&nbsp;821 | [Code](https://github.com/google-research/android_world/tree/main/android_world/agents) · [Paper](https://arxiv.org/abs/2405.14573) · [AndroidWorld](https://google-research.github.io/android_world/) · [Minimal M3A runner](https://github.com/google-research/android_world#quickstart) |
| **Mobile-Agent**<br><sub>ICLR 2024 Workshop; CCL 2024 demo</sub> | 2024&#8209;01&#8209;29 | Android | Citations&nbsp;13<br>Stars&nbsp;8,939<sup>family</sup> | [Code](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1) · [Paper](https://arxiv.org/abs/2401.16158) · [Mobile-Eval](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#mobile-eval) · [Quick start](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1#quick_start) |
| **AppAgent**<br><sub>CHI 2025</sub> | 2023&#8209;12&#8209;21 | Android | Citations&nbsp;47<br>Stars&nbsp;6,812 | [Code](https://github.com/TencentQQGYLab/AppAgent) · [Paper](https://arxiv.org/abs/2312.13771) · [Deployment demo](https://github.com/TencentQQGYLab/AppAgent#demo) · [Evaluation tasks](https://github.com/TencentQQGYLab/AppAgent/blob/main/assets/testset.md) |
| **MobileGPT**<br><sub>MobiCom 2024</sub> | 2023&#8209;12&#8209;04 | Android | Citations&nbsp;17<br>Stars&nbsp;26 | [Code](https://github.com/mobilegptsys/MobileGPT) · [Paper](https://arxiv.org/abs/2312.03003) · [Server and client run guide](https://github.com/mobilegptsys/MobileGPT#run) · [Benchmark dataset](https://github.com/mobilegptsys/MobileGPT#benchmark-dataset) |
| **AutoDroid**<br><sub>MobiCom 2024</sub> | 2023&#8209;08&#8209;29 | Android | Citations&nbsp;88<br>Stars&nbsp;480 | [Code](https://github.com/MobileLLM/AutoDroid) · [Paper](https://arxiv.org/abs/2308.15272) · [Installation](https://github.com/MobileLLM/AutoDroid#how-to-install) · [Paper evaluation](https://doi.org/10.1145/3636534.3649379) |

## Emerging agents

Released after **2025-07-15**. These 8 entries are listed by release date, newest first. Citation and star counts are dated snapshot metadata.

| Agent | Released | Platform | Snapshot | Links |
|---|:---:|---|---:|---|
| **TopoClaw** | 2026&#8209;04&#8209;23 | Android | Citations&nbsp;—<br>Stars&nbsp;22 | [Code](https://github.com/MadeAgents/TopoClaw) · [Project demos](https://github.com/MadeAgents/TopoClaw#-demo) · [Developer build](https://github.com/MadeAgents/TopoClaw#developer-build--run-commands) |
| **Ghost in the Droid** | 2026&#8209;04&#8209;08 | Android | Citations&nbsp;—<br>Stars&nbsp;240 | [Code](https://github.com/ghost-in-the-droid/android-agent) · [Quick start](https://github.com/ghost-in-the-droid/android-agent#quick-start) · [MCP tools](https://github.com/ghost-in-the-droid/android-agent#mcp-server--give-any-ai-agent-an-android-body) |
| **AppClaw** | 2026&#8209;03&#8209;23 | Android, iOS | Citations&nbsp;—<br>Stars&nbsp;94 | [Code](https://github.com/appclawhq/AppClaw) · [Demo and quick start](https://github.com/appclawhq/AppClaw#quickstart) · [Agent package](https://github.com/appclawhq/AppClaw/tree/main/packages/agent) |
| **Mobile-Agent-v3.5**<br><sub>arXiv 2026</sub> | 2026&#8209;02&#8209;15 | Android | Citations&nbsp;0<br>Stars&nbsp;8,939<sup>family</sup> | [Code](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5) · [Paper](https://arxiv.org/abs/2602.16855) · [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#evaluation-on-androidworld) · [Mobile runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3.5#deploy-gui-owl-15-on-your-mobile-device) |
| **Open-AutoGLM Phone Agent**<br><sub>arXiv 2024</sub> | 2025&#8209;12&#8209;08 | Android, iOS, HarmonyOS | Citations&nbsp;1<br>Stars&nbsp;25,781 | [Code](https://github.com/zai-org/Open-AutoGLM) · [Paper](https://arxiv.org/abs/2411.00820) · [Phone Agent quick start](https://github.com/zai-org/Open-AutoGLM#快速开始) · [iOS setup](https://github.com/zai-org/Open-AutoGLM/blob/main/docs/ios_setup/ios_setup.md) |
| **AgenticX-GUIAgent** | 2025&#8209;09&#8209;16 | Android | Citations&nbsp;—<br>Stars&nbsp;11 | [Code](https://github.com/DemonDamon/AgenticX-GUIAgent) · [Run guide](https://github.com/DemonDamon/AgenticX-GUIAgent#run) · [Architecture](https://github.com/DemonDamon/AgenticX-GUIAgent#system-architecture) |
| **Mobile-Agent-v3**<br><sub>arXiv 2025</sub> | 2025&#8209;08&#8209;21 | Android | Citations&nbsp;0<br>Stars&nbsp;8,939<sup>family</sup> | [Code](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3) · [Paper](https://arxiv.org/abs/2508.15144) · [AndroidWorld runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#evaluation-on-androidworld) · [Real-device runner](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v3#deploy-mobile-agent-v3-on-your-mobile-device) |
| **mobile-use**<br><sub>arXiv 2026</sub> | 2025&#8209;08&#8209;16 | Android, iOS | Citations&nbsp;0<br>Stars&nbsp;2,680 | [Code](https://github.com/minitap-ai/mobile-use) · [Paper](https://arxiv.org/abs/2602.07787) · [AndroidWorld report](https://minitap.ai/benchmark) · [Local quick start](https://github.com/minitap-ai/mobile-use#local-quick-start) |

<sup>family</sup> The repository hosts multiple cataloged agent generations, so its GitHub star count is family-level and is not attributed to one generation.

## Agent details

<details>
<summary><strong>App Use</strong> — A compact Appium-backed Agent API for controlling real Android and iOS applications.</summary>

- **Perception:** Appium UI tree, screenshots, app state
- **Actions:** Appium tap, swipe, text input, mobile gestures
- **Capabilities:** general Agent API, Android and iOS examples, CLI setup and doctor, optional memory
- **Recovery:** <code>retry</code> — The agent loop can act again from refreshed Appium state and records execution history, but no explicit backtracking mechanism is documented.
- **Runtime:** [entrypoint](https://github.com/erickjtorres/app-use/blob/main/examples/android_app_example.py) · [MIT license](https://github.com/erickjtorres/app-use/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-10
- **Main limitation:** It has no paper or standardized benchmark, and reliability inherits Appium and model constraints.

</details>
<details>
<summary><strong>Mobilerun</strong> — A widely adopted local framework giving LLM agents native Android and iOS inspection and control tools.</summary>

- **Perception:** accessibility tree, screenshots, device state
- **Actions:** Android portal actions, iOS portal actions, text and gestures, app launch
- **Capabilities:** CLI, Python API, reasoning mode, skills, app cards, custom tools, Docker
- **Recovery:** <code>replanning</code> — Reasoning mode repeatedly inspects updated UI state and can revise multi-step workflows; explicit rollback semantics are not documented.
- **Runtime:** [entrypoint](https://github.com/droidrun/mobilerun/blob/main/mobilerun/cli/main.py) · [MIT license](https://github.com/droidrun/mobilerun/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-06
- **Main limitation:** Published benchmark results are maintained by the project, and recovery is implemented as iterative reasoning rather than audited state restoration.

</details>
<details>
<summary><strong>MobileUse</strong> — A complete Android agent with hierarchical reflection, proactive exploration, and benchmark integrations.</summary>

- **Perception:** screenshots, multimodal model observations, repeated-state signals
- **Actions:** ADB tap, swipe, text input, app launch, navigation keys
- **Capabilities:** multi-agent planning, hierarchical reflection, proactive exploration, memory, WebUI, Python API
- **Recovery:** <code>replanning</code> — Action, trajectory, and global reflection operate at different temporal scales, with retries and revised execution after detected failures.
- **Runtime:** [entrypoint](https://github.com/MadeAgents/mobile-use/blob/master/pyproject.toml) · [MIT license](https://github.com/MadeAgents/mobile-use/blob/master/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-10
- **Main limitation:** Strong reported results use large external VLMs, and no common dedicated recovery benchmark is used.

</details>
<details>
<summary><strong>CHOP</strong> — A real-device mobile assistant that constrains planning around reusable high-frequency subtasks.</summary>

- **Perception:** screenshots, Aria-UI grounding, task context
- **Actions:** ADB tap, swipe, text input, navigation keys
- **Capabilities:** basis subtasks, constrained subtask planning, bilingual tasks, real-device demo
- **Recovery:** <code>replanning</code> — Constrained subtask planning can revise execution at subtask boundaries, but the paper does not present explicit state rollback.
- **Runtime:** [entrypoint](https://github.com/Yuqi-Zhou/CHOP/blob/main/src/run.py) · [MIT license](https://github.com/Yuqi-Zhou/CHOP/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2025-03-08
- **Main limitation:** Evaluation is small, some Chinese task data is unreleased, and the repository is no longer active.

</details>
<details>
<summary><strong>Mobile-Agent-E</strong> — A self-evolving Android assistant that converts outcome reflection into reusable task experience.</summary>

- **Perception:** screenshots, OCR, visual grounding, action outcomes
- **Actions:** ADB tap, swipe, text input, back, home
- **Capabilities:** action reflection, self-evolution, tips memory, shortcut memory
- **Recovery:** <code>reflection</code> — Its Action Reflector checks outcomes and updates reusable Tips and Shortcuts, while the runner supports sequential self-evolution.
- **Runtime:** [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-E/scripts/run_task.sh) · [MIT license](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-07
- **Main limitation:** Its reflection is high-level guidance rather than explicit state rollback or guaranteed recovery.

</details>
<details>
<summary><strong>Midscene.js</strong> — A production-oriented visual automation agent spanning Android, iOS, HarmonyOS, web, and desktop.</summary>

- **Perception:** screenshots, optional DOM, multimodal visual grounding
- **Actions:** ADB Android actions, WebDriverAgent iOS actions, HarmonyOS actions
- **Capabilities:** natural-language action, querying, assertion, JavaScript SDK, YAML workflows, agent skills
- **Recovery:** <code>replanning</code> — The action loop feeds execution errors and updated screenshots back into bounded planning; no transactional device rollback is documented.
- **Runtime:** [entrypoint](https://github.com/web-infra-dev/midscene/blob/main/packages/android/src/cli.ts) · [MIT license](https://github.com/web-infra-dev/midscene/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-15
- **Main limitation:** It is also a testing and automation platform, so agent behavior depends strongly on the selected multimodal model.

</details>
<details>
<summary><strong>Mobile-Agent-v2</strong> — A multi-agent Android system separating planning, decision, reflection, and focus memory.</summary>

- **Perception:** screenshots, OCR, visual grounding
- **Actions:** ADB tap, swipe, text input, back, home
- **Capabilities:** planning agent, decision agent, reflection agent, focus memory
- **Recovery:** <code>reflection</code> — The Reflection Agent observes each action outcome and can request correction when an operation is judged unsuccessful.
- **Runtime:** [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v2/run.py) · [MIT license](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-07
- **Main limitation:** Reflection can enter loops, and deployment still depends on several model services.

</details>
<details>
<summary><strong>M3A</strong> — The runnable multimodal default agent shipped with the AndroidWorld live benchmark.</summary>

- **Perception:** screenshots, accessibility tree
- **Actions:** AndroidEnv tap, swipe, text input, navigation and app actions
- **Capabilities:** multimodal reasoning, dynamic task execution, reproducible benchmark runner
- **Recovery:** <code>retry</code> — M3A observes the live state after every action and can issue a revised next action, but has no explicit backtracking controller.
- **Runtime:** [entrypoint](https://github.com/google-research/android_world/blob/main/minimal_task_runner.py) · [Apache-2.0 license](https://github.com/google-research/android_world/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-10
- **Main limitation:** It is primarily a research baseline and the default configured model is legacy and API-dependent.

</details>
<details>
<summary><strong>Mobile-Agent</strong> — A screen-only Android agent combining OCR, icon detection, and multimodal reasoning.</summary>

- **Perception:** screenshots, OCR, icon detection, visual grounding
- **Actions:** ADB tap, swipe, text input, back, home
- **Capabilities:** screen-only operation, single-agent planning, cross-app tasks
- **Recovery:** <code>none-documented</code> — The public v1 workflow executes iteratively but does not document a dedicated outcome verifier or recovery controller.
- **Runtime:** [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v1/run.py) · [MIT license](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-07
- **Main limitation:** Requires several external models and exposes no dedicated error-recovery module.

</details>
<details>
<summary><strong>AppAgent</strong> — An Android agent that first learns app-specific interaction knowledge, then reuses it for task execution.</summary>

- **Perception:** screenshots, OCR, visual element descriptions
- **Actions:** ADB tap, swipe, text input, back, home
- **Capabilities:** autonomous app exploration, human-demonstration learning, app knowledge base, task execution
- **Recovery:** <code>none-documented</code> — The public implementation reuses learned app documentation but does not expose a dedicated outcome-verification or recovery controller.
- **Runtime:** [entrypoint](https://github.com/TencentQQGYLab/AppAgent/blob/main/run.py) · [MIT license](https://github.com/TencentQQGYLab/AppAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2025-03-19
- **Main limitation:** The public repository contains the original AppAgent implementation; AppAgent v2 code is not separately identifiable.

</details>
<details>
<summary><strong>MobileGPT</strong> — A server-plus-Android-client agent that learns reusable app procedures with human-like memory.</summary>

- **Perception:** Android accessibility tree, app exploration state
- **Actions:** Android accessibility actions
- **Capabilities:** explore-select-derive-recall memory, reusable subtasks, on-device client, Python server
- **Recovery:** <code>none-documented</code> — Human-like app memory improves reuse, but the public system does not document a dedicated runtime recovery controller.
- **Runtime:** [entrypoint](https://github.com/mobilegptsys/MobileGPT/blob/main/Server/main.py) · [Apache-2.0 license](https://github.com/mobilegptsys/MobileGPT/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2024-10-02
- **Main limitation:** Setup is multi-component, the code is aging, and newly installed apps require memory reinitialization.

</details>
<details>
<summary><strong>AutoDroid</strong> — A DroidBot-based Android task agent that combines automated exploration with app-specific LLM memory.</summary>

- **Perception:** UI hierarchy, screenshots, dynamic app exploration
- **Actions:** ADB and DroidBot UI events
- **Capabilities:** functionality-aware UI representation, app memory, query optimization, task automation
- **Recovery:** <code>none-documented</code> — The implementation emphasizes exploration memory and task generation, with no dedicated execution-error recovery module documented.
- **Runtime:** [entrypoint](https://github.com/MobileLLM/AutoDroid/blob/main/batch_testing.py) · [MIT license](https://github.com/MobileLLM/AutoDroid/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2024-03-22
- **Main limitation:** The repository has seen little recent activity and requires host-side ADB rather than an on-device deployment.

</details>
<details>
<summary><strong>TopoClaw</strong> — A newly open-sourced cross-device personal agent with an Android client, skills, and proactive execution.</summary>

- **Perception:** mobile screenshots, desktop observations, proactive sensor events
- **Actions:** Android client GUI actions, cross-device tools, desktop tools
- **Capabilities:** cross-device agent, mobile client, skills, proactive sensing, multi-user collaboration, self-hosting
- **Recovery:** <code>replanning</code> — The core agent loop and skills can re-evaluate tasks across devices, but no dedicated mobile recovery benchmark or rollback contract is documented.
- **Runtime:** [entrypoint](https://github.com/MadeAgents/TopoClaw/blob/main/TopoClaw/topoclaw/service/runtime.py) · [Apache-2.0 license](https://github.com/MadeAgents/TopoClaw/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-05-12
- **Main limitation:** Deployment is multi-component, iOS is only planned, and no standardized mobile benchmark is reported.

</details>
<details>
<summary><strong>Ghost in the Droid</strong> — An Android automation framework combining an LLM phone agent, reusable skills, MCP tools, and fleet operations.</summary>

- **Perception:** screenshots, ADB UI hierarchy, live device stream
- **Actions:** ADB tap, swipe, text input, app launch, device controls
- **Capabilities:** agent chat, reusable app skills, MCP server, phone-farm jobs, dashboard, local-model support
- **Recovery:** <code>retry</code> — Skills and agent chat can retry device actions and re-read state, while no general semantic backtracking controller is documented.
- **Runtime:** [entrypoint](https://github.com/ghost-in-the-droid/android-agent/blob/main/run.py) · [MIT license](https://github.com/ghost-in-the-droid/android-agent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-11
- **Main limitation:** Many workflows are skill-driven automation, and general-agent quality is not backed by an academic mobile benchmark.

</details>
<details>
<summary><strong>AppClaw</strong> — An emerging TypeScript mobile agent and test runner with Android and iOS support.</summary>

- **Perception:** screenshots, device UI observations
- **Actions:** tap, type, swipe, mobile test actions
- **Capabilities:** natural-language agent mode, reusable flows, test runner, CLI, GitHub Action
- **Recovery:** <code>retry</code> — The runtime can continue from updated observations after action failures, but no explicit backtracking mechanism is documented.
- **Runtime:** [entrypoint](https://github.com/appclawhq/AppClaw/blob/main/packages/agent/src/cli.ts) · [Apache-2.0 license](https://github.com/appclawhq/AppClaw/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-13
- **Main limitation:** The project is young, has no scholarly paper, and lacks independent benchmark evidence.

</details>
<details>
<summary><strong>Mobile-Agent-v3.5</strong> — The current Mobile-Agent generation built around GUI-Owl-1.5, with a released Android phone runner.</summary>

- **Perception:** screenshots, GUI-Owl-1.5 grounding, action history
- **Actions:** ADB mobile actions, browser actions, desktop actions
- **Capabilities:** multi-platform planning, reflection, long-horizon memory, tool use
- **Recovery:** <code>reflection</code> — Thinking variants and the Mobile-Agent controller support planning and reflection; no explicit state rollback guarantee is documented.
- **Runtime:** [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3.5/mobile_use/run_gui_owl_1_5_for_mobile.py) · [MIT license](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-07
- **Main limitation:** The released phone runner is ADB-based Android code; other platform claims should not be read as a released iOS controller.

</details>
<details>
<summary><strong>Open-AutoGLM Phone Agent</strong> — An official visual Phone Agent runtime for Android, iOS, and HarmonyOS built around AutoGLM.</summary>

- **Perception:** screenshots, vision-language model observations
- **Actions:** ADB Android actions, HDC HarmonyOS actions, WebDriverAgent iOS actions
- **Capabilities:** natural-language tasks, visual planning, sensitive-action confirmation, human takeover, remote device connections
- **Recovery:** <code>retry</code> — The runner handles failed actions and human takeover cases, but the public documentation does not claim explicit long-range recovery.
- **Runtime:** [entrypoint](https://github.com/zai-org/Open-AutoGLM/blob/main/main.py) · [Apache-2.0 license](https://github.com/zai-org/Open-AutoGLM/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-03-06
- **Main limitation:** The current code repository appeared well after the paper and strongest operation quality depends on model availability.

</details>
<details>
<summary><strong>AgenticX-GUIAgent</strong> — An Android multi-agent implementation with explicit manager, executor, reflector, and notetaker roles.</summary>

- **Perception:** screenshots, UI state, multimodal model observations
- **Actions:** ADB basic actions, smart GUI tools
- **Capabilities:** manager agent, executor agent, action reflector, notetaker, knowledge flywheel, evaluation framework
- **Recovery:** <code>reflection</code> — A dedicated ActionReflectorAgent evaluates execution outcomes and coordinates revised actions through the multi-agent workflow.
- **Runtime:** [entrypoint](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/main.py) · [MIT license](https://github.com/DemonDamon/AgenticX-GUIAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-01-15
- **Main limitation:** It is a small emerging project without a paper, independent benchmark, or long maintenance history.

</details>
<details>
<summary><strong>Mobile-Agent-v3</strong> — A GUI-Owl-based multi-agent framework with planning, progress tracking, reflection, and memory.</summary>

- **Perception:** screenshots, native GUI-Owl grounding, action history
- **Actions:** ADB tap, swipe, text input, back, home
- **Capabilities:** multi-agent planning, progress management, reflection, memory, end-to-end GUI model
- **Recovery:** <code>reflection</code> — The framework documents reflection and progress-management agents, but not transactional rollback to a prior device state.
- **Runtime:** [entrypoint](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py) · [MIT license](https://github.com/X-PLUG/MobileAgent/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-07
- **Main limitation:** Running the strongest configurations requires large GUI-Owl models and substantial serving infrastructure.

</details>
<details>
<summary><strong>mobile-use</strong> — A local Android and iOS agent framework centered on task decomposition and reusable skills.</summary>

- **Perception:** screenshots, accessibility metadata, agent observations
- **Actions:** ADB Android actions, iOS IDB actions
- **Capabilities:** multi-agent decomposition, local SDK, CLI, skills, Android and iOS control
- **Recovery:** <code>replanning</code> — The framework decomposes goals among agents and can revise the next subtask from updated device observations; it does not claim state rollback.
- **Runtime:** [entrypoint](https://github.com/minitap-ai/mobile-use/blob/main/minitap/mobile_use/main.py) · [Apache-2.0 license](https://github.com/minitap-ai/mobile-use/blob/main/LICENSE)
- **Audit:** links-verified on 2026-07-15 · repository updated 2026-07-09
- **Main limitation:** The 100 percent AndroidWorld claim is self-reported on the project benchmark page and is not an independent recovery evaluation.

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
- A missing paper is shown as an em dash.

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
