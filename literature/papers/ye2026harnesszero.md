---
kind: paper
title: "Harness-Zero: Harness Distillation via Agent-as-Harness"
authors: ["Haoran Ye", "Yuxing Lu", "Haonan Dong", "Zhaochen Su", "Guojie Song"]
institutions: ["Peking University", "Google", "The Hong Kong University of Science and Technology"]
year: 2026
venue: "arXiv preprint (cs.AI), v1 2026-09-21"
peer_reviewed: false
url: "https://arxiv.org/abs/2609.24974"
code_url: "https://github.com/metaevo-ai/harness-zero"
citations: null
source: "raw/papers/ye2026harnesszero.pdf"
added: "2026-11-14"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/durable-structure]]", "[[concepts/context-engineering]]"]
tags: [harness-distillation, agent-as-harness, sft, mini-swe-agent, appworld, spreadsheetbench, uspto, procedure-vs-knowledge]
---

# Harness-Zero: Harness Distillation via Agent-as-Harness

## TL;DR

The authors evolve a domain harness (tools, middleware, skills, memory) for
a small student, Qwen3.5-9B, on three domains. A harnessing agent (GPT-5.6
Sol) reads an adapted copy of that harness and corrects the student's
proposals step by step inside a minimal bash-only mini-SWE-agent harness.
The student is fine-tuned on those corrected trajectories, then deployed
with only the minimal harness. Macro task success goes from 23.3% to 44.3%
(+21.0), beating the base model *with* the evolved harness (41.7%). Behavior
that encodes **procedure** transfers into weights. Domain **knowledge and
tools** (chemistry) do not fully transfer: 30.0% vs 38.0%. In inference-only
runs with frontier models, the evolved harness barely helped them on
procedural domains but added +16 on chemistry.

## Claims

- Harness gains can be moved from the scaffold into the weights, so the
  specialized harness can be removed at deployment.
- Agent-as-harness, where an LLM reviewer applies the harness guidance,
  beats code-as-harness for frontier models (81.1% vs 78.1% average).
- "Procedural harness behavior is easier to internalize than deep domain
  knowledge."
- Effective review needs a capable reviewer. With weak reviewer models,
  review becomes harmful.

## Methods

- Domains and splits: SpreadsheetBench Verified (300 train / 100 test),
  AppWorld (147 train / 56 three-task test scenarios from test_normal), and
  USPTO-50k-style retrosynthesis (500 train / 100 test). Metrics are pass@1,
  or scenario goal completion for AppWorld. These are **task-outcome
  metrics** from benchmark verifiers. All single runs (seed 42), no CIs.
- The target harness h is mini-SWE-agent-style: fixed system prompt, one
  Bash tool. The evolved harness h⋆ comes from three rounds of
  failure-analysis evolution by Kimi K3 under Kimi Code, in DeepAgents
  format. It is adapted into a private reviewer reference K.
- Distillation: 487 / 282 / 500 retained rollouts, LoRA SFT on Qwen3.5-9B
  for 2 epochs (Tinker recipe). Reasoning is on, at high effort, for all
  models.

## Results

- **Distillation (Table 2), Qwen3.5-9B.** Spreadsheet / AppWorld / USPTO /
  average:
  - base under h: 31.0 / 26.8 / 12.0 / **23.3**
  - base + evolved h⋆: 39.0 / 48.2 / 38.0 / **41.7**
  - distilled under h: 44.0 / 58.9 / 30.0 / **44.3**
  - General-purpose harnesses *hurt* the 9B model. DeepAgents averages 20.5
    and Claude Code 15.9, against 23.3 for the minimal harness.
- **Frontier models, no training (Table 1).** Columns are mini-SWE-agent h →
  evolved h⋆ (code) → reviewer with K. GPT-5.6 Sol: Spreadsheet 83 → 84 →
  88, AppWorld 96.4 → 94.6 → 96.4, **USPTO 50 → 66 → 67**. DeepSeek-V4-Pro:
  76 → 77 → 86, 75 → 91.1 → 89.3, 31 → 56 → 60. A reviewer with an *empty*
  K averages 69.2 vs 68.6 for h alone, so the gain comes from the harness
  content, not from review as such.
