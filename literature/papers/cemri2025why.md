---
kind: paper
title: "Why Do Multi-Agent LLM Systems Fail?"
authors: ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Aditya Parameswaran", "Dan Klein", "Kannan Ramchandran", "Matei Zaharia", "Joseph E. Gonzalez", "Ion Stoica"]
institutions: ["UC Berkeley", "Intesa Sanpaolo"]
year: 2025
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
peer_reviewed: true
url: "https://arxiv.org/abs/2503.13657"
code_url: "https://github.com/multi-agent-systems-failure-taxonomy/MAST"
citations: 878
source: "raw/papers/cemri2025why.pdf"
added: "2026-11-14"
relevance: 3
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/requirement-coverage]]", "[[concepts/durable-structure]]"]
tags: [multi-agent, failure-taxonomy, MAST, verification, specification]
---

# Why Do Multi-Agent LLM Systems Fail?

## TL;DR

MAST is a 14-mode, 3-category taxonomy of multi-agent failures. It was built
by grounded-theory analysis of 150 traces and applied with an o1-based LLM
annotator to MAST-Data: 1,642 traces from 7 MAS frameworks.
System-design failures, including disobeying task or role specifications,
are the largest category. Workflow and topology changes help more than
prompt edits.

## Claims

- MAS failure rates of 41% to 86.7% on 7 open-source MAS.
- Failures cluster into System Design Issues (FC1), Inter-Agent
  Misalignment (FC2) and Task Verification (FC3).
- Many failures come from organizational and system design, not only
  base-model limits. With the same model, redesigns gain up to +15.6%.
- Communication-protocol fixes (MCP, A2A) don't address FC2. The paper
  frames it as a "theory of mind" failure: agents don't model what other
  agents need to know.

## Methods

- Grounded theory over 150 traces (>15k lines each) from 5 frameworks:
  HyperAgent, AppWorld, AG2, ChatDev, MetaGPT. Six expert annotators, over
  20 hours each.
- Three IAA rounds on 15 traces, Cohen's kappa = 0.88.
- LLM annotator: o1 with few-shot examples. Accuracy 0.94, kappa = 0.77
  against humans; kappa = 0.79 on two unseen MAS.
- MAST-Data: 1,642 traces across 7 MAS (adds Magentic-One and OpenManus)
  on ProgramDev, SWE-Bench Lite, AppWorld Test-C, GSM-Plus, GAIA, etc.
  Models: GPT-4/4o, Claude 3.7 Sonnet, plus Qwen2.5 and CodeLlama.
  Prevalence is LLM-annotated.
- Intervention case studies (App. H): AG2 MathChat on 200 GSM-Plus problems
  with 6 repetitions, and ChatDev on ProgramDev-v0 (32 tasks) and
  HumanEval.

## Results

Prevalence over 1,642 traces (Fig. 1). Mode shares add up to the category
totals.

- **FC1 System Design Issues: 44.2%**
  - FM-1.1 disobey task specification 11.8%
  - FM-1.2 disobey role specification 1.5%
  - FM-1.3 step repetition 15.7%
  - FM-1.4 loss of conversation history 2.8%
  - FM-1.5 unaware of termination conditions 12.4%
- **FC2 Inter-Agent Misalignment: 32.3%**
  - FM-2.1 conversation reset 2.2%
  - FM-2.2 fail to ask for clarification 6.8%
  - FM-2.3 task derailment 7.4%
  - FM-2.4 information withholding 0.8%
  - FM-2.5 ignored other agent's input 1.9%
  - FM-2.6 reasoning-action mismatch 13.2%
- **FC3 Task Verification: 23.5%**
  - FM-3.1 premature termination 6.2%
  - FM-3.2 no or incomplete verification 8.2%
  - FM-3.3 incorrect verification 9.1%

Other category splits appear in the paper:

- Fig. 4, a 210-trace human-evaluated subset (7 MAS x 30): FC1 41.8%, FC2
  36.9%, FC3 21.3%.
