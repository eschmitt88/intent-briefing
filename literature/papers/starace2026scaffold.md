---
kind: paper
title: "Scaffold Effects on GAIA: A Controlled Comparison"
authors: ["Jason Starace"]
institutions: ["Independent Researcher"]
year: 2026
venue: "arXiv preprint (cs.AI), v1 2026-06-07; pre-registered on OSF (doi:10.17605/OSF.IO/SP576)"
peer_reviewed: false
url: "https://arxiv.org/abs/2606.08529"
code_url: "https://anonymous.4open.science/r/gaia-scaffold-comparison-ECBF/"
citations: null
source: "raw/papers/starace2026scaffold.pdf"
added: "2026-11-14"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/durable-structure]]", "[[concepts/cross-model-prompt-transfer]]"]
tags: [scaffolding, gaia, pre-registered, react, planner-executor, multi-agent, elicitation-gap, counter-evidence]
---

# Scaffold Effects on GAIA: A Controlled Comparison

## TL;DR

This is a pre-registered study: 3 scaffolds × 5 models on GAIA validation
Levels 1–2, with 3 attempts per question, scored by the official
exact-match scorer. The scaffolds are ReAct, Planner-Actor-Rater (PAR) and
planner-then-executor. The models are Opus 4.7, Sonnet 4.6, Haiku 4.5,
Gemini 3.1 Pro Preview and GPT-5.5. Scaffold choice moves accuracy by up to
28 points within one model. The pre-registered prediction that stronger
models are less scaffold-sensitive is rejected in direction. **But the
headline "strongest model gained most" holds under narrow conditions:**
inside the Anthropic family only, at Level 2 only, on the "robust" slice
only, with reasoning disabled for every model. Across providers, the
highest-baseline model (GPT-5.5) gained least.

## Claims

- H1 supported: scaffold variation gives a ≥10-point best-minus-worst gap
  for at least one model (Haiku clears it at L1 in all slices).
- H2 ("frontier models show smaller gaps") rejected in direction. The
  scaffold × model interaction is significant in every slice: LRT χ²(8) =
  82.95 / 122.18 / 81.38 for primary / robust / intersection, p < 1e-4. With
  Opus as reference, most non-Opus interactions are negative under the
  robust slice.
- H3 (multi-agent > ReAct at L2) holds within Anthropic but not for Gemini
  or GPT-5.5. The author concludes that "model family rather than capability
  tier [is] the conditioning variable".
- H4 (planner-executor helps on file tasks) falsified.
- Structured scaffolds make far fewer tool calls and recover more often from
  mid-trajectory tool errors at L2.

## Methods

- GAIA validation: 53 L1 and 86 L2 questions. 3 attempts per question gives
  159 / 258 attempt-units per cell. Designed 6,255 runs, of which 5,907
  completed. Implemented in Inspect AI with the official GAIA scorer. "No
  model-graded scoring is used."
- S1 is the unmodified `inspect_evals` ReAct solver, with web_browser, bash
  and python. S2 (PAR) and S3 (planner→executor) have the same tools as each
  other (web_search, bash, python, text_editor) and short role prompts
  (Appendix C).
- Three slices. *Primary* counts errored units as wrong. *Robust* drops
  units flagged with an Anthropic API/SDK `web_fetch` deserialization bug
  (314 records, all on Anthropic s2/s3). *Intersection* keeps only questions
  completed by every cell.
- Statistics: sample-clustered bootstrap CIs (5,000 resamples) and a GLMM
  with a scaffold × model interaction (lme4).
- **Deviations from the pre-registration** (disclosed in §3.6). Reasoning
  mode was pre-registered ON but ran OFF for all models. S1's tool surface
  differs from S2/S3. Input truncation was added mid-run. The held-out test
  submission was not executed. 15 of 30 cells are partial, all of them
  Anthropic.

## Results

Accuracy (primary slice, from Table 2):

| L2 | s1 ReAct | s2 PAR | s3 plan→exec | gap (primary) [95% CI] | gap (robust) |
|---|---|---|---|---|---|
| Haiku 4.5 | 0.314 | 0.426 | 0.225 | 0.202 [0.120, 0.287] (s2−s3) | 0.262 |
| Sonnet 4.6 | 0.523 | 0.620 | 0.597 | 0.097 [0.023, 0.198] | 0.221 |
| Opus 4.7 | 0.558 | 0.698 | 0.655 | 0.140 [0.066, 0.221] | **0.279 [0.213, 0.357]** |
| Gemini 3.1 Pro | 0.694 | 0.752 | **0.860** | 0.167 [0.097, 0.240] | 0.167 |
| GPT-5.5 | **0.764** | 0.779 | 0.822 | 0.058 [0.019, 0.132] | 0.058 |

- L1 primary gaps: Haiku 0.233, Opus 0.126, Sonnet 0.069, Gemini 0.057,
  GPT-5.5 0.038. At L1, **ReAct is Opus's best scaffold** (0.830 vs 0.761 /
  0.704). Under the robust slice the L1 Anthropic ladder becomes monotonic in
  H2's predicted direction (0.25 / 0.13 / 0.03).
