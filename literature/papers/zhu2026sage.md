---
kind: paper
title: "SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration"
authors: ["Ziyi Zhu", "Luka Smyth", "Saki Shinoda", "Jinghong Chen"]
institutions: ["Slingshot AI", "University of Cambridge, Department of Engineering"]
year: 2026
venue: "EMNLP 2026 Industry Track (pp. 3695–3711)"
peer_reviewed: true
url: "https://arxiv.org/abs/2606.18902"
code_url: "https://github.com/slingshot-ai/sage"
citations: 0
source: "raw/papers/zhu2026sage.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/llm-authored-instructions]]", "[[concepts/instruction-density-decay]]", "[[concepts/context-engineering]]"]
tags: [prompt-optimization, multi-agent, prompt-bloat, overfitting, appworld, production-ab-test]
---

# SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration

## TL;DR

The paper frames prompt optimization as noisy black-box hill climbing and
compares three proposal strategies under the same meta-model (Claude Sonnet
4.6) and target (DeepSeek-V3.1):
- residual random search (SPO-RS);
- a genetic algorithm (SPO-GA);
- SAGE, a multi-agent pipeline that writes and runs diagnostic code.

No strategy dominates. On FiNER, SAGE's prompt **grew to ~12K tokens** while
the simpler strategies plateaued near ~3K. SAGE had the highest training
accuracy there but the worse test result, so uncontrolled growth tracked
overfitting. On AppWorld, SAGE produced the *shortest* prompts (~1.5K). The
~12K figure is SAGE's own bloat, **not GEPA's**.

## Claims

- No single search strategy dominates. Effectiveness depends on landscape
  ruggedness interacting with error structure: cascading reasoning errors
  reward root-cause diagnosis, while procedural per-task errors yield to
  simpler search.
- "Uncontrolled growth tracks overfitting." Unbounded prompt growth by
  accreting rules is the mechanism behind SAGE's poor FiNER test transfer.
- Agentic diagnosis plus quantitative validation helps most where the signal
  is noisy and ground truth is underspecified (open-ended dialogue).

## Methods

- Target LLM DeepSeek-V3.1. Meta-model Claude Sonnet 4.6 for all three
  strategies.
- Search: K = 10 iterations, population P = 2, Q = 3 candidates per iteration,
  monotonic hill climbing. The best-validation prompt is scored once on test.
  n = 3 runs per strategy.
- Benchmarks:
  - XBRL Formula: 500 train / 300 val / 200 test;
  - FiNER: 1,000 train / 500 val / 441 test;
  - AppWorld test-normal: 90 train / 57 val / 168 test, TGC metric, ReAct
    agent.
- Baselines: base, ICL, MIPROv2, GEPA, Dynamic Cheatsheet, ACE offline.
- Landscape analysis: semivariogram of accuracy over prompt-embedding
  distance.
- Production: 8 continuous-optimization cycles on a mental-health chatbot.
  Each cycle runs a ~48h A/B test on D1 retention, with winner's-curse
  correction by empirical-Bayes shrinkage.
- SAGE's Generator prompt (Appendix) instructs: "Concrete 'if X then Y'
  rules: Specific decision rules with examples, not vague guidance". It also
  says "Preserve and extend: Keep all existing rules from the parent prompt
  intact", next to "Avoid bloat".

## Results

- Test accuracy (Table 1, mean of 3 runs, Formula / FiNER / AppWorld):

  | method | Formula | FiNER | AppWorld |
  |---|---|---|---|
  | GEPA | 71.5 | 73.5 | 64.9 |
  | ACE offline | 85.0 | 76.9 | 76.2 |
  | SPO-RS | 85.5 | **77.5** | 78.0 |
  | SPO-GA | 85.5 | 76.2 | **79.8** |
  | SAGE | **86.5** | 76.5 | 79.2 |

- **Prompt length (Appendix B, Fig. 6):**
  - FiNER: SAGE "grows without bound (∼12K tokens) by accreting ever more
    disambiguation rules", while SPO-GA and SPO-RS plateau near ~3K. SAGE had
    the highest FiNER training accuracy but lost on test (76.5 vs 77.5 for
    SPO-RS).
  - AppWorld: SAGE converges shortest (~1.5K vs SPO-GA ~3K), "because its
    diagnostic analysis localizes a fix".
  - GEPA's prompt length is not reported.
- Landscape: FiNER is smooth (stays correlated over ~4× the embedding distance
  of the other two tasks). Formula and AppWorld are rugged.
- Production: 7 of 8 cycles promoted an arm, and only 2 cycles were
  individually significant. Naive chained gain in D1 retention was +29.4%;
  selection-adjusted it was +13.2%, with the 95% band clearing zero from cycle
  5. A product-level metric moved +13.7% over the same period, but this was
  uncontrolled.
- Cost: ~$66 per SAGE run, ~1.05 h, ~350 model turns.

## Critique / open questions

- **Discrepancy vs the candidate summary:** the "~12K tokens" is SAGE's own
  prompt on FiNER, not GEPA's. "Up to 3× longer without matching accuracy" is
  ESPO's claim about GEPA (see [[literature/papers/liu2026espo]]). The bloat
  evidence here is one task, one figure, n = 3. The test gap tied to bloat is
  ~1 pt on 441 examples (76.5 vs 77.5), within plausible run noise. No
  per-run variance is tabulated.
- The bloat has a plausible cause in the authoring instructions themselves:
  the Generator is told to write concrete if-X-then-Y rules and to keep all
  existing rules. That is an LLM author instructed to accrete procedure. The
  paper doesn't ablate this.
- Benchmark outcomes are task metrics (accuracy, TGC), which is good. The
  production metric (D1 retention) is a behavioral outcome, not an LLM judge.
  It is a proxy, and the A/B arms were clinically pre-filtered.
- Single target model (DeepSeek-V3.1) and single meta-model. No cross-model
  transfer. AppWorld val (57) is small, and the authors note noisy rankings.
- 2×2 placement: the optimizer's output style is **verbose procedure**
  (if-then rules, definition blocks, worked examples). Where it bloated
  (FiNER), it overfit. Where diagnosis localized a fix (AppWorld), a shorter
  prompt won. This supports targeted rather than accreted coverage, not
  intent-over-procedure as such.

## Trust signals

- **Credibility:** 3. Peer-reviewed (EMNLP 2026 Industry Track) and code
  released (github.com/slingshot-ai/sage). Small company plus Cambridge,
  honest winner's-curse correction in production, n = 3 runs. The prompt-bloat
  evidence is appendix-only and single-task. 0 citations (Semantic Scholar,
  2026-11-14).

## Follow-up

- **ESPO (arXiv 2609.04197)** adds measured prompt-length vs accuracy evidence
  for GEPA, including a length-constrained-GEPA ablation. It is ingested as
  its own note: [[literature/papers/liu2026espo]].
- ACE (Zhang et al. 2026, grow-and-refine context) and MCE (Ye et al. 2026)
  are cited as the closest relatives and are candidates for the
  context-engineering thread.
- **Relevance:** 3. Measured, if thin, evidence that an LLM author told to
  accumulate rules produces bloated prompts that overfit. This is directly
  relevant to LLM-authored instructions.
- **Guide:** P6 supports. LLM-authored prompt accretion (~12K tokens) tracked
  overfitting. P2 refines. Coverage should come from diagnosed, localized
  fixes. Accumulating rules raises training accuracy and loses on test.
