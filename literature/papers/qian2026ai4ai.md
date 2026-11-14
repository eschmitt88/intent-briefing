---
kind: paper
title: "AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses"
authors: ["Cheng Qian", "Wenting Zhao", "Liangwei Yang", "Heng Wang", "Jielin Qiu", "Heng Ji", "Silvio Savarese", "Huan Wang", "Shelby Heinecke"]
institutions: ["Salesforce AI Research", "University of Illinois Urbana-Champaign"]
year: 2026
venue: "arXiv preprint (cs.LG), v1 2026-08-12"
peer_reviewed: false
url: "https://arxiv.org/abs/2608.12307"
code_url: null
citations: null
source: "raw/papers/qian2026ai4ai.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/llm-authored-instructions]]", "[[concepts/invariants-in-code]]", "[[concepts/degrees-of-freedom]]", "[[concepts/scaffold-absorption]]"]
tags: [strong-to-weak, harness-building, theory-of-mind, deterministic-offloading, format-enforcement, headroom]
---

# AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

## TL;DR

A strong "builder" model, working inside a coding agent (Cursor, Claude Code
or Codex), writes an inference-time harness for a fixed weaker "target"
model. It may iterate against a 5% validation slice. The harness is then
scored on the full hidden set of four Theory-of-Mind QA benchmarks (3,900
items). **0.49 → 0.91 is the single best run** (GPT-5.5 builder on Codex,
target GPT-5.4-mini). The mean over all 57 runs is 0.763 (+0.275). The gains
come mostly from moving reasoning into deterministic code, routing and
strict output formatting. The weaker target gains about 2.4× more than the
stronger one, which regresses on 9 of 20 benchmark cells.

## Claims

- Test-time strong-to-weak transfer through a harness can roughly double a
  weak model's accuracy without any weight updates.
- The mechanism is cognitive-load reduction. Accuracy correlates with the
  share of items answered entirely by code or rules (r = 0.72). It is not
  driven by more reasoning or sampling.
- Uplift follows a "headroom law" (r = 0.75 against 1 − baseline). On an
  already-strong target, scaffolding can backfire.
- Builder capability and reasoning effort matter more than platform.
  Validation probing count barely predicts quality (r = 0.17).

## Methods

- Benchmarks: BigToM (1,200), Hi-ToM (1,200), MMToM-QA (600), MuMA-ToM
  (900), text format only. The metric is the macro-average of per-benchmark
  accuracy, i.e. a task-outcome metric against gold labels with no judge.
- 11 builder configurations (Opus 4.7 at four efforts, Sonnet 4.6, GPT-5.5,
  GPT-5.4-mini, Codex-5.3, Gemini 3.1 Pro, Gemini 3.5 Flash, Grok-0.1), each
  on 1–3 platforms with 3 repeats. 72 runs in total, 57 of them with target
  GPT-5.4-mini. A second target, Gemini 3.5 Flash, was tested with 5
  builders on Cursor.
- Baselines: vanilla direct call (GPT-5.4-mini 0.488; Gemini 3.5 Flash
  0.761) and a human-designed ToM harness, UserHarness (0.939 / 0.941).
- Builders get a rule file, a demo of how to call the target, and the
  labelled validation slice. They were "explicitly asked to reduce the
  target model's cognitive load".

## Results

- Best run 0.912. The mean over 57 GPT-5.4-mini-target runs is 0.763. 100%
  of runs beat baseline. The best scaffold stays below the human UserHarness
  (0.939) except on BigToM (1.00 vs 0.95).
- Per-benchmark for the best scaffold: BigToM 1.00, Hi-ToM 0.80, MMToM 0.84,
  MuMA 0.88. On BigToM, scaffolds largely *compile the benchmark into rules*
  (determinism ≈ 0.94). The authors call this exploiting an explicit
  shortcut.
