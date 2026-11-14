---
kind: concept
name: "guidance-distraction"
status: seedling
added: "2026-11-14"
sources:
  - "[[literature/papers/wang2025harm]]"
  - "[[literature/papers/pushkin2026soft]]"
  - "[[literature/papers/zheng2025curse]]"
  - "[[literature/papers/meincke2025prompting]]"
  - "[[literature/papers/khan2025prompting]]"
  - "[[literature/papers/li2025thinking]]"
  - "[[literature/papers/gloaguen2026evaluating]]"
related_concepts:
  - "[[concepts/scaffold-absorption]]"
  - "[[concepts/degrees-of-freedom]]"
related_experiments: []
tags: [prompting, chain-of-thought, few-shot, reasoning-models]
---

# guidance-distraction

## Definition

Prescriptive guidance can pull a capable reader off a better strategy of its
own. The guidance here means literal worked examples, imposed reasoning
formats, or extra prose the reader faithfully follows. The guidance is not
wrong; the harm is in how the reader adopts it.

## Why it matters here

This is the proposed mechanism behind "brief, don't script" (guide P1). The
evidence is **weaker and narrower than the founding notes implied**:

- **Literal demos.** Few-shot reasoning traces hurt small open reasoning
  models: −6 to −16 points on AIME'25 with one demo, and up to −35 with
  three. The proposed fix ("abstracted insights") loses most of its gain once
  compute is matched by majority voting
  ([[literature/papers/wang2025harm]]).
- **Mid-size models.** The penalty for imposed demos is clear for one 7B math
  model only ([[literature/papers/pushkin2026soft]]).
- **Chain of thought.** CoT underperforms direct answering on pattern-based
  in-context learning ([[literature/papers/zheng2025curse]]). For reasoning
  models, CoT prompting gives about ±0.03, at a real time cost
  ([[literature/papers/meincke2025prompting]]).
- **Instruction-following.** CoT lowers instruction-following scores mainly
  below the frontier; it costs ≤1 point for the strongest models tested
  ([[literature/papers/li2025thinking]]).
- **Prose files.** Agents follow context files faithfully, which widens
  exploration and adds ~20% cost without raising success
  ([[literature/papers/gloaguen2026evaluating]]).
- **Excluded anecdote.** The "guardrail-to-handcuff" result has integrity
  problems ([[literature/papers/khan2025prompting]]) and is kept as an
  anecdote only.

No source shows this distraction for frontier models on agentic tasks. Treat
the concept as plausible, measured mostly on small models and math.

## Connections

- [[concepts/scaffold-absorption]]: the capability trend this is meant to
  explain.
- [[concepts/degrees-of-freedom]]: the authoring answer (loosen guidance where
  the reader's own strategy is better).