- The 28-point headline is Opus L2, **robust slice**: s2 0.849 (accuracy on
  completed units) vs s1 0.56. Under the primary slice it is 14 points.
- PAR minus ReAct at L2 (H3), primary: Haiku +0.112, Opus +0.140 (CIs above
  0). Sonnet +0.097, Gemini +0.058 and GPT-5.5 +0.016 have CIs spanning 0.
  Robust: Haiku +0.193, Sonnet +0.221, Opus +0.279.
- The clean structural contrast s2 vs s3 (same tools) is not significant for
  any Anthropic model at L2. Opus L2: +0.043 [−0.016, 0.105].
- Behavior at L2, averaged over models: mean tool calls 22.0 / 8.8 / 6.4
  (s1 / s2 / s3), output tokens 4.8k / 3.1k / 2.9k, recovery-from-error rate
  0.38 / 0.57 / 0.51. These are descriptive, not tested.
- Cost: Gemini s3 is the cheapest cell at both levels and the most accurate
  at L2 (0.860, $0.23/correct).

## Critique / open questions

- **The cited cell is narrow and fragile.** "Strongest model gained most"
  needs three conditions together: (a) Anthropic only; (b) L2 only (at L1,
  Opus does best with ReAct); (c) the robust slice. The robust slice drops
  errored attempts **only from s2/s3**, because S1 used a different web tool
  and never hit the bug. If the flagged web_fetch-heavy attempts were harder
  than average, dropping them inflates s2/s3 accuracy relative to s1. The
  author treats the robust slice as "the corrected reading". I'd treat the
  primary slice (14 points, CI [6.6, 22.1]) as the conservative figure. On
  the primary slice, the largest L2 gap belongs to Haiku (0.202), then Gemini
  (0.167), then Opus (0.140).
- **Across tiers, the direction partly flips.** GPT-5.5 has the highest
  ReAct baseline at L2 (0.764) and the smallest gap at both levels (0.058 and
  0.038). Gemini's gain comes from planner-executor (s3), not multi-agent.
  "Model family" and "tier" are confounded: the only within-family tier
  ladder is Anthropic, and that is also where the SDK bug sits.
- **Reasoning was disabled for every model**, against the pre-registration.
  A planner role or a written plan step may stand in for thinking that a
  current frontier deployment would have switched on. That limits transfer
  to how this project's readers actually run (thinking-enabled Opus).
- **S1 vs S2/S3 bundles loop structure with tool surface** (stateful browser
  vs search + editor), as §6 concedes. Every "structured beats ReAct"
  contrast inherits this confound. The clean contrast (s2 vs s3) shows no
  Anthropic-family difference.
- The metric is a strong point: GAIA exact match is task-outcome, with no
  LLM judge. Pre-registration plus disclosed deviations is better practice
  than most of the corpus. Remaining weaknesses: a single benchmark, the
  public validation split (contamination risk is acknowledged), a single
  author, 15 of 30 cells partial, and logs promised "on acceptance".
- **2×2 position.** None of the three scaffolds is an instruction-style
  manipulation. They are control architectures with terse role prompts
  (planner / actor / rater, or plan-then-execute). S3's plan is **written by
  the model**, not the author. So the result is about adding a separate
  planning step and a verifier role (durable structure, verification). It
  says nothing about author-written scripts vs briefs.
- **Discrepancies vs candidate summary / guide.** The numbers are accurate.
  The candidate's caveat ("single narrow cell (Opus, Level 2)… model family
  rather than tier looks like the moderator") is confirmed and understated.
  The guide's wording, "the strongest model gained the most", is true only
  for the strongest *Anthropic* model, only on the robust slice. GPT-5.5,
  arguably the strongest by baseline, gained least.

## Trust signals

- **Credibility:** 3. Pre-registered (OSF). Code and configs released
  (anonymized repo, reachable). Task-outcome metric with bootstrap CIs and a
  GLMM. Deviations disclosed. Against that: a single independent author, not
  peer reviewed, reasoning off, a tool-surface confound, an SDK bug hitting
  only the family the headline depends on, and per-attempt logs not yet
  released.

## Follow-up

- **Relevance:** 5. This is the main counter-evidence cited for Q2 and P4.
  The guide line depends on reading its cells correctly.
- **Guide:** P4 refines, and contradicts the line's current wording.
  Supported: structure that adds an explicit plan step and a verifier role
  raised task-outcome accuracy on hard GAIA tasks for 4 of 5 models (primary
  L2 gaps of 6–17 points, reasoning off). Not supported: "the strongest model
  gained the most". That holds only within Anthropic at L2 on a slice that
  favors the structured scaffolds. The highest-baseline model gained least,
  and at L1 Opus did best with plain ReAct. Suggested rewrite: "Structured
  planning/verification loops still raised accuracy on hard tasks for
  frontier models in one pre-registered study (reasoning disabled); the gain
  did not shrink reliably with capability, and varied by model family."
- **Q2:** this is evidence that the capability boundary isn't monotone in
  tier. It is not evidence that stronger readers need *more* scripting.
- Watch for the v2 / peer-reviewed version: reasoning-on rerun, released
  logs, held-out test submission.
