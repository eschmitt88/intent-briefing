---
kind: concept
name: "handoff-context-loss"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/wang2026facts]]"
  - "[[literature/papers/kc2026handoff]]"
  - "[[literature/papers/mazumder2026agentcollabbench]]"
  - "[[literature/papers/yu2026when]]"
  - "[[literature/papers/cemri2025why]]"
  - "[[literature/posts/hadfield2025multiagent]]"
  - "[[literature/posts/yan2025multiagents]]"
  - "[[literature/posts/chase2025multiagent]]"
  - "[[literature/posts/hughes2026claude]]"
  - "[[literature/papers/thomas2007interpreting]]"
related_concepts:
  - "[[concepts/brief-anatomy]]"
  - "[[concepts/invariants-in-code]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/commanders-intent]]"
related_experiments: []
tags: [delegation, handoff, multi-agent, context-transfer]
---

# handoff-context-loss

## Definition

What is lost when work passes from one agent or session to another.
**Rules, boundaries and implicit decisions are lost far more often than
facts.** That loss is the reason the research plan's "peer in capability, not
in context" asymmetry is load-bearing.

## Why it matters here

- **Facts survive, rules don't.** Under a 25-word summary cap, facts survive
  at ~0.98 while rules survive at only 0.53–0.69. 25–39% of rules are dropped
  entirely, and downstream agents re-add a missing rule only 7.5% of the
  time. Soft phrasing leaks: "use discretion" leaked 38–73% of the time,
  while a typed audience allowlist leaked 0/48
  ([[literature/papers/wang2026facts]]).
- **Traces beat notes for solving.** When a successor agent takes over
  interrupted coding work, predecessor context cuts its effort by 20–59%.
  Only the raw trace consistently raised the solve rate (+6.1 to +14.9).
  Structured notes did not beat free-form summaries
  ([[literature/papers/kc2026handoff]]).
- **Topology matters.** Information is dropped 1.6–5.0× more per hop at
  converging nodes, where several agents feed one, than in linear chains
  ([[literature/papers/mazumder2026agentcollabbench]]).
- **Weak support for a capability effect.** Stronger models lost more in
  some relay settings but not others; the study ran once per cell with no
  frontier models ([[literature/papers/yu2026when]]).
- **Base rate.** 32.3% of multi-agent failures are inter-agent misalignment
  ([[literature/papers/cemri2025why]]).
- **Practitioner accounts.**
  - Terse delegations led to duplicated and misdirected subagent work
    ([[literature/posts/hadfield2025multiagent]]).
  - Parallel writers clash even with the full context available. That is
    coordination, not compression, and the fix is a single thread
    ([[literature/posts/yan2025multiagents]],
    [[literature/posts/chase2025multiagent]]).
  - At delegation, the orchestrator's instruction can look like full user
    authorization ([[literature/posts/hughes2026claude]]).
- **Human analogue.** Intent transfer measured with true/false probes in a
  command-staff exercise; the result is confounded
  ([[literature/papers/thomas2007interpreting]]). Shattuck's 34% match rate
  (11 of 32 episodes) is known only from a secondary reproduction; see the
  curation record.

The design rules that follow:

- State constraints explicitly as operational imperatives.
- Enforce boundaries with typed fields.
- Pass full traces when the successor must continue the same decisions.
- Avoid coupled parallel writes.

## Connections

- [[concepts/brief-anatomy]]: what has to travel in the brief.
- [[concepts/invariants-in-code]]: boundaries that must survive a lossy relay.
- Hub `lossless-context-offload`.
