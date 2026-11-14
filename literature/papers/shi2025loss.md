---
kind: paper
title: "No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization"
authors: ["Wenhang Shi", "Yiren Chen", "Shuqing Bian", "Xinyi Zhang", "Kai Tang", "Pengfei Hu", "Zhe Zhao", "Wei Lu", "Xiaoyong Du"]
institutions: ["Renmin University of China", "Peking University", "Tencent"]
year: 2025
venue: "NeurIPS 2025"
peer_reviewed: true
url: "https://arxiv.org/abs/2509.23387"
code_url: "https://github.com/Eric8932/GRACE"
citations: 10
source: "raw/papers/shi2025loss.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/cross-model-prompt-transfer]]", "[[concepts/instruction-density-decay]]", "[[concepts/llm-authored-instructions]]"]
tags: [prompt-optimization, compression, prompt-length, transfer, bbh]
---

# No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization (GRACE)

## TL;DR

GRACE is an automatic prompt optimizer that gates updates and periodically
**compresses** the prompt, abstracting "narrow conditionals or memorized
phrasings" into general guidance. It beats prior optimizers on 11 tasks while
using about 25% of their prompt budget. Two results matter here. First,
prompts optimized on DeepSeek-V3 **transfer only partially**: gains shrink from
+16.7 pts on the source model to +7.2 (Llama-3.3-70B) and +5.9 (GPT-4.1), with
one regression. Second, accumulated case-specific detail made prompts longer
without making them better, and compressing it held or raised accuracy.

## Claims

- Reflection-based optimizers (APO, PromptAgent) make over-strong, biased
  updates and get trapped in local optima. Search-based ones (EvoPrompt, OPRO)
  barely move from the seed.
- Deliberate "information loss" through gated updates and compression improves
  optimization. Compression removes redundant, overly specific content and
  helps escape local optima.
- GRACE-optimized prompts show "partial transferability". They work best on
  the base model they were optimized for.

## Methods

- Optimizer LLM DeepSeek-R1; base (target) LLM DeepSeek-V3-0324. Appendix
  repeats this with GPT-4.1 as the base.
- 11 tasks: 5 BBH (Geometry, Translation error, Snarks, Movie, Epistemic), 3
  biomedical (NCBI, Biosses, MedQA), 3 general NLP (Subj, TREC, CB). Plus 2
  summarization sets in the appendix (ROUGE-L).
- Gated refinement uses 3 success and 3 failure samples per update, with
  rejection of non-improving candidates. Compression triggers after K = 5
  consecutive rejections. T = 80 steps, compared with ~300 generated prompts
  for the baselines.
- Prompts are selected on a validation set and scored on a disjoint test set.
- Transfer: prompts optimized on DeepSeek-V3 for the 5 BBH tasks were scored
  without re-tuning on Llama-3.3-70B-Instruct and GPT-4.1.

## Results

- Main (DeepSeek-V3, Table 1): BBH average 94.13 vs PromptAgent 89.42, APO
  88.14, CoT(FS) 79.62, zero-shot 77.45. Domain-specific average 82.00 vs
  77.60. General NLP average 96.63 vs 93.94. The paper reports relative gains
  over the best prior optimizer of 4.7% / 4.4% / 2.7%.
- **Cross-model transfer (Table 7, 5 BBH tasks, average accuracy):**

  | target | zero-shot seed | PromptAgent | GRACE | GRACE gain |
  |---|---|---|---|---|
  | DeepSeek-V3 (source) | 77.45 | 89.42 | 94.13 | +16.68 |
  | Llama-3.3-70B | 77.93 | 80.07 | 85.17 | +7.24 |
  | GPT-4.1 | 74.31 | 76.74 | 80.21 | +5.90 |

  - Gains on transfer are roughly 35–45% of the source-model gain.
  - Regression: on Epistemic with GPT-4.1, GRACE 82.50 and PromptAgent 84.25
    both fall below the zero-shot seed (87.00).
  - Biggest drop: Geometry gains +34.5 on the source (62.5→97.0) but only +9.0
    on GPT-4.1 (43.0→52.0) and +3.0 on Llama (72.5→75.5). The final Geometry
    prompt (Table 25) is a long numbered rule script with tolerances and
    priority overrides.
- **Prompt length (Fig. 5d, TREC only, plotted not tabulated; lengths up to
  ~2k):**
  - Local accuracy peaks often coincide with local length maxima.
  - At several compression points, accuracy holds or rises despite a shorter
    prompt.
  - Without compression, length keeps growing while accuracy stagnates.
  - The CB trace (Table 2) shows the mechanism: steps 4–5 add more elaborate,
    "case-bound" rules and the score falls (94.6→92.9→91.1). Compression at
    step 9 restores 94.6, and step 13 reaches 96.4.
- Cost: GRACE converges with about 25% of the baselines' prompt-generation
  budget (Table 3/11, TREC).

## Critique / open questions

- All outcomes are task accuracy or F1 against gold labels, with no LLM
  judge. That is good for this project.
- Single-lineage optimizer and target (DeepSeek-R1 → DeepSeek-V3). Transfer is
  tested only on 5 BBH tasks and 2 targets. No variance is reported. Results
  appear to be single runs, and "the best test result is reported" is
  ambiguous about selection on test.
- The length evidence is one task (TREC), shown as a figure, plus a
  qualitative CB trace. It shows that length and accuracy are decoupled, not a
  dose-response curve. It is suggestive, not measured at scale.
- These are short classification/reasoning prompts, not agentic tasks or
  multi-step tool use. The "reader" is the target model, not a peer agent.
- 2×2 placement: optimizer outputs drift toward **verbose procedure** (numbered
  rule lists, conditionals). Compression pushes toward **terse,
  generalized guidance**, which is closer to the terse-intent cell, although
  the instructions remain task heuristics rather than goals plus rationale.
  The pattern (accreted case rules overfit, abstraction generalizes) lines up
  with the hypothesis. The stronger transfer loss for the most script-like
  prompt (Geometry) is suggestive with n = 1.

## Trust signals

- **Credibility:** 3. Peer-reviewed at NeurIPS 2025 and code released
  (github.com/Eric8932/GRACE). Academic plus Tencent authors, 10 citations
  (Semantic Scholar, 2026-11-14). Limited by a single model lineage, no
  variance, and transfer and length analyses in the appendix or figures only.

## Follow-up

- **Relevance:** 3. Cite-worthy measured evidence that machine-optimized
  prompts lose most of their gain across target models, and that accreted
  case-specific detail adds length without accuracy.
- **Guide:** P2 refines. Unstated-requirement coverage helps, but accreting
  case-specific rules overfits. Coverage should be general constraints, not
  edge-case scripts. Gains shrink ~55–65% when transferred across models, which
  is consistent with the "regress across model changes" clause.
- **Guide:** P1 supports (weak, indirect). Abstracting narrow conditionals into
  general guidance held or improved accuracy, and the most script-like
  optimized prompt transferred worst.
