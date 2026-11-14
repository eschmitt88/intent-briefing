---
kind: concept
name: "cross-model-prompt-transfer"
status: seedling
added: "2026-11-14"
sources:
  - "[[literature/papers/shi2025loss]]"
  - "[[literature/papers/yang2025what]]"
  - "[[literature/papers/barbaste2026harness]]"
  - "[[literature/posts/openai2026gpt55]]"
  - "[[literature/posts/anthropic2026prompting]]"
  - "[[literature/papers/starace2026scaffold]]"
  - "[[literature/papers/gong2026prompt]]"
related_concepts:
  - "[[concepts/requirement-coverage]]"
  - "[[concepts/scaffold-absorption]]"
  - "[[concepts/llm-authored-instructions]]"
related_experiments: []
tags: [transfer, model-migration, prompt-optimization]
---

# cross-model-prompt-transfer

## Definition

How well an instruction tuned for one model keeps its value on another model,
or on a newer version of the same one.

## Why it matters here

claude-system's skills and briefs outlive any single model.

- **Optimized prompts lose part of their gain on other models.** Prompts
  optimized on DeepSeek-V3 gained +16.7 there, but only +7.2 on Llama-3.3 and
  +5.9 on GPT-4.1. The most rule-heavy prompt transferred worst
  ([[literature/papers/shi2025loss]]).
- **Unstated requirements break first.** Across version updates, unspecified
  requirements regress about twice as often as specified ones
  ([[literature/papers/yang2025what]]).
- **Harness behaviour depends on model family.** Harnesses ship per-family
  prompts (OpenCode has 9) ([[literature/papers/barbaste2026harness]]).
  Scaffold sensitivity is moderated by family more than by tier
  ([[literature/papers/starace2026scaffold]]).
- **Vendors say restart, not port.** Begin from the smallest prompt that
  works ([[literature/posts/openai2026gpt55]]). Emphasis tuned for older
  models over-triggers on newer ones
  ([[literature/posts/anthropic2026prompting]]).
- **No direct test yet.** No source in hand measures transfer across backbones
  directly (the candidate claim about [[literature/papers/gong2026prompt]]
  did not hold).

The practical rule:

- Treat a model change as a reason to re-test.
- Make the requirements explicit ([[concepts/requirement-coverage]]).
- Keep model-specific emphasis out of the shared text.

## Connections

- [[concepts/scaffold-absorption]]: what a new model absorbs is one reason
  transfer is partial.
