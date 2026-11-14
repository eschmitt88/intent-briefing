---
kind: paper
title: "ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize"
authors: ["Lihao Liu", "Peng Tang", "Kunwar Yashraj Singh", "Shabnam Ghadar"]
institutions: ["AWS Agentic AI"]
year: 2026
venue: "EMNLP 2026 (per arXiv comment)"
peer_reviewed: true
url: "https://arxiv.org/abs/2609.04197"
code_url: null
citations: 1
source: "raw/papers/liu2026espo.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/llm-authored-instructions]]", "[[concepts/instruction-density-decay]]", "[[concepts/requirement-coverage]]"]
tags: [prompt-optimization, prompt-bloat, gepa, prompt-length, bootstrap-selection]
---

# ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize

## TL;DR

GEPA's reflective loop keeps appending rules. Its final prompts average 1.87×
ESPO's length (up to ~3×) and are less accurate. ESPO does three things:
- diagnoses all training errors at once into 3–7 patterns;
- proposes candidates via 4 strategies (diagnostic revision, consolidation,
  ablation, factual injection);
- picks candidates by bootstrap stability.

ESPO gets +3.76 pp over GEPA (74.67 vs 70.91, Claude Sonnet 4.5 student, 7
benchmarks) with prompts 47% shorter (1,004 vs 1,878 chars). The key control:
**forcing GEPA to be short does not make it better.** A length cap cuts length
38% but changes accuracy by +0.09 pp, and HotpotQA drops 4.2 pp. Length is a
symptom of undiagnosed rule accretion, not the lever.

## Claims

- Evolutionary optimizers bloat because of three issues:
  - incomplete error observation (3–8 random errors per reflection, so ~15
    rounds to see all patterns at 95%);
  - one mutation operator that "compensates by stacking more rules";
  - noisy point-estimate selection on a ~30-example validation set, which can
    pick "a verbose candidate that ranks first by noise".
- Fixing all three yields shorter *and* more accurate prompts. No single fix
  does both.
- The concise-by-construction behavior holds across student models.

## Methods

- Student: Claude Sonnet 4.5 (T = 0). Reflection: Claude Sonnet 4.5 (T = 0.7)
  throughout.
- Cross-model: 4 more students (Gemma 3 12B, Mistral 14B, Qwen3 32B, Claude
  Haiku 4.5), each **re-optimized from scratch**. This is not zero-shot
  transfer of prompts.
- 7 benchmarks: Tweet, MMLU, GSM8K, HotpotQA, ScoNe, HoVer, PUPA. Each uses
  70 train / 30 val / 500 test.
- Baselines: Default, DSPy BootstrapFewShot, COPRO, MIPROv2, GEPA.
- **All methods start from a deliberately weak, partly misleading seed** (e.g.
  "Classify the tweet by leaning 'negative'"). Appendix D.4 reruns with a
  strong, task-tuned seed.
- Main-table cells are single runs, with ±std over 3 more seeds. Appendix
  Table 11 gives the full 3-seed means.
- Ablations: per-component additions atop GEPA, and "Constrained GEPA"
  (compact proposer instruction plus max_length_ratio = 1.2 relative to the
  seed). Both are single-seed.

## Results

- **Main (Sonnet 4.5):** average accuracy 74.67 (ESPO) vs 70.91 (GEPA). The
  3-seed means are 74.55 vs 70.74. The paired SE of the gap is ≈1.2 pp
  (≈3.1 SE). ESPO is ≥ GEPA on all 7 datasets, but HotpotQA (+0.80), PUPA
  (+1.20) and GSM8K (tie) are within noise.
- **Length:** average 1,004 vs 1,878 chars. Examples:
  - HotpotQA: GEPA 2,845 chars, 44.00%; ESPO 1,008 chars, 44.80%.
  - Tweet: GEPA 1,279 chars, 68.60%; ESPO 774 chars, 74.78%.
- **Constrained GEPA (Table 2):**

  | config | accuracy | length |
  |---|---|---|
  | GEPA | 70.91% | 1,878c |
  | Constrained GEPA | 71.00% | 1,171c |
  | ESPO | 74.67% | 1,004c |

  Constrained GEPA cuts length 38% for +0.09 pp. On HotpotQA it falls 44.00 →
  39.80. An indiscriminate length cut discards needed rules along with
  redundant ones.
