---
kind: concept
name: "degrees-of-freedom"
status: seedling
added: "2026-11-14"
sources:
  - "[[literature/posts/anthropic2026skill]]"
  - "[[literature/posts/rajasekaran2025effective]]"
  - "[[literature/papers/wang2025harm]]"
  - "[[literature/papers/qian2026ai4ai]]"
  - "[[literature/papers/tomasev2026intelligent]]"
  - "[[literature/repos/SWE-agent-mini-swe-agent]]"
related_concepts:
  - "[[concepts/guidance-distraction]]"
  - "[[concepts/brief-anatomy]]"
  - "[[concepts/invariants-in-code]]"
related_experiments: []
tags: [skills, specificity, fragility, instruction-design]
---

# degrees-of-freedom

## Definition

Set how specific an instruction is by how **fragile and variable** the task
is:

- High freedom (goal only) where many paths succeed.
- Low freedom ("run exactly this script") where one wrong step breaks the
  task.

The term comes from Anthropic's skill guidance
([[literature/posts/anthropic2026skill]]).

## Why it matters here

The project's 2x2 asks which cell to use. This concept answers "it depends
on the task, not only on the reader."

- **Altitude.** Context engineering names the same idea: neither brittle
  if-else logic nor vague guidance that "falsely assumes shared context"
  ([[literature/posts/rajasekaran2025effective]]).
- **Strict vs open delegation.** Strict-spec execution and open-ended
  delegation are distinct modes, and only outcomes that can be verified should
  be delegated ([[literature/papers/tomasev2026intelligent]], position paper).
- **Weak readers.** Weaker readers gain from structure the author compiles
  into code ([[literature/papers/qian2026ai4ai]]). Strong readers can be
  pulled off course by literal demos ([[literature/papers/wang2025harm]]).
- **Minimal harnesses still have low-freedom parts.** Even the minimal
  harness keeps its submission protocol at low freedom
  ([[literature/repos/SWE-agent-mini-swe-agent]]).
- **Unmeasured.** No source measures the fragility rule directly; it is
  vendor guidance.

## Connections

- [[concepts/invariants-in-code]]: the lowest-freedom cases belong in code.
- [[concepts/guidance-distraction]]: the cost of too little freedom.
