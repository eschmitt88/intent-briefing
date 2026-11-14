---
kind: concept
name: "invariants-in-code"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/palumbo2026formal]]"
  - "[[literature/papers/wang2026facts]]"
  - "[[literature/posts/hughes2026claude]]"
  - "[[literature/papers/rodionov2026improving]]"
  - "[[literature/papers/harada2025instructions]]"
  - "[[literature/papers/barbaste2026harness]]"
  - "[[literature/papers/qian2026ai4ai]]"
  - "[[literature/papers/li2025thinking]]"
  - "[[literature/posts/openai2026gpt55]]"
related_concepts:
  - "[[concepts/durable-structure]]"
  - "[[concepts/handoff-context-loss]]"
  - "[[concepts/instruction-density-decay]]"
related_experiments: []
tags: [enforcement, invariants, hooks, policy, safety]
---

# invariants-in-code

## Definition

Hard constraints that must hold on every run should be enforced by code:
hooks, typed fields, runtime policy monitors, permission gates. They should
not be stated in prose, whether as a brief or a script. This is the local,
literature-facing form of hub `typed-enforcement` and `constraint-pinning`.

## Why it matters here

This is guide P3, and it is the best-supported principle in the corpus.

- **Runtime policy enforcement** ([[literature/papers/palumbo2026formal]]):

  | Test | Prompt-only | Enforced |
  |---|---|---|
  | Exfiltration attacks that succeed | 5/5 | 0/5 |
  | Multi-agent trials fully compliant | 0/15 | 15/15 |
  | Frontier τ²-Bench airline pass^1 | 74.7 | 81.5 |

  Enforcement can cost utility: on AgentDojo, benign utility fell from 83.7
  to 62.5.
- **Typed boundaries.** A typed audience allowlist leaked 0/48, against
  58/288 leaks for prompt-only mitigation
  ([[literature/papers/wang2026facts]]).
- **Model-judged gates miss.** The model-judged permission layer misses 17%
  of 52 real overeager actions. Anthropic found no prompt fix for scope
  misses and kept a deterministic allowlist
  ([[literature/posts/hughes2026claude]]).
- **Prose rule to controller.** Moving a prose reset rule into a controller
  helped a frontier model ([[literature/papers/rodionov2026improving]]).
- **Joint compliance collapses.** Even Claude 3.5 Sonnet satisfies six
  linter-checkable style rules together only 1% of the time; code should
  check those rules ([[literature/papers/harada2025instructions]]).
- **Field practice.** Harnesses are migrating policy from prompts into
  configuration ([[literature/papers/barbaste2026harness]]). Vendor guidance
  reserves ALWAYS/NEVER "for true invariants"
  ([[literature/posts/openai2026gpt55]]).
- **Weaker support.** CoT neglects simple mechanical constraints, but only
  qualitatively and mainly below the frontier
  ([[literature/papers/li2025thinking]]).

## Connections

- [[concepts/durable-structure]]: enforcement is one of the three kinds of
  structure that survive.
- Hub concepts: `typed-enforcement`, `constraint-pinning`,
  `enforcement-boundary-placement`.
