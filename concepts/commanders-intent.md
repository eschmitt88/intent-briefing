---
kind: concept
name: "commanders-intent"
status: seedling
added: "2026-11-14"
sources:
  - "[[literature/papers/thomas2007interpreting]]"
  - "[[literature/posts/yan2025multiagents]]"
  - "[[literature/posts/anthropic2026prompting]]"
related_concepts:
  - "[[concepts/handoff-context-loss]]"
  - "[[concepts/brief-anatomy]]"
related_experiments: []
tags: [mission-command, human-delegation, analogy]
---

# commanders-intent

## Definition

The mission-command doctrine: the commander states the purpose and desired
end state, and subordinates choose the method. It is the human model behind
the project's intent-brief thesis.

## Why it matters here

The analogy is in the research plan, but its empirical base in the corpus is
**thin**.

- **Measured, but confounded.** Staff understanding of intent was measured
  with true/false probes. The run with degraded tools scored better than the
  run with full tools (d' 1.35 vs 0.49). The runs differed in personnel, so
  the cause can't be isolated. In the better run, one person's job was to
  relay the intent ([[literature/papers/thomas2007interpreting]]).
- **Shattuck & Woods (2000) is not in the graph.** Its chapter is paywalled,
  so it was declined at curation. A secondary reproduction reports that 11 of
  32 episodes (34%) matched intent. The successful subordinates first
  established force dispositions and consulted the intent statement.
- **Vendor guidance.** "Give the reason behind instructions" is the vendor
  form of stating purpose ([[literature/posts/anthropic2026prompting]]).
- **Limit of the analogy.** Cognition's coupled-writes argument marks where it
  stops: intent alone can't coordinate parallel actors
  ([[literature/posts/yan2025multiagents]]).

The doctrine assumes shared doctrine and trained subordinates. In this
project, that means CLAUDE.md, rules and skills being present for the reader.

## Connections

- [[concepts/handoff-context-loss]]: what the doctrine is supposed to solve.
- [[concepts/brief-anatomy]]: purpose and end state as brief fields.
