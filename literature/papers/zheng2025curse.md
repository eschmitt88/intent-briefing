---
kind: paper
title: "The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning"
authors: ["Tianshi Zheng", "Yixiang Chen", "Chengxi Li", "Chunyang Li", "Qing Zong", "Haochen Shi", "Baixuan Xu", "Yangqiu Song", "Ginny Y. Wong", "Simon See"]
institutions: ["The Hong Kong University of Science and Technology", "NVIDIA"]
year: 2025
venue: "Transactions on Machine Learning Research (11/2025)"
peer_reviewed: true
url: "https://arxiv.org/abs/2504.05081"
code_url: "https://github.com/HKUST-KnowComp/CoT-ICL-Eval"
citations: null
source: "raw/papers/zheng2025curse.pdf"
added: "2026-11-14"
relevance: 2
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/guidance-distraction]]", "[[concepts/cross-model-prompt-transfer]]"]
tags: [chain-of-thought, in-context-learning, reasoning-models, demonstrations]
---

# The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning

## TL;DR

On nine pattern-induction in-context-learning benchmarks (ARC-AGI, SCAN, COGS,
List Function, RAVEN, …) across 16 LLMs, direct answering beats CoT by 5.1 pp
absolute (20% relative). It beats ReAct and ToT by more. Long-CoT reasoning
models use about 40× more inference tokens yet only match the best
direct-answering LLMs.

## Claims

- CoT and its variants consistently underperform direct answering on
  pattern-based ICL. The gap widens with more demonstrations (3 → 15 shots on
  COGS and List Function).
- Mechanism, an "explicit-implicit hybrid":
  - Explicit pattern inference from demonstrations is the bottleneck: models
    execute a given rule better than they infer it.
  - The CoT rationale also increases the "contextual distance" between the
    demonstrations and the answer, which degrades implicit (direct-answer-like)
    pattern use.
  - Implicit reasoning drives most CoT successes: 7.5× (List Function) and
    3.6× (MiniSCAN) more often than explicit reasoning.
- Long-CoT LRMs (QwQ-32B, o1-mini, DeepSeek-R1) don't overcome this.

## Methods

- 16 LLMs (Llama 3.1 8B–405B, Qwen2.5, Gemma2, Mistral, Gemini 1.5/2.0,
  GPT-3.5/4o/4o-mini, DeepSeek-V3) plus 3 LRMs analysed separately.
- 9 datasets, 8,594 instances; symbolic, textual, and numerical modalities.
- Exact-match task-outcome accuracy.
- Hypothesis tests:
  - dummy rationales (Shakespeare recitation or countdown, 150–1,200 tokens)
  - rationale front-loading (same rationale placed before the demonstrations)
  - inference vs execution split
  - explicit/implicit attribution

## Results

- **Direct vs CoT:** direct beats CoT by 5.10 pp absolute (20.42% relative),
  ReAct by 8.02 pp, ToT by 9.64 pp. The gap is largest on symbolic tasks
  (41.9% relative) and smaller on textual ones (10.4%).
- **Mitigating factors:** larger models narrow the gap, and CoT occasionally
  ties.
- **Contextual distance:** dummy rationales degrade accuracy as their length
  grows. Front-loading the rationale recovers some accuracy but still trails
  direct answering.
- **LRMs vs direct-answering LLMs** (Table 2; average over MiniARC, COGS, RAVEN):
  - DeepSeek-R1 26.81%, o1-mini 18.68%, QwQ-32B 13.51%.
  - Gemini-1.5-pro (direct) 28.38%, DeepSeek-V3 (direct) 26.46%.
  - Token cost is about 2,400–3,100 for LRMs vs about 200.
  - LRMs use 12× more total tokens and **40× more inference tokens**. The
    candidate summary's "~40×" is confirmed.

## Critique / open questions

- **Rigorous within scope:** peer-reviewed (TMLR, OpenReview 7SIrvcYNYj), code
  released, broad model set, task-outcome metric, and mechanism experiments
  with acknowledged confounds (the dummy-rationale controls are imperfect).
- **Scope is narrow for this project:**
  - inductive pattern-learning from input-output demonstrations
  - no instructions, briefs, or agentic tasks
  - absolute accuracies are low (about 20–30%), so the tasks sit at the edge
    of model ability
  - SCAN may be contaminated
- **2×2 placement:** off-axis. It contrasts reasoning modes, not
  instruction styles. The loose analogy is that imposing explicit stepwise
  procedure on a task the model does better implicitly can hurt, and more
  deliberation isn't free.
- **Possible bearing on P1:** it is consistent with claims that reasoning
  models handle raw demonstrations poorly (cf. 2509.23196, "literal demos hurt
  reasoning models"). But the mechanism here is pattern *induction*, not
  instruction following.

## Trust signals

- **Credibility:** 4. Peer-reviewed in TMLR, code on GitHub, HKUST and NVIDIA,
  16 models and 9 benchmarks with deterministic scoring. The mechanism claims
  rest on proxy experiments.
- Citations not looked up: the Semantic Scholar API was rate-limited.

## Follow-up

- **Relevance:** 2. Tangential. It is about CoT in few-shot pattern induction,
  not briefing. The "40× tokens" cost figure is useful background for
  deliberation-cost arguments.
- **Guide:** P1 refines (weakly). For pattern-from-examples tasks, adding
  explicit reasoning or procedure on top of demonstrations underperforms, and
  reasoning models pay about 40× the inference tokens without gain. Don't
  assume more deliberation or scaffolding helps. At most, cite next to
  2509.23196 on demos vs reasoning models. Don't tag any line on this alone.
