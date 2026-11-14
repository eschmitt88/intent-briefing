---
kind: concept
name: "llm-authored-instructions"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/gloaguen2026evaluating]]"
  - "[[literature/papers/zhu2026sage]]"
  - "[[literature/papers/liu2026espo]]"
  - "[[literature/papers/shi2025loss]]"
  - "[[literature/papers/gong2026prompt]]"
  - "[[literature/posts/aizawa2025writing]]"
  - "[[literature/posts/hadfield2025multiagent]]"
  - "[[literature/papers/qian2026ai4ai]]"
  - "[[literature/posts/anthropic2026skill]]"
related_concepts:
  - "[[concepts/instruction-density-decay]]"
  - "[[concepts/cross-model-prompt-transfer]]"
  - "[[concepts/requirement-coverage]]"
related_experiments: []
tags: [author-bias, prompt-optimization, context-files, q5]
---

# llm-authored-instructions

## Definition

How instructions written by a model (context files, optimizer-grown prompts,
orchestrator briefs, tool descriptions) differ in quality from instructions
written by humans, and why. This bears on research question Q5 (author bias).

## Why it matters here

The founding claim was that LLM-written files hurt. **It doesn't survive the
full text.**

- **AGENTS.md.** In the current version, neither LLM-generated nor
  developer-written context files significantly change success
  ([[literature/papers/gloaguen2026evaluating]]):
  - LLM-generated vs none: −0.5 points (p=0.87) on SWE-bench Lite and −1.8
    (p=0.37) on CTXbench.
  - Developer-written vs LLM-generated: +4.2 points (p=0.038).
  - LLM-generated files add ~20–23% cost.
  - The comparison is uncontrolled: the human arm is 12 files. With repo docs
    removed, the LLM-generated files *help* (+2.7). The driver looks like
    **redundancy with documentation the reader can already find**, not
    authorship.
- **Iteration loops grow prompts.**
  - SAGE's own generator grew prompts to ~12K tokens without a test gain; it
    is told to write if-then rules and keep every old rule
    ([[literature/papers/zhu2026sage]]).
  - GEPA's prompts run 1.87× longer than ESPO's for less accuracy, but
    capping their length blindly didn't help
    ([[literature/papers/liu2026espo]]).
  - The most rule-heavy optimized prompt transferred worst to other models
    ([[literature/papers/shi2025loss]]).
  - Observational DSPy analysis: added meta-instructions ("ensure", "do
    not") correlate with lower math accuracy
    ([[literature/papers/gong2026prompt]], weak).
- **Counter-evidence: LLM authors can do well.**
  - Claude-optimized tool servers beat human-written ones on held-out tasks:
    Slack 67.4 → 80.1 ([[literature/posts/aizawa2025writing]]).
  - Orchestrators *under*-specified subtasks
    ([[literature/posts/hadfield2025multiagent]]).
  - Builder models used less code when building for a stronger target
    ([[literature/papers/qian2026ai4ai]]).

Current reading:

- LLM authors don't systematically over-script.
- They accumulate rules when an iteration loop rewards patching failures.
- They restate what the reader could discover for itself.
- A held-out eval loop is what makes LLM authorship safe.

## Connections

- [[concepts/instruction-density-decay]]: the cost when rules accumulate.
- [[concepts/requirement-coverage]]: diagnose which requirements to state;
  don't just trim.
