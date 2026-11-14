---
kind: concept
name: "brief-anatomy"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/posts/hadfield2025multiagent]]"
  - "[[literature/posts/openai2026gpt55]]"
  - "[[literature/posts/anthropic2026prompting]]"
  - "[[literature/posts/anthropic2026skill]]"
  - "[[literature/posts/rajasekaran2026harness]]"
  - "[[literature/papers/wang2026facts]]"
  - "[[literature/papers/kc2026handoff]]"
  - "[[literature/papers/jaroslawicz2025instructions]]"
  - "[[literature/papers/tomasev2026intelligent]]"
related_concepts:
  - "[[concepts/requirement-coverage]]"
  - "[[concepts/handoff-context-loss]]"
  - "[[concepts/degrees-of-freedom]]"
  - "[[concepts/commanders-intent]]"
related_experiments: []
tags: [briefing, delegation, subagents, instruction-design]
---

# brief-anatomy

## Definition

The fields a good brief carries. Sources agree on a core set:

- **objective / outcome**;
- **success criteria and stopping rule**;
- **output format / contract**;
- **boundaries and hard constraints**, with the reason for each;
- **context and sources**;
- **effort budget**.

## Why it matters here

- **Anthropic's fix.** Their multi-agent system fixed terse delegations with
  four fields: objective, output format, tool/source guidance and task
  boundaries. It added numeric effort budgets ("1 agent, 3–10 tool calls" up
  to ">10 subagents") ([[literature/posts/hadfield2025multiagent]]).
- **OpenAI's guidance.** Outcome, success criteria, constraints and context;
  "define success criteria and stopping rules"; avoid step-by-step process
  "unless the exact path matters" ([[literature/posts/openai2026gpt55]]).
- **Reasons.** Give the reason behind each instruction so the model can
  generalize ([[literature/posts/anthropic2026prompting]]).
- **Planners.** A planner briefed at deliverable level, not implementation,
  avoided under-scoping ([[literature/posts/rajasekaran2026harness]]).
- **Rules as imperatives.** Rules must travel as explicit operational
  imperatives, not soft discretion ([[literature/papers/wang2026facts]]).
- **Structure doesn't help on its own.** Structured handoff notes did not
  beat free-form ones ([[literature/papers/kc2026handoff]]). The fields
  matter more than the formatting.
- **Order.** Put critical constraints first; primacy bias peaks at 150–200
  instructions ([[literature/papers/jaroslawicz2025instructions]]).
- **Verifiable delegation.** Delegate only what can be verified: "contract-first"
  ([[literature/papers/tomasev2026intelligent]]).

All of this is vendor or practitioner guidance plus handoff studies. No
controlled study ablates the fields one at a time.

## Connections

- [[concepts/requirement-coverage]]: what goes in the constraints field.
- [[concepts/commanders-intent]]: purpose and end state.