- Ablation on USPTO (Table 3). Fine-tuning on teacher rollouts gives 12.0,
  no gain over base, even though those rollouts succeed 52% of the time.
  Teacher rollouts under h⋆ give 3.0. Review with oracle answers gives 15.0.
  Harness-guided review gives 30.0.
- 82.3% average recovery of 28 harness-exclusive behavior patterns (e.g.
  "inspect before editing", "validate with RDKit"). AppWorld recovery is
  lowest, at 40–73% per pattern.
- Appendix F: the advantage of reviewer over code harness tracks reviewer
  capability. It is +1.0 for GPT-5.6 Sol, +4.0 for DeepSeek-V4-Pro, −1.0 for
  DeepSeek-V4-Flash and −12.0 for Qwen3.6-35B-A3B.

## Critique / open questions

- **The procedure vs knowledge split is the key result for this project.**
  For the strongest model (GPT-5.6 Sol), an evolved harness that mostly
  encodes procedure (inspect, edit, verify on spreadsheets and apps) added
  about 0 to +1. One that also carried domain knowledge and a validation tool
  (reaction priors, candidate generation, RDKit checks) added +16. The same
  split shows up in distillation: procedure was absorbed into weights, but
  knowledge and tooling were not. Read through the research plan, procedure
  is what a strong reader can work out, and knowledge or tools are context it
  lacks.
- **Confounds.** h⋆ was evolved on the 9B student and reused unchanged for
  the frontier models, so it may under-serve them. Test sets are small (56
  AppWorld scenarios, 100 tasks elsewhere), runs are single, and there are no
  CIs, so ±5-point differences are within noise. Harness evolution and the
  reviewer both use frontier models, so "distillation" also transfers
  frontier-model judgment.
- **2×2 position.** h⋆ is mostly *enforced* procedure (middleware) plus
  skills and memory, i.e. verbose procedure with knowledge. The minimal
  target harness is a terse fixed prompt (mini-SWE-agent's own prompt
  includes a short recommended workflow). The paper doesn't vary instruction
  style. It varies where the structure lives: code, a reviewer agent, or
  weights.
- Context management was "not fully expressible as student responses", and
  the authors say the method "does not remove the need for a harness, but
  narrows what that harness must provide".
- **Provenance vs the candidate (Arize blog):** the blog's numbers check out
  against the primary text. +21 is the macro-average (23.3 → 44.3), beating
  the full harness's 41.7. "Trails by 8 on chemistry" is USPTO 30.0 vs 38.0.
  Context management not fully transferring is in the Limitations. The blog
  itself was not ingested.

## Trust signals

- **Credibility:** 3. Peking University State Key Lab group, code released
  (metaevo-ai/harness-zero), task-outcome metrics on three public benchmarks,
  informative ablations including an oracle-answer control. Not peer
  reviewed, single runs on small test sets with no CIs, and the evolved
  harness was tuned for the student and reused for frontier models.

## Follow-up

- **Relevance:** 4. It separates which harness content strong models still
  need (domain knowledge and tools) from what they don't (procedure), with
  task-outcome numbers. This is directly on Q2 and P4.
- **Guide:** P4 refines. Structure that carries knowledge or tools still
  helped the strongest model (+16 on USPTO). Procedural structure added about
  nothing for it on spreadsheets and AppWorld. That supports the line's
  "carries knowledge" qualifier and counts against keeping procedure for
  strong readers.
- **Guide:** P1 supports. Procedure was what strong models didn't need and
  small models could absorb. Knowledge was what both lacked.
- **Guide:** P5 supports. The hard-to-transfer part was domain context and
  tooling, not method.
- Related: qian2026ai4ai (test-time strong-to-weak harness),
  SWE-agent-mini-swe-agent (the target harness).
