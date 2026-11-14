---
kind: concept
name: "scaffold-absorption"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/posts/rajasekaran2026harness]]"
  - "[[literature/repos/SWE-agent-mini-swe-agent]]"
  - "[[literature/papers/ye2026harnesszero]]"
  - "[[literature/papers/rodionov2026improving]]"
  - "[[literature/papers/starace2026scaffold]]"
  - "[[literature/papers/dennis2026incontext]]"
  - "[[literature/posts/openai2026gpt55]]"
  - "[[literature/papers/meincke2025prompting]]"
related_concepts:
  - "[[concepts/durable-structure]]"
  - "[[concepts/guidance-distraction]]"
  - "[[concepts/cross-model-prompt-transfer]]"
related_experiments: []
tags: [scaffolding, harness, bitter-lesson, capability]
---

# scaffold-absorption

## Definition

As models get stronger, harness components that do **procedural** work for
the model stop paying for themselves and can be removed. Examples are
decomposition, context resets, scripted flow control and custom tools. In
the harness-design post's words, "every component in a harness encodes an
assumption about what the model can't do on its own"
([[literature/posts/rajasekaran2026harness]]).

## Why it matters here

This is the Bitter Lesson version of the project thesis. The evidence comes
in three kinds.

**Removal across model generations:**

- **Anthropic's long-running harness.** Context resets were dropped at Opus
  4.5 and sprint decomposition at 4.6. The planner and a final evaluator
  stayed ([[literature/posts/rajasekaran2026harness]]).
- **mini-swe-agent.** A ~100-line bash-only agent comes within ~2–3 points of
  the best custom scaffolds for Opus 4.5 and Gemini 3 Pro, but trails by ~10
  for Claude 4 Sonnet. Even this "minimal" prompt keeps a 5-step workflow and
  a strict submission protocol ([[literature/repos/SWE-agent-mini-swe-agent]]).

**Controlled removal:**

- **Harness-Zero.** Without training, an evolved harness added ~0 to GPT-5.6
  Sol on procedure-heavy domains. It added +16 where it also carried domain
  knowledge and a validation tool ([[literature/papers/ye2026harnesszero]]).
- **Rodionov.** The gap between a task-specific reference agent and a generic
  one shrinks with capability: 18.3 → 6.9 points
  ([[literature/papers/rodionov2026improving]]).
- **Who enforces the procedure.** Code feeding a script to the model node by
  node did worse than the same script held whole in the prompt (Sonnet 4.5,
  judge metric; [[literature/papers/dennis2026incontext]]). This tests who
  enforces a procedure, not script vs intent.

**Counter-evidence:**

- **GAIA.** Structured scaffolds help Anthropic models at L2 by 14 points
  (primary slice). That is model-run planning and verification, not
  author-written procedure, and GPT-5.5, which has the highest ReAct baseline
  of the five models, gained least ([[literature/papers/starace2026scaffold]]).

Absorption is real for procedure. It does not extend to structure that carries
knowledge, tools or verification ([[concepts/durable-structure]]).

## Connections

- Vendor guidance tells authors to restart from the smallest working prompt on
  each model change ([[literature/posts/openai2026gpt55]]).
- [[concepts/cross-model-prompt-transfer]]: what gets absorbed differs by model
  family.