- **Per-component ablation (Table 13, single seed):**

  | config | accuracy | length |
  |---|---|---|
  | GEPA | 70.91 | 1,878 |
  | + multi-strategy | 72.39 | 1,924 |
  | + bootstrap select | 72.50 | 1,816 |
  | + full-error diagnosis | 73.24 | 1,843 |
  | all three (ESPO) | 74.67 | 1,004 |

  Only the combination cuts length. Diversity without diagnosis grows the
  prompt.
- **Strong seed (Table 12):** Default 62.60, GEPA 71.11, ESPO 75.90 (+4.79 pp).
  The authors say GEPA "keeps appending marginal rules to an already-good
  prompt (length grows, accuracy stagnates)". Strong-seed lengths are not
  tabulated.
- **Students (average accuracy, GEPA → ESPO):**

  | student | GEPA | ESPO |
  |---|---|---|
  | Gemma 3 12B | 63.71 | 66.50 |
  | Mistral 14B | 59.14 | 62.42 |
  | Qwen3 32B | 59.11 | 68.31 |
  | Haiku 4.5 | 67.98 | 70.15 |

  ESPO prompts are 30–60% shorter on every student. Qwen3 GSM8K: Default 15.00
  → GEPA 35.40 → ESPO 91.40, attributed to a diagnosed output-format mismatch.
- Open-ended pilot (XSum, 200 articles): ESPO wins 58% / ties 22% / loses 20%
  vs GEPA. Prompt length 720 vs 2,180 chars. The judge was Claude Sonnet 4.5,
  the same family as the reflection model.

## Critique / open questions

- **Discrepancy vs the candidate summary:** "up to 3× longer" is GEPA
  *relative to ESPO's prompts* (1.87× on average). It is not growth relative
  to the seed, and these prompts are small (≈0.6–3K **characters**). The
  "~12K tokens" figure belongs to SAGE (its own prompt on FiNER), not to this
  paper or to GEPA.
- **Data anomaly:** in Table 3, several GEPA final-prompt lengths are
  character-identical to the Sonnet runs on other students: Tweet 1,279 on
  Gemma, Mistral and Qwen3; HotpotQA 2,845 and ScoNe 1,948 on Gemma and
  Mistral; GSM8K 660. Some ESPO lengths repeat too (Tweet 774 and GSM8K 660 on
  Gemma). That is implausible if each student was re-optimized "from scratch".
  It suggests copied cells or reused prompts. Treat per-student length numbers
  with caution.
- Default-seed lengths also differ between Fig. 1 (Tweet 609c) and Table 3
  (487c).
- The weak, misleading seed inflates gaps against non-reflective baselines and
  stresses recovery rather than refinement. The strong-seed rerun partly
  answers this.
- The validation set is only 30 examples. Constrained GEPA and the component
  ablation are single-seed. Gaps of 1–2 pp are within noise (95% CI ±3.8 pp at
  n = 500).
- Outcomes are task metrics (accuracy, EM, F1), which is good, except for the
  XSum pilot. That pilot is an LLM judge from the same family as the
  optimizer, so discount it.
- No agentic or tool-use tasks; the authors list these as out of scope.
- 2×2 placement: GEPA drifts toward **verbose procedure**, a pile of
  if-then caveats (Fig. 1: "If the tweet contains 'but' consider both
  clauses... Watch for negation words... Double-check ambiguous cases").
  ESPO's winning prompts are **terse** but not pure intent: a short task
  statement plus the few diagnosed rules that matter. The constrained-GEPA
  control is the cleanest evidence here that *which* constraints survive
  matters more than length.

## Trust signals

- **Credibility:** 3. Accepted at EMNLP 2026 per the arXiv comment. Industry
  lab (AWS). 3-seed variance on the main grid, plus a sensible length-control
  ablation. The paper says code and prompts are released but gives no URL, so
  code_url is null. Limited by a 30-example validation set, single-seed
  ablations, and the unexplained duplicate lengths across students. 1 citation
  (Semantic Scholar, 2026-11-14).

## Follow-up

- Check whether the released code (once located) explains the duplicate
  per-student GEPA lengths.
- **Relevance:** 3. The best measured evidence so far on LLM-authored prompt
  growth vs accuracy, with a length-controlled ablation. It is non-agentic,
  short-prompt evidence.
- **Guide:** P6 supports. Reflective LLM authors accrete redundant rules
  (1.87× longer) that don't buy accuracy.
- **Guide:** P2 refines. Coverage should come from diagnosed error patterns.
  Blind brevity (length caps) doesn't help and can cost 4 pp. Coverage of the
  right requirements beats both bloat and brevity.
