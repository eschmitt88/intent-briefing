---
kind: paper
title: "Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting"
authors: ["Lennart Meincke", "Ethan Mollick", "Lilach Mollick", "Dan Shapiro"]
institutions: ["Generative AI Labs, The Wharton School, University of Pennsylvania", "WHU–Otto Beisheim School of Management", "Glowforge"]
year: 2025
venue: "Technical report series (arXiv preprint v1, 2025-06-08; SSRN)"
peer_reviewed: false
url: "https://arxiv.org/abs/2506.07142"
code_url: null
citations: null
source: "raw/papers/meincke2025prompting.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/guidance-distraction]]"]
tags: [chain-of-thought, reasoning-models, gpqa, latency, prompt-sensitivity, repeated-trials]
---

# Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting

## TL;DR

The test is GPQA Diamond (198 questions, 25 trials each per condition). A
"think step by step" suffix helps non-reasoning models on average when the
alternative is "answer directly". It adds little over default behaviour,
because most models already reason unprompted. It can lower per-question
reliability. For reasoning models (o3-mini, o4-mini, Gemini 2.5 Flash) the
gain is ≤3 pp or negative, while requests take 20–80% (10–20 s) longer.

## Claims

- Non-reasoning models: CoT generally improves average accuracy a little. It
  adds variability that breaks questions the model would otherwise always get
  right. It "generally requires far more tokens (increasing cost and time)".
- Many recent models do CoT by default, so explicitly asking for it has
  little impact.
- Reasoning models: "marginal, if any, gains", with a substantial increase in
  time and tokens.
- Telling a non-reasoning model to answer only with the answer likely harms
  it.

## Methods

- GPQA Diamond, 198 MCQ. 25 trials per question per condition (4,950 runs per
  prompt per model), temperature 0, standard GPQA system prompt.
- Conditions:
  - Direct ("Answer directly without any explanation or thinking");
  - Step by step ("Think step by step");
  - Default (no suffix, no format constraint), for non-reasoning models only.
- Metrics: average over all trials, and per-question thresholds of 100%
  (25/25), 90% (≥23/25) and 51% (≥13/25). Paired bootstrap-permutation tests
  with 95% CIs (Tables S3–S5).
- Four CoT wordings were checked on GPT-4o and gave negligible differences
  (Fig. S3).

## Results

**Non-reasoning models, Step-by-step vs Direct** (risk differences, Table S3):

| Model | Average | 100% correct | 90% correct |
|---|---|---|---|
| Gemini 2.0 Flash | +0.135, p<.001 | **−0.131**, p<.001 | — |
| Sonnet 3.5 | +0.117, p<.001 | +0.101 | +0.136 |
| GPT-4o | +0.072, p=.003 | +0.010, n.s. | — |
| Gemini 1.5 Pro | +0.071, p=.014 | **−0.172**, p<.001 | −0.131 |
| GPT-4o-mini | +0.044, p=.067 | **−0.091**, p=.001 | −0.066 |

**Non-reasoning models, Step-by-step vs Default** (Table S4):

| Model | Average | Note |
|---|---|---|
| Gemini 2.0 Flash | +0.062, p<.001 | also +0.071 at 100%, +0.111 at 90% |
| GPT-4o | +0.069, p=.003 | 100% n.s. |
| Sonnet 3.5 | −0.019, n.s. | |
| GPT-4o-mini | +0.004, n.s. | |

No model changes at the 51% threshold.

**Reasoning models, Step-by-step vs Direct** (Table S5):

| Model | Average | Threshold metrics |
|---|---|---|
| o3-mini | +0.029, p=.024 | all n.s. |
| o4-mini | +0.031, p=.003 | 51%: +0.056 |
| Gemini 2.5 Flash | **−0.033**, p=.005 | 100%: −0.131, 90%: −0.071 |

**Cost:**

- Time: CoT requests took 35–600% longer (5–15 s) for non-reasoning models
  and 20–80% longer (10–20 s) for reasoning models (Figs. S1–S2).
- **Token counts are not reported numerically.** The "far more tokens" claim
  is qualitative.

## Critique / open questions

- **Discrepancy with the candidate summary:** gains and time cost are
  quantified, but token cost is not.
- **Sound design:** repeated trials and per-question reliability thresholds
  are better than single-shot accuracy. Task outcomes only, no LLM judge.
- **Limits:**
  - one MCQ benchmark;
  - a single minimal CoT phrase (plus 3 variants on one model);
  - no agentic or multi-step tool tasks;
  - reasoning models were told to "answer directly", which does not switch
    off hidden reasoning, so the "Direct" baseline differs in kind across
    model classes.
- **Models are dated** (mid-2025 small reasoning models). No frontier reasoning
  model was tested.
- **2×2:** "think step by step" is the tersest possible *procedure* nudge.
  The finding is that a generic method instruction adds ~nothing for readers
  who already apply that method, at a latency cost. Removing the method
  entirely ("answer directly") hurts non-reasoners.

## Trust signals

- **Credibility:** 3. Wharton Generative AI Labs (Mollick). A careful
  statistical design with CIs and paired tests. Not peer reviewed (report
  series). No code or data release found. Semantic Scholar was rate-limited,
  so citations were not retrieved.

## Follow-up

- **Relevance:** 3. Cite-worthy, well-measured prior art for Q2 (capability
  boundary) and scaffold absorption. Effects are small and the setting is
  non-agentic.
- **Guide:** P1 supports — telling a reasoning model *how* to think (generic
  procedure) buys ≤3 pp, sometimes −3 pp, and costs 20–80% more latency.
  Method instructions the reader already follows are dead weight.
- **Guide:** P4 refines — the reliability cost (more variance, lower
  25/25-correct rates) means even "helpful" procedural nudges can trade
  consistency for average accuracy.