- Target dependence (Cursor, 5 builders): GPT-5.4-mini +0.262 (0.488 →
  0.750) vs Gemini 3.5 Flash +0.110 (0.761 → 0.871). For Gemini, 96% of the
  uplift is on BigToM. Gemini regresses on 9/20 builder×benchmark cases
  (Hi-ToM −0.04, MuMA −0.02 on average). GPT-5.4-mini regresses on 0/20.
- Builders adapt to the stronger target, using less deterministic code. The
  model-only share on MuMA rose from 40% to 73%.
- Self-scaffolding (GPT-5.4-mini building for itself) gives +0.17 to +0.22,
  against up to +0.31 for stronger builders. Prompt-only scaffolds are "more
  stable, but… smaller gains".
- Opus 4.7 builder effort sweep: 0.711 / 0.793 / 0.807 / 0.856 from low to
  x-high (Spearman ρ = 0.77). Scaffold size grows from ~510–650 to
  ~1,000–1,300 lines.
- Best scaffold vs baseline, McNemar: 1,717 items fixed vs 105 broken.

## Critique / open questions

- **Not an agentic task.** These are static multiple-choice/QA ToM items. The
  "harness" is a classifier pipeline (routing, parsing, rules, a forced-CoT
  prompt), not a multi-turn tool-using agent. Transfer to briefing agentic
  readers is indirect.
- **Benchmark compilability inflates the effect.** Much of the gain on
  BigToM, and nearly all of the strong target's gain, comes from encoding
  benchmark regularities as rules. That is overfitting to task structure, not
  transferable competence, even though the 5% validation → full-set
  optimism gap is small (mean 0.021). Validation and test come from the same
  distribution, so a small gap doesn't rule out benchmark-specific shortcuts.
- **The headline number is a max over 57 runs.** The fair headline is the
  mean, +0.275. The 0.91 figure is the best run.
- **"Weaker targets gain most" rests on two targets.** It is better read
  through the headroom law (r = 0.75 across builder×benchmark points) than as
  a capability-tier result. The finding that a near-ceiling target regresses
  in 9/20 cells is the more useful signal for this project: structure added
  for a reader who doesn't need it does harm.
- **2×2 position.** The scaffolds are mostly code. Where they are prose, it
  is terse procedure (forced CoT, format rules) aimed at a *weaker* reader.
  This is the expected flip side of the thesis (Q2): scripts and code win
  when the reader is weaker than the author. It also bears on Q5, because the
  author is an LLM. Strong builders calibrated the amount of structure to
  the reader, using less code for the stronger target. That is mild evidence
  *against* blanket over-scripting by LLM authors when they get feedback
  from the reader.
- No code or harness artifacts are linked in the paper. Single benchmark
  family. Not peer reviewed.
- **Discrepancy vs candidate summary:** "average accuracy… rose from 0.49 to
  0.91" is the best single run, not the average. The average scaffolded
  result is 0.763. "Weaker targets gained most" is verified, but the
  comparison is n = 2 targets, Cursor only.

## Trust signals

- **Credibility:** 3. Salesforce AI Research and UIUC, 72 runs with
  repeats, gold-label task-outcome metric, McNemar test, honest reporting of
  the shortcut on BigToM and of regressions on the strong target. Not peer
  reviewed, no code release found, non-agentic QA benchmarks with exploitable
  structure, and the headline quoted as a max.

## Follow-up

- **Relevance:** 3. Cite-worthy prior art for the weak-reader end of Q2 and
  for LLM authors writing structure (Q5). It is not about strong readers on
  agentic tasks.
- **Guide:** P3 supports. Offloading deterministic sub-decisions and output
  format into code was the main lever (determinism r = 0.72 with accuracy).
- **Guide:** P1 supports at the boundary. Heavy structure pays for weak
  readers and harmed a near-ceiling reader in 9/20 cells, which fits "brief,
  don't script, for what the reader can work out".
- Compare with ye2026harnesszero, which distils a harness into weights
  instead of keeping it at test time.
