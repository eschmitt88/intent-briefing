---
kind: paper
title: "When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs"
authors: ["Xiaomin Li", "Zhou Yu", "Zhiwei Zhang", "Xupeng Chen", "Ziji Zhang", "Yingying Zhuang", "Narayanan Sadagopan", "Anurag Beniwal"]
institutions: ["Harvard University", "Amazon", "NYU"]
year: 2025
venue: "NeurIPS 2025 (Main Conference Track); read arXiv v3"
peer_reviewed: true
url: "https://arxiv.org/abs/2505.11423"
code_url: null
citations: null
source: "raw/papers/li2025thinking.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/guidance-distraction]]", "[[concepts/invariants-in-code]]", "[[concepts/instruction-density-decay]]"]
tags: [chain-of-thought, instruction-following, ifeval, complexbench, reasoning-models]
---

# When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs

## TL;DR

Prompting "think step by step" lowers single-turn constraint compliance on
IFEval (13 of 14 models) and ComplexBench (14 of 14). The drops are large for
small and mid open models and for Claude 3.5. They are near zero for the
strongest models tested (Claude 3.7 Sonnet, DeepSeek-V3/R1). Reasoning helps
formatting and lexical constraints. It hurts by neglecting simple mechanical
constraints and by adding well-meant extra content.

## Claims

- Explicit CoT (prompted, or a reasoning-tuned variant) can significantly lower
  instruction-following accuracy.
- A qualitative case study finds four recurring patterns:
  - **Helps:** (1) formatting and structure (valid JSON, quoting, markdown);
    (2) lexical precision (e.g. "letter q six times", no final punctuation).
  - **Hurts:** (3) over-focus on content planning, neglecting simple
    constraints (word limits, exact repetition, lowercase-only, trailing
    content); (4) adding unnecessary content that breaks constraints (English
    in foreign-only output, commas in "no commas" tasks, commentary after
    quotes).
- "Constraint attention" to constraint tokens falls under CoT. The drop is
  larger in cases where CoT loses.
- Mitigations: classifier-selective reasoning (a per-model trained classifier
  decides whether to use CoT) recovers most of the loss. Self-reflection helps
  on IFEval for larger models but hurts on ComplexBench in 10 of 14 models.

## Methods

- 14 models in the main table (Llama 3.x 1B–70B, Mixtral, Qwen2.5 1.5B/7B,
  R1-distills, Claude 3.5 Haiku/Sonnet, Claude 3.7 Sonnet, DeepSeek-V3). Plus
  base-vs-reasoning pairs (Claude 3.7 Sonnet vs Sonnet-Think, V3 vs R1).
  Temperature 0, single run.
- **IFEval:** 541 prompts with 1–3 rule-verifiable constraints, scored as
  instruction-level *loose* accuracy.
- **ComplexBench:** 1,150 compositional instructions, translated to English,
  scored by a rule-based **plus LLM-based** assessment.
- The CoT condition is a generic step-by-step prompt. No agentic tasks, no
  tools, no multi-turn.
- Attention analysis is mainly on Qwen2.5-1.5B. Constraint spans were
  extracted by GPT-4o.

## Results

| Model | IFEval orig → CoT | ComplexBench orig → CoT |
|---|---|---|
| Llama-3-8B | 75.2 → 59.0 (−16.2) | 55.8 → 54.9 |
| Llama-3.1-70B | 85.6 → 77.3 (−8.3) | 66.8 → 60.2 |
| Claude-3.5-Sonnet | 86.5 → 79.5 (−7.0) | 67.5 → 66.0 |
| Claude-3.5-Haiku | 86.9 → 79.5 (−7.4) | 66.9 → 62.1 |
| Claude-3.7-Sonnet | 90.6 → 90.2 (−0.4) | 69.8 → 67.0 |
| DeepSeek-V3 | 85.2 → 84.3 (−0.9) | 71.2 → 71.1 |
| Mixtral-8x7B | 53.0 → 56.4 (**+3.4**) | 60.4 → 58.3 |

- **Reasoning-tuned pairs** (Table 2):
  - Claude 3.7 Sonnet → Sonnet-Think: IFEval 90.6 → 90.2, ComplexBench
    69.8 → 69.0.
  - DeepSeek-V3 → R1: IFEval 85.2 → 83.3, ComplexBench 71.2 → 71.1.
- **Classifier-selective reasoning** (relative to CoT): e.g. Llama-3-8B +10.7,
  Claude-3.5-Haiku +6.3 (IFEval).
- **Reasoning length** doesn't correlate meaningfully with effectiveness
  (App. I).
- **No quantitative per-constraint-type breakdown.** The "helped vs hurt" types
  come from a manual case study only.

## Critique / open questions

- **Does it show lower adherence to *simple hard constraints*? Partly.**
  - "Neglecting simple constraints" is one of four *qualitative* failure
    patterns, illustrated with word count, lowercase, and no-comma examples.
  - Two other patterns show reasoning *helping* exactly such mechanical
    constraints (format, letter counts, punctuation).
  - The aggregate drop is real for mid-tier models but **≤1 pp for the
    strongest models tested**.
  - Nothing in the paper tests moving constraints into code or checks. So it
    is at most indirect support for "invariants in code".
- **Evaluation:**
  - IFEval scoring is fully programmatic, which is good.
  - ComplexBench scoring is partly LLM-judged.
  - Single run, no significance tests.
  - Prompt-level CoT on non-reasoning-tuned models differs from native
    thinking in current frontier models.
  - The model set stops at early-2025 (no o-series, no GPT-4o).
- **2×2 placement:** off-axis. The manipulation is a *reasoning mode*
  meta-instruction (a terse procedural "think step by step"). The constraints
  are terse hard requirements. It doesn't compare intent vs procedure briefs.
- **Agentic relevance is limited.** These are single-turn text constraints, not
  tool-using tasks. Mechanism: extra deliberation pulls attention toward
  content and away from mechanical constraints. This is a plausible analogue
  for long agent runs dropping small rules, but it is untested here.
- **Peer review:** confirmed in the NeurIPS 2025 proceedings (papers.neurips.cc;
  poster 115354), although arXiv v3 (2025-09-02) still says "Preprint. Under
  review." The proceedings abstract reportedly says "over 20 models". This note
  is from arXiv v3 (14 models in the main table, 15 counting pairs), so the
  camera-ready may add models.

## Trust signals

- **Credibility:** 3. Peer-reviewed (NeurIPS 2025), Amazon and Harvard
  authors, two standard benchmarks with mostly rule-based scoring. But no code
  is released, runs are single, there are no significance tests,
  per-constraint-type claims are qualitative only, and the frontier coverage is
  dated.
- Citations not looked up: the Semantic Scholar API was rate-limited.

## Follow-up

- **Relevance:** 3. Cite-worthy prior art on how deliberation trades off
  against mechanical constraints. Not canonical for any guide line, and its
  frontier-model effect is near zero.
- **Guide:** P3 refines. The current citation ("CoT lowers adherence to simple
  hard constraints") overstates the paper:
  - The drop is mostly in small and mid models (Claude 3.7 Sonnet −0.4 pp).
  - Reasoning *helps* formatting and lexical constraints.
  - Code enforcement isn't tested.
  
  Better wording: "explicit reasoning can crowd out simple mechanical
  constraints (word limits, case, forbidden characters), mainly below the
  frontier; deterministic checks don't depend on that." Keep the tag at
  `[weak]`.
- Read the NeurIPS camera-ready to see whether the added models (">20")
  change the frontier picture.
