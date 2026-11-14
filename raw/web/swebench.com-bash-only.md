---
source_url: https://www.swebench.com/bash-only.html
retrieved_from: https://www.swebench.com/ (embedded <script id="leaderboard-data"> JSON) and https://www.swebench.com/js/leaderboardFilters.js
fetched: 2026-11-14
title: "SWE-bench leaderboards: Bash Only (mini-SWE-agent) view"
note: >
  The requested URL https://www.swebench.com/bash-only.html returned HTTP 404 at fetch time.
  The bash-only leaderboard is now a preset on the main page. Per leaderboardFilters.js,
  "Bash Only" is defined as the Agent filter narrowed to mini-SWE-agent ("so every model ran
  in the same harness"), offered on the Verified and Multilingual boards. Rows below were
  extracted mechanically from the embedded leaderboard JSON (fields: model_display, model_org,
  reasoning_effort, mini-swe-agent_version, resolved, instance_cost, instance_calls, date,
  os_model). No values were edited. The last section lists the top-25 non-mini-SWE-agent
  Verified rows from the same JSON, for same-model scaffold comparisons.
---

# SWE-bench "Bash Only" leaderboard (snapshot 2026-11-14)

Preset definition (verbatim comment from js/leaderboardFilters.js):

> "Bash Only" is a preset rather than a mode: it means the Agent filter narrowed to
> mini-SWE-agent and nothing else selected, so every model ran in the same harness.

### Multilingual (bash-only preset: agent = mini-SWE-agent; 13 rows of 13)

| rank | model | model org | reasoning effort | mini version | % resolved | avg cost/instance (USD) | avg API calls/instance | date | open-weights model |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Gemini 3 Flash | Google DeepMind |  | 2.0.0a0 | 72.70 | 0.35 | 52.5 | 2026-02-13 | False |
| 2 | Claude 4.6 Opus | Anthropic |  | 2.0.0a0 | 72.00 | 0.66 | 28.9 | 2026-02-13 | False |
| 3 | Claude 4.5 Opus | Anthropic |  | 2.0.0a0 | 70.70 | 0.83 | 30.8 | 2026-02-13 | False |
| 4 | GLM 5 | Z.ai |  | 2.0.0a0 | 69.70 | 0.64 | 67.6 | 2026-02-13 | True |
| 5 | Gemini 3 Pro | Google DeepMind |  | 2.0.0a0 | 68.70 | 1.02 | 48.9 | 2026-02-13 | False |
| 6 | MiniMax M2.5 | Minimax |  | 2.0.0a0 | 68.30 | 0.10 | 74.2 | 2026-02-16 | True |
| 7 | Kimi K2.5 | Moonshot AI |  | 2.0.0a0 | 67.30 | 0.69 | 50.4 | 2026-02-13 | True |
| 8 | Claude 4.5 Sonnet | Anthropic |  | 2.0.0a0 | 67.00 | 0.67 | 42.5 | 2026-02-13 | False |
| 9 | GPT 5.2 | OpenAI | high | 2.0.0a0 | 66.70 | 0.54 | 40.3 | 2026-02-13 | False |
| 10 | GPT 5.2 Codex | OpenAI |  | 2.0.0 | 66.30 | 0.66 | 38.2 | 2026-02-20 | False |
| 11 | Claude 4.5 Haiku | Anthropic |  | 2.0.0a0 | 64.70 | 0.38 | 70.1 | 2026-02-13 | False |
| 12 | DeepSeek V3.2 | DeepSeek |  | 2.0.0a0 | 59.00 | 0.38 | 82.7 | 2026-02-13 | True |
| 13 | GPT 5 mini | OpenAI |  | 2.0.0a0 | 39.70 | 0.05 | 30.0 | 2026-02-13 | False |

### Verified (bash-only preset: agent = mini-SWE-agent; 47 rows of 180)

| rank | model | model org | reasoning effort | mini version | % resolved | avg cost/instance (USD) | avg API calls/instance | date | open-weights model |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Claude 4.5 Opus | Anthropic | high | 2.0.0 | 76.80 | 0.75 | 32.9 | 2026-02-17 | False |
| 2 | Gemini 3 Flash | Google DeepMind | high | 2.0.0 | 75.80 | 0.36 | 56.1 | 2026-02-17 | False |
| 3 | MiniMax M2.5 | Minimax | high | 2.0.0 | 75.80 | 0.07 | 60.5 | 2026-02-17 | True |
| 4 | Claude 4.6 Opus | Anthropic |  | 2.0.0 | 75.60 | 0.55 | 28.9 | 2026-02-17 | False |
| 5 | Claude 4.5 Opus | Anthropic | medium | 1.16.0 | 74.40 | 0.72 | 38.0 | 2025-11-24 | False |
| 6 | Gemini 3 Pro Preview | Google DeepMind |  | 1.15.0 | 74.20 | 0.46 | 40.3 | 2025-11-18 | False |
| 7 | GLM 5 | Z-AI | high | 2.0.0 | 72.80 | 0.53 | 76.2 | 2026-02-17 | True |
| 8 | GPT 5.2 | OpenAI | high | 2.0.0 | 72.80 | 0.47 | 35.0 | 2026-02-17 | False |
| 9 | GPT 5.2 Codex | OpenAI |  | 2.0.0 | 72.80 | 0.45 | 28.1 | 2026-02-19 | False |
| 10 | GPT 5.2 | OpenAI | high | 1.17.2 | 71.80 | 0.52 | 19.8 | 2025-12-11 | False |
| 11 | Claude 4.5 Sonnet | Anthropic | high | 2.0.0 | 71.40 | 0.66 | 48.3 | 2026-02-17 | False |
| 12 | Kimi K2.5 | Moonshot AI | high | 2.0.0 | 70.80 | 0.15 | 51.2 | 2026-02-17 | True |
| 13 | Claude 4.5 Sonnet | Anthropic |  | 1.13.3 | 70.60 | 0.56 | 51.0 | 2025-09-29 | False |
| 14 | DeepSeek V3.2 | DeepSeek | high | 2.0.0 | 70.00 | 0.45 | 88.5 | 2026-02-17 | True |
| 15 | Gemini 3 Pro | Google DeepMind | high | 2.0.0 | 69.60 | 0.96 | 51.3 | 2026-02-26 | False |
| 16 | GPT 5.2 | OpenAI |  | 1.17.2 | 69.00 | 0.27 | 16.3 | 2025-12-11 | False |
| 17 | Claude 4 Opus | Anthropic |  | 1.0.0 | 67.60 | 1.13 | 31.1 | 2025-08-02 | False |
| 18 | Claude 4.5 Haiku | Anthropic | high | 2.0.0 | 66.60 | 0.33 | 66.2 | 2026-02-17 | False |
| 19 | GPT 5.1 | OpenAI | medium | 1.15.0 | 66.00 | 0.31 | 21.0 | 2025-11-20 | False |
| 20 | GPT 5.1 Codex | OpenAI | medium | 1.16.0 | 66.00 | 0.59 | 23.9 | 2025-11-24 | False |
| 21 | GPT 5 | OpenAI | medium | 1.7.0 | 65.00 | 0.28 | 13.2 | 2025-08-07 | False |
| 22 | Claude 4 Sonnet | Anthropic |  | 1.0.0 | 64.93 | 0.37 | 37.2 | 2025-07-26 | False |
| 23 | Kimi K2 Thinking | Moonshot AI |  | 1.17.2 | 63.40 | 0.44 | 46.8 | 2025-12-10 | True |
| 24 | MiniMax M2 | Minimax |  | 1.17.0 | 61.00 | 0.43 | 74.1 | 2025-11-24 | True |
| 25 | DeepSeek V3.2 Reasoner | deepseek |  | 1.17.1 | 60.00 | 0.03 | 46.4 | 2025-12-01 | True |
| 26 | GPT 5 mini | OpenAI | medium | 1.7.0 | 59.80 | 0.04 | 14.5 | 2025-08-07 | False |
| 27 | o3 | OpenAI |  | 1.0.0 | 58.40 | 0.33 | 24.7 | 2025-07-26 | False |
| 28 | Devstral Small (2512) | mistral |  | 1.17.2 | 56.40 |  | 86.9 | 2025-12-09 | True |
| 29 | GPT 5 mini | OpenAI |  | 2.0.0 | 56.20 | 0.05 | 20.3 | 2026-02-17 | False |
| 30 | Qwen3-Coder 480B/A35B Instruct | Qwen |  | 1.0.0 | 55.40 | 0.25 | 64.8 | 2025-08-02 | True |
| 31 | GLM 4.6 | Z.ai |  | 1.17.1 | 55.40 | 0.10 | 49.3 | 2025-12-01 | True |
| 32 | GLM 4.5 | Z.ai |  | 1.9.1 | 54.20 | 0.30 | 40.2 | 2025-08-22 | True |
| 33 | Devstral (2512) | mistral |  | 1.17.2 | 53.80 |  | 75.1 | 2025-12-09 | True |
| 34 | Gemini 2.5 Pro | Google DeepMind |  | 1.0.0 | 53.60 | 0.29 | 20.5 | 2025-07-26 | False |
| 35 | Claude 3.7 Sonnet | Anthropic |  | 0.0.0 | 52.80 | 0.35 | 34.7 | 2025-07-20 | False |
| 36 | o4-mini | OpenAI |  | 1.0.0 | 45.00 | 0.21 | 23.3 | 2025-07-26 | False |
| 37 | Kimi K2 Instruct | Moonshot AI |  | 1.7.0 | 43.80 | 0.53 | 37.5 | 2025-08-07 | True |
| 38 | GPT 4.1 | OpenAI |  | 1.0.0 | 39.58 | 0.15 | 19.5 | 2025-07-26 | False |
| 39 | GPT 5 nano | OpenAI | medium | 1.7.0 | 34.80 | 0.04 | 39.8 | 2025-08-07 | False |
| 40 | Gemini 2.5 Flash | Google DeepMind |  | 1.0.0 | 28.73 | 0.13 | 26.6 | 2025-07-26 | False |
| 41 | gpt-oss-120b | OpenAI |  | 1.7.0 | 26.00 | 0.06 | 27.6 | 2025-08-07 | True |
| 42 | GPT 4.1 mini | OpenAI |  | 0.0.0 | 23.94 | 0.44 | 89.2 | 2025-07-20 | False |
| 43 | GPT 4o | OpenAI |  | 0.0.0 | 21.62 | 1.53 | 63.1 | 2025-07-20 | False |
| 44 | Llama 4 Maverick Instruct | Meta |  | 0.0.0 | 21.04 | 0.31 | 48.1 | 2025-07-20 | False |
| 45 | Gemini 2.0 Flash | Google DeepMind |  | 0.0.0 | 13.52 | 0.00 | 0.0 | 2025-07-26 | False |
| 46 | Llama 4 Scout Instruct | Meta |  | 0.0.0 | 9.06 | 0.12 | 29.2 | 2025-07-20 | False |
| 47 | Qwen2.5-Coder 32B Instruct | Qwen |  | 1.0.0 | 9.00 | 0.07 | 48.2 | 2025-08-03 | True |

### Verified: top 25 rows with agent != mini-SWE-agent (same JSON)

| % resolved | agent | model | date | checked | tags |
|---|---|---|---|---|---|
| 79.20 | Sonar Foundation Agent | Claude 4.5 Opus | 2025-12-05 | checked=False | tags=['Model: claude-opus-4-5', 'Org: Sonar', 'System: Attempts - 1'] |
| 79.20 | live-SWE-agent | Claude 4.5 Opus | 2025-12-15 | checked=False | tags=['Model: claude-opus-4-5-20251101', 'Org: UIUC', 'System: Attempts - 1'] |
| 78.80 | TRAE | Doubao-Seed-Code | 2025-09-28 | checked=False | tags=['Model: Doubao-Seed-Code', 'Model: Doubao-Seed-1.6', 'Org: ByteDance', 'System: Attempts - 2+'] |
| 77.40 | live-SWE-agent | Gemini 3 Pro Preview | 2025-11-20 | checked=false (See README.md for info on how to get your results verified) | tags=['Model: gemini-3-pro-preview', 'Org: UIUC', 'System: Attempts - 1'] |
| 76.80 | EPAM AI/Run Developer Agent | Claude 4 Sonnet | 2025-08-04 | checked=False | tags=['Model: claude-sonnet-4-20250514', 'Org: EPAM Systems, Inc.', 'System: Attempts - 2+'] |
| 76.80 | Atlassian Rovo Dev | Multiple | 2025-09-02 | checked=False | tags=['Model: claude-sonnet-4-20250514', 'Model: gpt-5', 'Org: Atlassian', 'System: Attempts - 2'] |
| 76.40 | ACoder | Multiple | 2025-08-19 | checked=False | tags=['Model: claude-4-sonnet', 'Model: claude-4.1-opus', 'Model: gpt-5-0807-global', 'Model: gemini-2.5-pro-06-17', 'Org: ACoder', 'System: Attempts - 2+'] |
| 75.60 | Warp | Multiple | 2025-09-01 | checked=False | tags=['Model: gpt-5', 'Model: claude-sonnet-4-20250514', 'Org: Warp', 'System: Attempts - 2+'] |
| 75.20 | TRAE | Multiple | 2025-06-12 | checked=False | tags=['Model: claude-4-sonnet-20250522', 'Model: claude-4-opus-20250522', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro-preview-06-05', 'Org: TRAE', 'System: Attempts - 2+'] |
| 74.80 | Harness AI | Claude Sonnet 4 | 2025-07-31 | checked=False | tags=['Model: claude-sonnet-4-20250514', 'Org: Harness', 'System: Attempts - 1'] |
| 74.80 | Sonar Foundation Agent | Claude 4.5 Sonnet | 2025-11-03 | checked=False | tags=['Model: claude-sonnet-4-5', 'Org: Sonar', 'System: Attempts - 1'] |
| 74.60 | Lingxi-v1.5 | Claude 4 Sonnet | 2025-07-20 | checked=False | tags=['Model: claude-4-sonnet-20250514', 'Org: Lingxi', 'System: Attempts - 1'] |
| 74.60 | JoyCode | Multiple | 2025-09-15 | checked=False | tags=['Model: claude-4-sonnet', 'Model: gpt-4.1', 'Org: JoyCode', 'System: Attempts - 1'] |
| 74.40 | Refact.ai Agent | Multiple | 2025-06-03 | checked=False | tags=['Model: claude-4-sonnet', 'Model: o4-mini', 'Org: Refact.ai', 'System: Attempts - 1'] |
| 74.40 | Prometheus-v1.2.1 | GPT-5 | 2025-10-15 | checked=False | tags=['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 2+'] |
| 73.80 | Salesforce AI Research SAGE | Multiple | 2025-11-03 | checked=False | tags=['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] |
| 73.20 | Tools | Claude 4 Opus | 2025-05-22 | checked=False | tags=['Model: claude-4-opus-20250514', 'System: Attempts - 1'] |
| 73.00 | Salesforce AI Research SAGE | Multiple | 2025-10-21 | checked=False | tags=['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] |
| 72.40 | Tools | Claude 4 Sonnet | 2025-05-22 | checked=False | tags=['Model: claude-4-sonnet-20250514', 'System: Attempts - 1'] |
| 71.80 | OpenHands | GPT-5 | 2025-08-07 | checked=True | tags=['Model: openai/gpt-5-2025-08-07', 'Org: OpenHands', 'System: Attempts - 1'] |
| 71.20 | Bloop | Claude 4 Sonnet | 2025-07-10 | checked=False | tags=['Model: claude-4-sonnet-20250514', 'Org: Bloop AI', 'System: Attempts - 1'] |
| 71.20 | Qodo Command | Multiple | 2025-07-15 | checked=False | tags=['Model: claude-sonnet-4-20250514', 'Model: gpt-4o', 'Org: Qodo', 'System: Attempts - 1'] |
| 71.20 | Prometheus-v1.2 | GPT-5 | 2025-09-29 | checked=False | tags=['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 1'] |
| 71.20 | Lingxi v1.5 | Kimi K2 | 2025-10-14 | checked=False | tags=['Model: kimi-k2-0905-preview', 'Org: Huawei', 'System: Attempts - 1'] |
| 71.00 | Warp | Multiple | 2025-06-23 | checked=False | tags=['Model: claude-sonnet-4-20250514', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro', 'Model: gpt-4.1-2025-04-14', 'Org: Warp', 'System: Attempts - 1'] |
