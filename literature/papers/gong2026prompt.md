---
kind: paper
title: "Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis"
authors: ["Shuzhi Gong", "Hechuan Wen"]
institutions: ["The University of Melbourne", "The University of Queensland"]
year: 2026
venue: "arXiv preprint (2605.26655)"
peer_reviewed: false
url: "https://arxiv.org/abs/2605.26655"
code_url: null
citations: 1
source: "raw/papers/gong2026prompt.pdf"
added: "2026-11-14"
relevance: 3
credibility: 1
status: read
related_experiments: []
related_concepts: ["[[concepts/cross-model-prompt-transfer]]", "[[concepts/llm-authored-instructions]]", "[[concepts/instruction-density-decay]]"]
tags: [prompt-optimization, observational, edit-analysis, meta-instructions, dspy, textgrad, gepa]
---

# Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis

## TL;DR

An observational, IPTW-adjusted analysis of consecutive prompt edits from real
optimizer runs (2,095 DSPy/MIPROv2 pairs in the main analysis, plus 17,708
TextGrad/GEPA pairs used for direction only). The effect of an edit type
depends on the **task group**. Four associations survive FDR correction:
- inserted **meta-instructions** ("make sure to", "ensure", "do not",
  "remember to"): −0.103 accuracy on math;
- **clarity constraints** ("concisely", "briefly", "avoid"): −0.083 on logical
  tasks;
- **extraneous load**: −0.060 on sequential tasks;
- **metacognition**: +0.062 on sequential tasks.

Despite the abstract, the paper **does not analyze transfer across
backbones**. Backbone is pooled as a covariate.

## Claims

- Optimizer failures come from systematic interactions between edit families
  and task characteristics, not from random noise.
- Complexity-increasing and meta-instructional edits hurt math and multi-hop
  reasoning. Step-by-step and metacognitive edits help logical and sequential
  tasks.
- These patterns are robust across representations (GPT-4o annotations,
  surface text statistics, regex edit motifs) and "can generalize across
  optimization frameworks".

## Methods

- Logs: 3 optimizers (DSPy MIPROv2, TextGrad, GEPA). 5 backbones (GPT-5.2,
  GPT-4o, Qwen3-32B, DeepSeek-V3, DeepSeek-R1). 11 benchmarks in 5 groups:
  commonsense, math (GSM8K, MultiArith; mean base accuracy 0.97), logical,
  sequential, multi-hop.
- Unit: a consecutive edit p1→p2, with Δacc on a fixed eval set.
- Features, three views:
  - 12 cognitive-load features scored 1–10 by GPT-4o. Construct validity is
    partial: 7 of 19 expected correlations hold.
  - 14 deterministic surface features.
  - 4 regex edit motifs.
- Estimator: stabilized IPTW with propensity on pre-edit state (length, demos,
  headroom, framework, backbone, dataset, step). Weights capped at 10.
  Block-bootstrap SEs (500 resamples, dataset × backbone blocks). BH-FDR across
  60 feature×group tests and 15 motif×group tests.
- Robustness: leave-one-dataset-out sign stability, and directional replication
  on TextGrad/GEPA (surface features only, without the full IPTW protocol).

## Results

- Feature analysis: 11 of 60 tests are significant uncorrected and 2 survive
  BH. Extraneous_load×sequential −0.060. Metacognition×sequential +0.062.
- Motif analysis (15 tests), 2 survive BH:
  - meta_instruction×math −0.103. This is concentrated in MultiArith (naive
    −0.277, n = 64) vs GSM8K (−0.019, n = 14).
  - clarity_constraint×logical −0.083. Telling the model to "be concise" may
    suppress reasoning on boolean and coin-flip tasks.
- Exploratory only: meta_instruction×multi-hop −0.044. Chain-of-thought motif:
  math −0.048, sequential +0.045.
- Ceiling: headroom vs Δacc ρ = 0.047 (p = 0.053). The task group adds partial
  R² 0.003 beyond headroom. The authors say ceiling is "a minor contributor",
  but the effect sizes being explained are themselves tiny.
- Appendix C: the per-task "receptivity score" fails out of sample (LOO AUC
  0.26, below chance).

## Critique / open questions

- **Discrepancy vs the candidate summary:** there is **no per-backbone or
  cross-backbone transfer analysis**. Backbones are pooled and conditioned on.
  "Across backbones" in the abstract describes the data, not a finding.
  Cross-*framework* evidence is directional only, not a replication.
- **Internal inconsistencies** (these matter for citing numbers):
  - Surface word_count is +0.097 on sequential. The text says this "aligns
    with" Extraneous_load, but Extraneous_load is −0.060 on sequential.
  - "Sequential" is described once as a single-dataset group (last_letters) and
    elsewhere as two datasets (last_letters, ListOps). The conclusion says all
    four findings involve "at least two benchmark datasets".
  - The LOO note for Metacognition×sequential cites a "flip in
    disambiguation_qa", which is a commonsense dataset.
  - Two renderings of Table 2 order the columns differently.
- Math sits at 0.97 base accuracy and the headline math effect rests on 64 +
  14 edits. Ceiling and small-n concerns remain despite the headroom check.
- Observational, and the authors say so: bundled edits, trajectory confounding
  (optimizers insert meta-instructions after failures).
- Outcomes are task accuracy, which is good, but features come from a GPT-4o
  judge with partial validity. Code and data are "to be released upon
  publication".
- 2×2 placement: it isn't about intent vs procedure. The relevant slice is
  that **generic emphatic directives** ("make sure to", "ensure", "do not")
  written by an LLM author are associated with losses on some task types.
  These directives sit in neither the "intent" nor the "procedure" cell
  usefully: they are exhortation without content. Step structure helps
  sequential tasks and hurts multi-hop ones, so procedure's value is
  task-dependent.

## Trust signals

- **Credibility:** 1. Two-author preprint, not peer-reviewed. No code or data
  released yet. Observational design with partially validated LLM-judge
  features, small-n concentration in the main math effect, and several
  internal inconsistencies between text and tables. 1 citation (Semantic
  Scholar, 2026-11-14).

## Follow-up

- Cited as related: "Coin Flip" (Zhang et al. 2026, ANOVA on optimizer
  success), CPO (Chen et al. 2026a, arXiv 2602.01711), TextReg (Fu et al.
  2026, arXiv 2605.21318, prompt distributional overfitting). TextReg may bear
  on transfer.
- **Relevance:** 3. Its edit taxonomy maps onto writing-guide concerns, but
  the evidence is weak and it doesn't answer the backbone-transfer question it
  was flagged for.
- **Guide:** P6 supports (weak). LLM-inserted meta-instructions and brevity
  directives are associated with accuracy losses on math and logical tasks.
- **Guide:** P1 refines (weak). Step-structured edits help sequential tasks and
  hurt multi-hop ones, so whether procedure helps depends on the task.
- Tag stays `[weak]` at most.
