---
kind: concept
name: "durable-structure"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/ye2026harnesszero]]"
  - "[[literature/papers/starace2026scaffold]]"
  - "[[literature/posts/rajasekaran2026harness]]"
  - "[[literature/papers/cemri2025why]]"
  - "[[literature/papers/palumbo2026formal]]"
  - "[[literature/posts/hughes2026claude]]"
  - "[[literature/papers/rodionov2026improving]]"
  - "[[literature/repos/SWE-agent-mini-swe-agent]]"
  - "[[literature/papers/barbaste2026harness]]"
related_concepts:
  - "[[concepts/scaffold-absorption]]"
  - "[[concepts/invariants-in-code]]"
related_experiments: []
tags: [scaffolding, harness, verification, enforcement]
---

# durable-structure

## Definition

Structure that keeps paying off as models get stronger. It does one of three
things the model can't supply from its own capability:

- **Carries knowledge** the model lacks: domain facts, validation tools.
- **Enforces invariants** the model must not violate.
- **Verifies** work at the edge of what the model can do reliably on its own.

## Why it matters here

This is the counterpart to [[concepts/scaffold-absorption]], and the reason
guide P4 is not just "delete the harness".

- **Knowledge and tools.** For a strong model, Harness-Zero added +16 on
  chemistry, where it carried domain knowledge and a validation tool. It added
  ~0 on procedure-heavy domains ([[literature/papers/ye2026harnesszero]]).
- **Verification.**
  - In MAST, adding verification gave the largest gain: ChatDev success went
    25.0 → 40.6 with a topology change plus verification
    ([[literature/papers/cemri2025why]]).
  - Anthropic kept an evaluator, which is worth its cost only "when the task
    sits beyond what the current model does reliably solo"
    ([[literature/posts/rajasekaran2026harness]]).
  - Planning and verifier loops helped on GAIA L2, but the effect depends on
    model family ([[literature/papers/starace2026scaffold]]).
- **Enforcement.**
  - Runtime policy checks beat prompt-only policies
    ([[literature/papers/palumbo2026formal]]).
  - Claude Code keeps a deterministic allowlist under its classifier
    ([[literature/posts/hughes2026claude]]).
  - Moving a reset rule from prose into a controller closed 34–60% of a gap
    for a frontier model ([[literature/papers/rodionov2026improving]]).
- **Field practice.** Across eleven coding harnesses, safety controls and
  context management persist, and behavioural policy is moving from prompt
  text into configuration ([[literature/papers/barbaste2026harness]]).
- **Output contracts.** mini-swe-agent dropped its custom tools but kept a
  strict submission protocol ([[literature/repos/SWE-agent-mini-swe-agent]]).

Test each component by asking whether it carries knowledge, enforcement or
verification the current model lacks. If it only sequences work the model
could sequence itself, expect it to be absorbed. Re-test the answer on each
model change.

## Connections

- [[concepts/invariants-in-code]] covers the enforcement subset.
- Hub `typed-enforcement`, `constraint-pinning`
  (`~/projects/research/agentic-research/concepts/`).
