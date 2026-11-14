---
kind: paper
title: "AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators"
authors: ["Aritra Mazumder", "Shubhashis Roy Dipta", "Nusrat Jahan Lia", "Tanzila Khan", "Kainat Raisa Hossain", "Nehaa Shri", "Shubhrangshu Debsarkar", "Humayra Tasnim", "Gour Gupal Talukder Shawon", "Debjoty Mitra", "Sumaiya Ahmed Rani", "Al Jami Islam Anik", "Al Nafeu Khan"]
institutions: ["University of Utah", "University of Maryland, Baltimore County", "University of Dhaka", "Vellore Institute of Technology", "University of Virginia", "Rajshahi University of Engineering and Technology", "Shahjalal University of Science and Technology", "BRAC University", "Islamic University of Technology", "Comilla University"]
year: 2026
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2605.08647"
code_url: "https://github.com/aritra741/AgentCollabBench"
citations: 3
source: "raw/papers/mazumder2026agentcollabbench.pdf"
added: "2026-11-14"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/invariants-in-code]]"]
tags: [multi-agent, benchmark, constraint-loss, topology, instruction-decay]
---

# AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators

## TL;DR

A 900-task diagnostic benchmark (SWE, DevOps, data engineering) with four
process metrics for multi-agent pipelines: instruction decay under peer
pressure, tracer survival across hops, false-belief contagion, and
cross-task leakage. The headline is topology. Converging-DAG nodes drop
information that arrives on only one of N parent inputs at 1.6-5.0x the
per-hop rate of linear chains.

## Claims

- Outcome-only evaluation misses constraint loss: a pipeline can emit a
  valid, complete artifact with the critical constraint silently dropped.
- Communication topology explains 7-40% of variance in multi-hop information
  survival (eta^2 = 0.07-0.40). That is comparable to the choice of backbone.
- The mechanism is a "synthesis bottleneck" at converging-DAG nodes: an
  agent weighing competing parent inputs discards constraints carried by
  only one of them.
- No model dominates all four metrics. Capability benchmarks don't predict
  the profiles.

## Methods

- 900 human-validated tasks; the baseline run reports 916. Three domains,
  five topologies (linear chain, branching tree, converging DAG, fully
  connected, custom graph), three complexity tiers.
- Metrics, each tied to an injected artifact:
  - **IDR** (Instruction Decay Rate): a hard constraint sits in the target
    agent's system prompt. Peers then invite violation, mildly and then more
    strongly. An LLM judge labels each turn compliant or violating.
  - **RTD** (Radioactive Tracer Durability): exact-match depth reached by a
    unique tracer string. Deterministic.
  - **CPR** (Consensus Pollution Rate): spread of a seeded false fact. LLM
    judge.
  - **CLC** (Cross-task Leakage Containment): private tracer from task A
    appearing in task B. Deterministic.
- Judge: DeepSeek V4 Flash, disjoint from the backbones.
  - Human-human IAA: kappa = 0.739 on 120 items.
  - Human-LLM agreement: 86.7%, kappa = 0.688 (for GPT-4.1-mini judge
    labels).
- Backbones: GPT-4.1 mini, Gemini 2.5 Flash Lite, Qwen-3.5-35B-A3B,
  Llama 3.1 8B Instruct.
- Statistics: Mann-Whitney with Bonferroni correction, Kruskal-Wallis and
  Dunn tests. Perturbation ladders validate the constructs.

## Results

Baseline profiles (Table 9; mean +/- SE, %):

| Model | IDR (lower is better) | CPR (lower) | RTD (higher) | CLC (lower) |
|---|---|---|---|---|
| GPT-4.1 mini | 3.4 | 17.7 | 80.3 | 2.6 |
| Gemini 2.5 Flash Lite | 1.5 | 22.0 | 84.5 | 3.9 |
| Qwen-3.5-35B-A3B | 0.9 | 20.7 | 94.0 | 4.7 |
| Llama 3.1 8B | 10.1 | 40.3 | 62.6 | 4.9 |

Topology effects:

- RTD in multi-hop topologies (Table 21, n=45 per cell), in the order
  linear / branching / converging:
  - GPT-4.1 mini 75.9 / 77.4 / 49.4
  - Gemini 83.9 / 76.1 / 64.4
  - Qwen 97.4 / 91.1 / 81.7
  - Llama 48.3 / 49.3 / 20.7
  - Converging DAG is worst for all four models. (Column order is
    reconstructed from the PDF text extraction; it matches the body text.)
- Direct-routing topologies (fully connected, custom) keep RTD at about
  96-100% for GPT-4.1 mini, because they remove the multi-hop path.
- Per-hop tracer drop is 1.6x (Llama) to 5.0x (Qwen) higher at
  converging-DAG hops than at linear-chain hops. This is not explained by
  path length or fan-in.
- "Synthesis loss" (the tracer present in a parent, absent at the
  convergence node) is the largest failure class: 44% for GPT, 60% for
  Qwen, 61% for Llama.
- The construct check moves the expected way: IDR rises with peer pressure
  (rho = 0.211).
- Structural complexity tier does not predict IDR.

## Critique / open questions

- **ID verified**: 2605.08647 is this paper.
- The candidate summary's "constraint loss across handoffs" is partly
  right:
  - Handoff loss is measured with an exact-match *tracer string* (RTD), not
    semantic constraints. The trace audits do show constraints being dropped
    (e.g. a verified container image displaced at the convergence node).
  - "Instruction decay" (IDR) is a different thing. It measures an agent
    keeping its own system-prompt constraint under peer pressure, not
    constraint loss in transfer.
- No task-success correlation: the authors list this as a limitation.
  These are process diagnostics, and their predictive validity for outcomes
  is unestablished.
- IDR and CPR are LLM-judged (kappa about 0.69 vs humans).
- Only small or cheap backbones. Whether converging-node synthesis loss
  persists for frontier models is open. Qwen-3.5's 5.0x ratio suggests it
  is not purely a capacity effect.
- "Explicit constraint echoing at converging nodes" is proposed but not
  tested.
- 2x2 position: not about brief style. Its relevance is how constraints
  survive transfer, i.e. what a brief must carry and where.

## Trust signals

- Multi-institution student-heavy team (Utah, UMBC, Dhaka, UVA, BRAC and
  others).
- Preprint; Semantic Scholar lists only arXiv, with 3 citations (checked
  2026-11-14).
- Tasks, injection artifacts, judge prompts and scoring code are released.
  Human-validated tasks. Judge-backbone separation. Appropriate
  non-parametric statistics.
- **Credibility:** 3. Careful instrument with released artifacts and
  validation, but unreviewed, LLM-judged on two metrics, weak backbones, no
  outcome linkage.

## Follow-up

- **Relevance:** 3. Cite-worthy evidence on where constraints get lost in
  multi-agent transfer (convergence/synthesis nodes).
- **Guide:** P5 refines.
  - Context handed to a node that merges several parents is the weakest
    point.
  - A constraint arriving via one of N inputs is dropped at 1.6-5.0x the
    linear-chain per-hop rate.
  - Briefs to synthesizer or aggregator agents should restate
    load-bearing constraints explicitly, or route them directly. Fully
    connected and direct routing gave about 96-100% survival.
- **Guide:** P3 supports, weakly.
  - System-prompt constraints still decay under peer pressure (IDR
    0.9-10.1%).
  - This argues for enforcing hard invariants outside prose.
