---
kind: moc
name: "brief-writing"
status: active
added: "2026-11-14"
concepts:
  - "[[concepts/requirement-coverage]]"
  - "[[concepts/brief-anatomy]]"
  - "[[concepts/degrees-of-freedom]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/instruction-density-decay]]"
  - "[[concepts/guidance-distraction]]"
  - "[[concepts/llm-authored-instructions]]"
tags: [moc, brief-writing, instruction-design, briefing]
---

# brief-writing

What should a brief for a strong reader contain, and what does each extra
line cost? These concepts hold the evidence behind guide principles P1, P2 and
P6 (`docs/writing-guide.md`). The first curate pass found the live variable
is **coverage of requirements the reader won't meet by default**, not brief
length or intent-vs-script style.

## What goes in

- [[concepts/requirement-coverage]]: state the conditional and corner-case
  requirements; leave out defaults. Anchor:
  [[literature/papers/yang2025what]].
- [[concepts/brief-anatomy]]: the fields that recur across vendor and
  handoff evidence. These are outcome, success criteria and stopping rule,
  output contract, constraints with reasons, context, and budget. Anchors:
  [[literature/posts/hadfield2025multiagent]] and
  [[literature/posts/openai2026gpt55]].
- [[concepts/context-engineering]]: the smallest high-signal set;
  "minimal does not necessarily mean short". Anchor:
  [[literature/posts/rajasekaran2025effective]].

## How specific to be

- [[concepts/degrees-of-freedom]]: match specificity to how fragile the task
  is. A step sequence is right when order or completeness is itself a
  requirement. Anchor: [[literature/posts/anthropic2026skill]].
- [[concepts/guidance-distraction]]: literal demos and imposed formats can
  pull a reader off its own better strategy. This is measured mostly on small
  models and math. Anchor: [[literature/papers/wang2025harm]].

## What prose costs

- [[concepts/instruction-density-decay]]: joint compliance compounds small
  misses, and frontier readers have a higher ceiling. Anchors:
  [[literature/papers/harada2025instructions]] and
  [[literature/papers/jaroslawicz2025instructions]].
- [[concepts/llm-authored-instructions]]: model-written instructions tend to
  restate what the reader can discover, and they grow rules when a loop
  rewards patching. A held-out eval loop makes them safe. Anchor:
  [[literature/papers/gloaguen2026evaluating]].

## Open thread

No source runs the controlled comparison the project most needs: a goal-only
brief against a procedural brief with **equal requirement coverage**, on
agentic tasks, scored by task outcome. Every study in hand changes coverage
and style together. Separate theme, not yet ripe for its own MoC:
harness structure ([[concepts/scaffold-absorption]],
[[concepts/durable-structure]], [[concepts/invariants-in-code]]).
