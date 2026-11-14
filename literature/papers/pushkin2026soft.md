---
kind: paper
title: "Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve"
authors: ["Denys Pushkin", "Albert Q. Jiang", "Aryo Lotfi", "Colin Sandon", "Emmanuel Abbé"]
institutions: ["EPFL", "Apple", "Mistral AI"]
year: 2026
venue: "arXiv preprint (v1, 2026-08-04)"
peer_reviewed: false
url: "https://arxiv.org/abs/2608.03550"
code_url: null
citations: 0
source: "raw/papers/pushkin2026soft.pdf"
added: "2026-11-14"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/guidance-distraction]]", "[[concepts/scaffold-absorption]]"]
tags: [chain-of-thought, few-shot, zero-shot, gsm8k, reasoning-models, in-context-examples]
---

# Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve

## TL;DR

The test is GSM8K with three 7–8B models from 2024. For the math-specialised
model (Mathstral), few-shot CoT with human-written dataset exemplars does
clearly worse than giving the bare problem (≤74.2% vs 83.8%). The authors
name the cause a **guidance–distraction trade-off**: exemplars demand style
adaptation and format compliance, which crowds out reasoning. For the
general-purpose Llama, exemplars still help a lot. "Let's think step by step"
adds about 2 pp for the specialised models.

## Claims

- Few-shot CoT with dataset examples "significantly hinders
  reasoning-specialized models".
  - Mathstral: best DS-CoT is 74.2% vs free-form zero-shot 83.8%. The
    official report gave 77.1%, which the authors could not reproduce.
  - Qwen2.5-7B: the text says DS-CoT reaches "no more than 83.4%" vs 88.6%.
    Table 1, however, shows DS-CoT+Prompt reaching 87.6%. That is still
    below zero-shot, but the gap is 1 pp, not 5.
- Even model-generated exemplars (Self-CoT) fail to beat zero-shot for
  Mathstral.
- Zero-shot CoT "remains effective but produces only marginal gains" for
  reasoning-optimised models.
- The authors predict that, as models improve, unconstrained free-form
  generation will overtake hand-crafted prompt phrases, by analogy with
  hand-engineered features.

## Methods

- Models: Mathstral-7B (math-tuned), Qwen2.5-7B-Instruct and
  Llama-3.1-8B-Instruct, all evaluated on the GSM8K test split.
- Prompt variants:
  - DS-CoT: random training-set exemplars, 1–16 shots, with or without
    answer-format instructions.
  - Self-CoT: model-generated exemplars, free-form or with a zero-shot-CoT
    prefix, optionally cleaned.
  - Baselines: free-form zero-shot and zero-shot CoT.
- Answer extraction is either rule-based (`#### n`) or a follow-up prompt.
  This separates formatting failures from reasoning.
- Greedy decoding. Results are averaged over 10 random exemplar draws. No
  variances or significance tests are reported.

## Results

Table 1, accuracy %:

| Model | Free-form 0-shot | 0-shot CoT | Best DS-CoT | Best Self-CoT+0shot |
|---|---|---|---|---|
| Mathstral-7B | 83.8 | 86.1 | 74.2 | 85.5 |
| Qwen2.5-7B | 88.6 | 90.9 | 87.6 (+Prompt extraction) | 91.6 |
| Llama-3.1-8B | 67.3 | 81.4 | 80.3 | 84.4 |

- Qwen's best DS-CoT (87.6) still trails zero-shot. The text's "≤83.4%"
  figure matches only the +Instr variants.
- So the strong exemplar penalty (about −10 pp) is shown for Mathstral alone.
- For Llama, exemplars help over free-form (+13 pp) and zero-shot CoT helps
  most (+14.1 pp).
- Format-compliance confound (Table 2): with rule-based extraction, Qwen
  1-shot DS-CoT scores 3.0% with 96.5% invalid answers. The apparent gain
  from adding more shots is mostly formatting compliance, not reasoning.

## Critique / open questions

- **Title overclaims.** "As LLMs improve" rests on three ~7B 2024 models
  differing in *specialisation*, not on a capability or scale series. There
  are no frontier models and no 2025–26 reasoning (RLVR) models.
- **Narrow evidence:** single benchmark (GSM8K), no CIs, and the
  abstract/text numbers are slightly inconsistent (74.1 vs 74.2).
- The main effect is large and has a clean mechanism for the specialised
  model. It agrees with Cheng et al. 2025 (2506.14641) and with 2509.23196.
- **Evaluation:** exact-match task outcome, no LLM judge. Good.
- **2×2:** few-shot worked exemplars are *verbose procedure by
  demonstration*. Free-form zero-shot is *terse intent* (just the problem).
  Zero-shot CoT is a one-line procedural nudge. The result is that verbose
  demonstrated procedure hurts readers that already have the skill, and
  helps readers that don't.

## Trust signals

- **Credibility:** 2. Strong group (EPFL / Apple, Abbé; Jiang ex-Mistral).
  Not peer reviewed, no code released. Small models, single benchmark, no
  variance reporting. Semantic Scholar showed 0 citations on 2026-11-14.

## Follow-up

- **Relevance:** 3. Cite-worthy prior art for the guidance–distraction
  mechanism and Q2. Effect shown only for small math models.
- **Guide:** P1 supports (narrowly) — worked exemplars of *how* to reason
  degrade a reader already specialised for the task. The cost comes from
  style and format adaptation, not from missing information.
- **Guide:** P4 refines — scaffolding that imposes *format* is distraction
  for a skilled reader. The same exemplars help a reader lacking the skill
  (Llama +13 pp). The line should separate format-imposing structure from
  knowledge-carrying structure.
