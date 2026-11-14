---
kind: paper
title: "You Don't Need Prompt Engineering Anymore: The Prompting Inversion"
authors: ["Imran Khan"]
institutions: ["Independent Researcher"]
year: 2025
venue: "arXiv preprint (v1, 2025-10-25)"
peer_reviewed: false
url: "https://arxiv.org/abs/2510.22251"
code_url: "https://github.com/strongSoda/prompt-sculpting"
citations: 3
source: "raw/papers/khan2025prompting.pdf"
added: "2026-11-14"
relevance: 3
credibility: 1
status: read
related_experiments: []
related_concepts: ["[[concepts/degrees-of-freedom]]", "[[concepts/cross-model-prompt-transfer]]", "[[concepts/guidance-distraction]]"]
tags: [prompting, constraints, capability-scaling, gsm8k, gpt-5, hyper-literalism]
---

# You Don't Need Prompt Engineering Anymore: The Prompting Inversion

## TL;DR

The paper compares a rule-heavy constrained prompt ("Sculpting": persona, "use
ONLY the numbers given", "do NOT use common sense") with plain zero-shot CoT
on GSM8K. Sculpting helps gpt-4o on a 100-problem subset (97% vs 93%). On the
full set, gpt-5 does worse with it (94.00% vs 96.36%), with errors from
hyper-literal readings. The direction is plausible, but the evidence is weak.
The single-author paper has fabricated-looking case studies and a
nonexistent model ID.

## Claims

- There is a "Prompting Inversion": constraints act as guardrails for
  mid-tier models but as "handcuffs" for advanced ones (abstract, §5.5).
- On gpt-5, Sculpting induces hyper-literalism, rejection of reasonable
  inference, and over-constraint (§5.3).
- Prompts should be versioned by model capability. The paper suggests a
  heuristic: below 90% validation accuracy use constraints, above 95% use
  simple prompts (§6.2.1).

## Methods

- Three prompts:
  - Zero Shot (question only);
  - "Scaffolding" (= zero-shot CoT: "Let's think step-by-step");
  - "Sculpting" (persona + 4 rules).
- Models: gpt-4o-mini, gpt-4o and gpt-5. Temperature 0, one query per item,
  no confidence intervals.
- gpt-4o-mini, gpt-4o and gpt-5 ran on the same random 100-problem subset.
  Only gpt-5 ran on the full 1,317 parseable items.

## Results

- **Verified against the paper and the released data files.**
  - gpt-4o (100-item subset, Table 2): Zero Shot 88%, CoT 93%, Sculpting 97%.
  - gpt-5 (full 1,317, Table 4): Zero Shot 94.00% (1238), CoT 96.36% (1269),
    Sculpting 94.00% (1238).
  - The repo's `gsm8k_gpt5_full_benchmark_results.json` reproduces exactly
    1269/1238/1238, and the gpt-4o subset file reproduces 88/93/97.
- gpt-4o-mini (100): 86 / 91 / 93. gpt-5 (100): 97 / 99 / 97.
- Error table on the 100-item subset (Table 6):
  - gpt-4o: CoT made 7 errors, Sculpting 3.
  - gpt-5: CoT made 1 error, Sculpting 3 (2 hyper-literal, 1 over-constraint).

## Critique / open questions

- **Discrepancy with the candidate summary.** The headline numbers are right,
  but the gpt-4o comparison (97 vs 93) is on **100 problems only**. That is a
  4-item difference with no significance test, so the "inversion" rests on a
  single full-benchmark contrast for one model.
- **Case studies don't match the data.** Checked against the GSM8K test file
  and the author's released outputs:
  - gsm8k_test_42 ("Fibonacci"), _57 ("lemonade stand") and _73 ("shirt
    discount") are different problems in GSM8K. The quoted problems don't
    appear in the test set at all. In the released outputs, Sculpting solved
    the real items at those IDs.
  - The "Fibonacci" item's stated expected answer is also internally
    inconsistent.
  - Only the iPhone case (test_40, Sculpting answered 12) and the gift-bag
    case (test_89) are real.
  - The "Sprint" case is listed as a Scaffolding failure, but the paper itself
    says Scaffolding got it right.
- **Model ID problem.** The paper names "gpt-5-preview-2024-10-01", but no
  such model existed. The released script calls `"gpt-5"`.
- **Narrow setup:** single benchmark, single vendor lineage, a near-ceiling
  task, one sample per item.
- **2×2:** Sculpting is *terse procedure + negative constraints*. The
  comparison is constraint-heavy vs. minimal prompting, not intent vs. script.
  No rationale or context is given in any condition.
- The underlying point does match other sources: prohibitions that override
  a strong model's pragmatic reading cause literalism errors.

## Trust signals

- **Credibility:** 1. Independent single author, not peer reviewed. Code and
  per-item outputs are released, and the headline counts check out. But at
  least three case studies cannot be found in the dataset, and the model ID
  is impossible. Semantic Scholar showed 3 citations on 2026-11-14.

## Follow-up

- **Relevance:** 3. On topic for Q2 (capability boundary for constraints).
  Usable only as a weak, single-model data point.
- **Guide:** P1 supports (weakly) — blanket behavioural prohibitions that
  helped gpt-4o cost gpt-5 2.4 pp on GSM8K via hyper-literalism. Do not cite
  it as more than a `[weak]` anecdote, given the integrity problems.
