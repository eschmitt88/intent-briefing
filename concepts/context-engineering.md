---
kind: concept
name: "context-engineering"
status: seedling
added: "2026-11-14"
sources:
  - "[[literature/posts/rajasekaran2025effective]]"
  - "[[literature/papers/gloaguen2026evaluating]]"
  - "[[literature/papers/kc2026handoff]]"
  - "[[literature/papers/yu2026when]]"
  - "[[literature/papers/zhu2026sage]]"
  - "[[literature/papers/ye2026harnesszero]]"
  - "[[literature/posts/anthropic2026skill]]"
related_concepts:
  - "[[concepts/requirement-coverage]]"
  - "[[concepts/handoff-context-loss]]"
  - "[[concepts/degrees-of-freedom]]"
related_experiments: []
tags: [context, compaction, progressive-disclosure]
---

# context-engineering

## Definition

Curating "the smallest set of high-signal tokens" a model needs for a task.
That covers the system prompt, tools, examples, retrieved state, compaction
and sub-agent summaries ([[literature/posts/rajasekaran2025effective]]).
"Minimal does not necessarily mean short."

## Why it matters here

This is the vendor vocabulary for the project's coverage-not-length finding.

- **Redundant context costs.** Content the reader can discover itself adds
  cost without adding success ([[literature/papers/gloaguen2026evaluating]]).
- **What context is worth passing.** In handoffs, context mostly saves the
  successor's effort; full traces carry the decision-relevant residue
  ([[literature/papers/kc2026handoff]]). Pass the evidence behind decisions,
  not just the decided fields ([[literature/papers/yu2026when]]).
- **Accumulated rules.** They grow context without signal
  ([[literature/papers/zhu2026sage]]).
- **Context is hard to distil.** Of the evolved harness's functions, context
  management transferred least well into weights
  ([[literature/papers/ye2026harnesszero]]).
- **Progressive disclosure.** Skills load detail only when needed
  ([[literature/posts/anthropic2026skill]]).

## Connections

- [[concepts/requirement-coverage]]: which tokens are high-signal.
- [[concepts/handoff-context-loss]]: compaction as a lossy relay.