- Fig. 2 still shows earlier-version shares: 37.17 / 31.41 / 31.41.

Interventions (Table 5, task success):

- AG2/GSM-Plus, GPT-4: 84.75 baseline, 89.75 improved prompt, 85.50 new
  topology.
- AG2/GSM-Plus, GPT-4o: 84.25, 89.00, 88.83 (p = 0.03).
- ChatDev ProgramDev-v0: 25.0 baseline, 34.4 with role-spec and hierarchy
  fix (the "+9.4%"), 40.6 with cyclic topology and CTO verification (the
  "+15.6%").
- ChatDev HumanEval: 89.6, 90.3, 91.5.

Model and design comparisons:

- MetaGPT with GPT-4o has 39% fewer FC1 failures than with Claude 3.7.
- MetaGPT has 60-68% fewer FC1/FC2 failures than ChatDev, but 1.56x more
  FC3.

## Critique / open questions

- **Trace-count discrepancy settled.** Both candidate summaries are right
  for different versions:
  - v1 (Mar 2025) analysed "5 MAS frameworks across over 150 tasks".
  - v3 (Oct 2025, the NeurIPS 2025 D&B camera-ready) adds MAST-Data, 1,642
    traces across 7 frameworks.
  - The taxonomy itself is still built from the 150 traces.
  - Cite 1,642/7 for prevalence and 150 for taxonomy construction.
- **Specification failures: under-specification, not over-specification.**
  - FM-1.1/1.2 are defined as *failure to adhere* to stated task or role
    constraints, i.e. non-compliance.
  - The authors trace them to three causes: (1) MAS design of roles and
    workflow, (2) poor or ambiguous user prompt specification, (3) LLM
    limits.
  - FM-2.2 (fail to ask for clarification, 6.8%) is the under-spec handling
    failure.
  - Nothing in the taxonomy measures over-specification.
  - The fixes *add* explicit role and verification specification and gain.
  - However, the Wordle example shows a *more* explicit prompt still failing
    in ChatDev. The authors read this as a design problem, not one solved
    by more prompt text.
  - v1 called the category "Specification and system design failures";
    v3 renamed it "System Design Issues".
- Prevalence is LLM-judged (o1, kappa 0.77). Human annotation covers only
  the 150-trace development set and IAA subsets. Task success in the
  interventions is a task outcome, but the samples are small (32 ProgramDev
  tasks, a single run).
- The models are older (GPT-4/4o, Claude 3.7 Sonnet). The frameworks are
  rigid role-play MAS (ChatDev, MetaGPT), not frontier orchestrator-subagent
  setups.
- 2x2 position: not about brief style. The interventions mix procedure
  (verification steps, a termination rule) with structure (topology). Its
  relevance is the handoff and verification failure classes, and evidence
  that structure carrying verification and termination rules pays off.

## Trust signals

- UC Berkeley Sky lab (Stoica, Zaharia, Gonzalez, Klein).
- NeurIPS 2025 D&B (peer-reviewed). Code, MAST-Data and the annotator are
  released (`pip install agentdash`).
- Semantic Scholar citations: 878 (checked 2026-11-14).
- **Credibility:** 4. Peer-reviewed, high-agreement taxonomy, open data and
  code, heavily cited. Prevalence relies on an LLM annotator, and the
  intervention samples are small.

## Follow-up

- **Relevance:** 3. Cite-worthy prior art on handoff and verification
  failures and the role of specifications in MAS. It isn't a test of brief
  vs script.
- **Guide:** P5 supports.
  - FC2 (32.3%) is largely about information failing to cross agent
    boundaries: withholding, ignored input, failure to ask, and the
    "theory of mind" gap.
- **Guide:** P4 supports.
  - Explicit verification and termination structure gives the biggest gain
    (ChatDev 25.0 to 40.6).
  - Verifiers that only do superficial checks are common (FM-3.2/3.3 = 17.3%).
- Use the MAST mode list as a checklist vocabulary for subagent-brief
  failure audits.
