---
kind: concept
name: "requirement-coverage"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/yang2025what]]"
  - "[[literature/papers/harada2025instructions]]"
  - "[[literature/papers/jaroslawicz2025instructions]]"
  - "[[literature/papers/liu2026espo]]"
  - "[[literature/papers/cemri2025why]]"
  - "[[literature/posts/hadfield2025multiagent]]"
  - "[[literature/posts/rajasekaran2025effective]]"
related_concepts:
  - "[[concepts/instruction-density-decay]]"
  - "[[concepts/brief-anatomy]]"
  - "[[concepts/cross-model-prompt-transfer]]"
  - "[[concepts/context-engineering]]"
related_experiments: []
tags: [briefing, specification, underspecification, instruction-design]
---

# requirement-coverage

## Definition

The share of requirements a brief states **that the reader would not meet by
default**. The variable is coverage of those requirements, not the length of the
brief. A requirement the reader already meets costs density when it is
stated. A requirement it won't meet costs accuracy when it is left out.

## Why it matters here

This is the axis that the terse-vs-verbose framing hides. The best-measured
source ([[literature/papers/yang2025what]]) finds:

- **Unstated requirements still mostly fail.** When a requirement is left out,
  its accuracy falls by 22.6% on average. Only 41.1% of unstated
  requirements still reach ≥98% accuracy. Format requirements are met
  unprompted 70.7% of the time; conditional ones only 22.9%.
- **Unstated requirements are what break across model changes.** Across model
  version updates within a family, 5.9% of unspecified requirements regress
  by more than 20%, against 3.0% of specified ones.
- **Stating everything also hurts.** With 19 requirements stated at once,
  gpt-4o meets each one 85.0% of the time on average, against 98.7% for a
  requirement stated alone. An optimizer that picks which requirements to
  state cut tokens by 41–45% and still gained accuracy. It mostly dropped
  requirements the model follows by default.

Other sources point the same way:

- **Compounding.** Satisfying all instructions at once compounds small
  per-instruction misses ([[literature/papers/harada2025instructions]]).
- **Length is a symptom.** Capping an optimizer's prompt length without
  diagnosing what to drop gave no accuracy
  ([[literature/papers/liu2026espo]]).
- **In multi-agent systems.** "Disobey task specification" accounts for 11.8%
  of failures. The fixes add explicit specification; none removes it
  ([[literature/papers/cemri2025why]]).
- **Orchestrators.** Left alone, Anthropic's orchestrator under-specified its
  subtasks ([[literature/posts/hadfield2025multiagent]]).

The practical rule:

- State the conditional and corner-case requirements.
- Leave out what the reader already does.
- Re-check unstated requirements whenever the model changes.

Evidence quality: Yang et al. score with LLM validators (95.6% agreement with
humans), not task outcomes, and test older models. ManyIFEval uses rule-based
checks.

## Connections

- [[concepts/instruction-density-decay]] is the cost on the other side.
- [[concepts/cross-model-prompt-transfer]]: unstated requirements are the
  fragile part.
- Hub `intent-level-briefing` ("context the author would otherwise take for
  granted").
