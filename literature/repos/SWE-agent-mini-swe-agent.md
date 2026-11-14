---
kind: repo
name: "mini-swe-agent"
url: "https://github.com/SWE-agent/mini-swe-agent"
commit: "04d809ceab9df28f9adaed044884180159172930"
source: "raw/repos/SWE-agent-mini-swe-agent.md"
source_leaderboard: "raw/web/swebench.com-bash-only.md"
added: "2026-11-14"
relevance: 4
credibility: 3
status: scanned
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/durable-structure]]", "[[concepts/degrees-of-freedom]]"]
tags: [minimal-harness, bash-only, swe-bench, leaderboard, bitter-lesson, swe-agent]
---

# mini-swe-agent

## Purpose

This is the SWE-agent team's (Princeton/Stanford) "100x simpler" coding
agent: about 100 lines of agent class, **bash as the only tool** (no
tool-calling interface required), a strictly linear message history, and
each action run as an independent `subprocess.run`. It was built after the
team concluded that, as LMs improved, "a lot of [SWE-agent's special tools
and interfaces] is not needed at all". It also serves as the fixed harness
for SWE-bench's **Bash Only** leaderboard, so models are compared "in the
same harness". MIT license, about 9.6k stars at fetch.

## Shape

- `agents/default.py` (agent loop), `environments/local.py` (and docker,
  podman, singularity and others), `models/litellm_model.py`. Configs live
  in `src/minisweagent/config/`. The README is at v2 (migration guide
  linked).
- **What the minimal harness still tells the model.**
  `config/benchmarks/swebench.yaml` (snapshotted in the raw file) has a
  one-line system prompt. The instance prompt carries: hard boundaries (do
  not modify tests or config); a 5-step **"Recommended Workflow"** (analyze,
  reproduce, edit, verify, edge cases); command-execution rules; and a
  strict, capitalized **submission protocol** (`git diff > patch.txt`,
  verify, then an exact echo sentinel command). There is a step limit of 250
  and a $3 cost limit. Minimal *scaffold code* does not mean minimal
  *instructions*. It keeps a terse checklist plus hard output invariants.

## Useful bits

- **SWE-bench Verified, Bash Only view** (agent = mini-SWE-agent; 47 rows of
  180; extracted 2026-11-14; the old `bash-only.html` URL is now 404 and the
  view is a preset on swebench.com). Selected rows, % resolved:
  - Claude 4.5 Opus (high, v2.0.0) **76.8**. Gemini 3 Flash (high) 75.8.
    MiniMax M2.5 (high, open weights) 75.8. Claude 4.6 Opus 75.6. Claude
    4.5 Opus (medium, v1.16) 74.4. Gemini 3 Pro Preview 74.2.
  - GLM 5 72.8. GPT 5.2 (high) 72.8. GPT 5.2 Codex 72.8. Claude 4.5 Sonnet
    (high) 71.4. Kimi K2.5 70.8. DeepSeek V3.2 70.0. Gemini 3 Pro (high)
    69.6. Claude 4 Opus 67.6. Claude 4.5 Haiku 66.6. GPT 5 (medium) 65.0.
    Claude 4 Sonnet 64.9.
  - Older and smaller: o3 58.4, Claude 3.7 Sonnet 52.8, GPT 4.1 39.6, GPT 4o
    21.6, Llama 4 Scout 9.1, Qwen2.5-Coder 32B 9.0.
  - The ">74%" in the README matches the Claude 4.5 Opus and Gemini 3 Pro
    rows (74.4 / 74.2 on v1.x) and is exceeded by 76.8 on v2. The newest row
    is dated 2026-02-26. Later models (Opus 4.7, GPT-5.5/5.6) are absent.
- **SWE-bench Multilingual, Bash Only** (13 rows): Gemini 3 Flash 72.7,
  Claude 4.6 Opus 72.0, Claude 4.5 Opus 70.7, GLM 5 69.7 … GPT 5 mini 39.7.
- **Same model, minimal vs custom scaffold.** This is my arithmetic from the
  same JSON, using only single-attempt custom entries. Those entries are
  unverified submissions on different dates, so treat this as indicative
  only:
  - Claude 4 Sonnet: 64.9 mini vs 74.8 (Harness AI), a gap of about 10.
  - GPT-5: 65.0 vs 71.8 (OpenHands, checked), about 7.
  - Claude 4 Opus: 67.6 vs 73.2 ("Tools"), about 6.
  - Claude 4.5 Sonnet: 71.4 vs 74.8 (Sonar), about 3.
  - Gemini 3 Pro Preview: 74.2 vs 77.4 (live-SWE-agent), about 3.
  - Claude 4.5 Opus: 76.8 vs 79.2 (Sonar / live-SWE-agent), about 2.

  The advantage of elaborate custom scaffolds over a bash-only loop appears
  to **shrink across model generations**, from about 10 to about 2–3 points.
  It never reaches zero.

## Critique

- These are leaderboard rows, not a controlled study. Per-model rows mix
  mini versions (v0.0.0 to v2.0.0) and reasoning-effort settings. The custom
  scaffolds are self-reported, mostly `checked=False`, and possibly tuned and
  selected. But the metric is task outcome (SWE-bench test-based resolution),
  and per-instance logs and trajectories are public (S3 links in the JSON).
- **2×2 position.** The scaffold is minimal in code and tools. The prompt is
  terse procedure plus hard invariants (boundaries and an exact submission
  protocol), not a pure intent brief. It is a good example of "keep the
  invariants explicit, drop the bespoke machinery".

## Trust signals

- **Credibility:** 3. Built by the SWE-bench and SWE-agent authors
  (Princeton/Stanford; SWE-agent is NeurIPS 2024), open source with tests,
  the leaderboard's own reference harness, public trajectories. The cited
  comparisons are leaderboard observations, not peer-reviewed controlled
  results.

## Follow-up

- **Relevance:** 4. This is the canonical minimal-harness data point, and
  the bash-only rows give a fixed-scaffold model comparison with task
  outcomes.
- **Guide:** P4 refines. A bash-only loop with a terse checklist and strict
  output invariants gets within about 2–3 points of the best custom
  scaffolds for 2025–26 frontier models, down from about 10 for
  earlier-generation models (indicative, uncontrolled). Bespoke tools and
  interfaces were absorbed. Hard invariants such as the submission protocol
  stayed.
- **Guide:** P3 supports, weakly. The parts the authors kept explicit and
  strict are the output contract and the boundaries.
- Used as the fixed target harness in ye2026harnesszero.
