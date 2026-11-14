---
kind: paper
title: "When Instructions Multiply: Measuring and Estimating LLM Capabilities of Multiple Instructions Following"
authors: ["Keno Harada", "Yudai Yamazaki", "Masachika Taniguchi", "Edison Marrese-Taylor", "Takeshi Kojima", "Yusuke Iwasawa", "Yutaka Matsuo"]
institutions: ["The University of Tokyo", "Kyoto University", "University of the Ryukyus"]
year: 2025
venue: "Findings of EMNLP 2025 (arXiv comment: 'Accepted to EMNLP2025'; ACL Anthology 2025.findings-emnlp.896)"
peer_reviewed: true
url: "https://arxiv.org/abs/2509.21051"
code_url: "https://github.com/kenoharada/Multiple-Instructions-Following"
citations: null
source: "raw/papers/harada2025instructions.pdf"
added: "2026-11-14"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/instruction-density-decay]]", "[[concepts/requirement-coverage]]", "[[concepts/invariants-in-code]]"]
tags: [instruction-following, multi-instruction, manyifeval, stylembpp, dose-response]
---

# When Instructions Multiply: Measuring and Estimating LLM Capabilities of Multiple Instructions Following

Published version of the ICLR 2025 OpenReview submission "Curse of
Instructions: Large Language Models Cannot Follow Multiple Instructions at
Once" (OpenReview R6q67CDBCH; same first author and lab). That submission was
never on arXiv under that title.

## TL;DR

Two benchmarks hold the task fixed and vary only the number of verifiable
instructions: ManyIFEval (1–10 text instructions) and StyleMBPP (1–6 code-style
instructions). The rate of satisfying *all* instructions falls steeply with
count in all 10 models, while per-instruction accuracy stays high. A logistic
model on instruction count predicts the curve within about 0.03–0.06 MAE.

## Claims

- Prompt-level accuracy (all instructions satisfied) degrades consistently and
  steeply as instruction count rises, even for individually easy instructions.
- Reasoning models (o3-mini, DeepSeek-R1) degrade less than their
  non-reasoning counterparts. Higher o3-mini effort is best.
- In StyleMBPP, functional correctness (passing tests) stays roughly flat as
  style rules are added. Only compliance falls.
- LLM-as-judge (GPT-4o) inflates multi-instruction accuracy: at n = 10, 0.657
  judged vs 0.213 rule-based.
- Logistic regression on instruction count extrapolates to unseen counts
  (trained on n ≤ 9, predicting n = 10: MAE 0.03 ± 0.04).

## Methods

- **ManyIFEval:**
  - 216 IFEval task descriptions × 1–10 instructions = 2,160 samples.
  - 15 non-conflicting IFEval instruction types in six categories: keyword,
    length, format, case, start/end, punctuation.
  - Incompatible combinations are excluded algorithmically.
- **StyleMBPP:**
  - 500 MBPP problems × 1–6 Pylint-checkable style rules = 3,000 samples.
  - Rules: MIT licence notice, 2-space indentation, docstrings, comparison
    operators, 79-character lines, variable-name length.
- **Models:** GPT-4o, Claude 3.5 Sonnet (2024-06), Gemini 1.5 Pro, o3-mini
  (low/med/high), Gemma2-2B/9B, Llama3.1-8B, Qwen2.5-72B, DeepSeek-V3, R1.
  Zero-shot.
- **Scoring:** fully programmatic and rule-based.

## Results

Prompt-level accuracy (all instructions satisfied), ManyIFEval (Table 8):

| Model | n=1 | n=3 | n=5 | n=7 | n=10 |
|---|---|---|---|---|---|
| o3-mini (high) | 1.00 | 0.95 | 0.90 | 0.83 | 0.78 |
| o3-mini (low) | 0.97 | 0.92 | 0.81 | 0.69 | 0.53 |
| Claude 3.5 Sonnet | 0.95 | 0.88 | 0.72 | 0.67 | 0.48 |
| Gemini 1.5 Pro | 0.96 | 0.86 | 0.71 | 0.58 | 0.39 |
| DeepSeek-R1 | 0.95 | 0.81 | 0.71 | 0.59 | 0.38 |
| GPT-4o | 0.94 | 0.73 | 0.57 | 0.39 | 0.21 |
| DeepSeek-V3 | 0.96 | 0.85 | 0.63 | 0.43 | 0.19 |
| Qwen2.5-72B | 0.95 | 0.71 | 0.40 | 0.19 | 0.02 |
| Gemma2-2B | 0.80 | 0.36 | 0.08 | 0.01 | 0.00 |

- **Instruction-level accuracy stays high on ManyIFEval:** Claude 3.5 Sonnet
  0.95 → 0.93 and GPT-4o 0.94 → 0.85 at n = 10. Most of the decay is small
  per-instruction slippage compounding across instructions.
- **But per-instruction rates do fall in combination.** The naive product of
  *isolated* success rates under-predicts the decay (MAE 0.34 at n = 10). The
  product of in-combination rates fits (MAE 0.02).
- **StyleMBPP prompt-level, n = 1 → 6:**
  - Claude 3.5 Sonnet 0.96 → **0.01**
  - Gemini 1.5 Pro 0.97 → 0.13
  - GPT-4o 0.93 → 0.68
  - o3-mini (high) 0.95 → 0.37
  - DeepSeek-R1 0.90 → 0.12
- **What drives it:** the "≤79 characters per line" rule. It is followed 97%
  (Claude) and 99% (Gemini) of the time in isolation, but only 2% and 20% when
  combined with five other rules.
- **Sample size for estimation:** about 500 samples (ManyIFEval) and 300
  (StyleMBPP) suffice for stable estimates.

## Critique / open questions

- **Strong design for isolating dose:** a fixed task, only the count varies,
  balanced n per count, programmatic verification. The outcome is compliance,
  not an LLM judge, and the paper itself shows the judge would have hidden the
  effect.
- **Scope limits:**
  - simple, independent, format-level constraints
  - no semantic or procedural instructions
  - single-turn
  - no agentic tasks
  - models are a 2024–early-2025 generation
- The authors flag that semantic and conditional instructions are untested.
- **The code-generation result maps directly onto "invariants in code".** Style
  rules a linter can check deterministically are exactly the ones models fail
  in combination, while the functional task survives.
- **2×2 placement:** the *terse* row with constraint count as the dose. It says
  nothing about intent vs procedure, but it does price each added terse
  requirement.

## Trust signals

- **Credibility:** 4. Peer-reviewed (Findings of EMNLP 2025), data and
  evaluation code released, Matsuo lab (UTokyo), rule-based scoring, balanced
  design. Limits: an older model set and synthetic constraints.
- Citations not looked up: the Semantic Scholar API was rate-limited.

## Follow-up

- **Relevance:** 4. The cleanest controlled dose-response evidence for
  instruction-density decay at small counts (1–10). It prices each requirement
  that P2 asks authors to write down.
- **Guide:** P2 refines. Coverage has a compounding price: each added
  checkable requirement multiplies the chance that *something* is missed. For
  Claude 3.5 Sonnet, 10 instructions dropped all-satisfied from 0.95 to 0.48
  (o3-mini-high: 0.78). Cover what is needed, not everything. P3 also supports:
  machine-checkable rules (line length, style) collapse in combination
  (0.97 → 0.02), so give them to a linter or hook.
- Pair with jaroslawicz2025instructions (IFScale) for the 10–500 range and
  frontier-model curves.
