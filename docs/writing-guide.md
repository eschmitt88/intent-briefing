---
kind: guide
title: Writing instructions for strong models
updated: "2026-11-14"
---

# Writing instructions for strong models

The reference for writing claude-system skills, rules, hooks, system prompts
and subagent briefs. **Writing something? Use [The rules](#the-rules).**
[Evidence](#evidence) is for checking or updating a rule; its numbers are
stable IDs that literature notes cite. Maintenance rules live in this repo's
`CLAUDE.md`.

## The rules

1. **P2: State what the reader won't do by default; leave out what it will.**
   Conditional requirements, corner cases, output format, and anything you
   know that it can't discover. `[strong]`
2. **P3: Put hard invariants in code, not prose.** Use hooks, typed fields
   and permission gates. Prose of either style leaks. `[strong]`
3. **P5: Hand over context, not just a task.** Include what you've found,
   what's ruled out, and where to look. Write rules as explicit imperatives,
   because soft phrasing gets lost in handoff. When the reader continues
   your work, give it the trace, not a summary. `[strong]`
4. **P1: Give the outcome, success criteria, stopping rule, and constraints
   with their reasons. Leave the method to the reader.** Spell out steps only
   where the order is itself a requirement. `[moderate]`
5. **P4: Keep structure that carries knowledge, tools, verification or
   enforcement; expect procedure to be absorbed.** Re-check both on every
   model change. `[moderate]`
6. **P6: Don't restate what the reader can discover, and don't trust
   model-written instructions untested.** Accreting rules after failures
   adds cost without gains. `[moderate]`
7. **P7: The weaker or cheaper the reader, the more explicit the
   structure.** This matters here because many subagents run on Sonnet or
   Haiku. `[weak]`

**Evidence tags.** `[strong]` passes `/elevate` Gate 1 (peer-reviewed, code
released, or ≥3 independent attestations at credibility ≥3). `[moderate]` is
one credible controlled study, or vendor guidance plus a study. `[weak]` is
practitioner reports or single small studies. `[provisional]` is not yet
ingested. `[in-house]` is a de-identified observation from the private
system audit, not literature.

## This guide's own standing

The guide is model-written and has not been tested against held-out tasks,
which is what P6 asks for. Its evidence comes from literature, not from
checking the guide itself. The partial check available here is in-house:
whether briefs written after the guide meet their goals more often in the
private audit. Until then, treat it as a well-sourced hypothesis.

## Evidence

1. **Brief, don't script, for procedure the reader can work out.** State the
   outcome, the success criteria, the stopping rule, the hard constraints and
   the reason for each. Leave the method to the reader. Keep explicit steps
   only where the order or completeness of steps is itself a requirement.
   `[moderate]`:
   - Vendor guidance on both sides: [[literature/posts/openai2026gpt55]]
     ("avoid step-by-step process guidance unless the exact path matters";
     "define success criteria and stopping rules"),
     [[literature/posts/anthropic2026prompting]] and
     [[literature/posts/anthropic2026skill]].
   - One study: a procedure-heavy evolved harness added ~0 for a frontier
     model without training ([[literature/papers/ye2026harnesszero]]).
   - Literal worked demos hurt *small* reasoning models. The
     "abstracted insights help" result does not survive compute matching
     ([[literature/papers/wang2025harm]], `[weak]`).
   - No controlled study yet compares a goal-only brief with a procedural
     brief on agentic tasks.
2. **State what the reader won't do by default, and leave out what it will.**
   Coverage of non-default requirements is the live axis, not length.
   `[strong]`:
   - An unstated requirement loses ~22.6% accuracy on average. Conditional
     requirements are met unprompted only 22.9% of the time, format
     requirements 70.7%.
   - Unstated requirements regress about twice as often across model
     updates (5.9% vs 3.0%) ([[literature/papers/yang2025what]]).
   - Stating everything costs too. Joint compliance compounds small misses:
     at 10 instructions, Claude 3.5 Sonnet satisfies all of them 48% of the
     time, GPT-4o 21% ([[literature/papers/harada2025instructions]]).
   - Blind length caps don't help; a diagnosed choice of what to state does
     ([[literature/papers/liu2026espo]],
     [[literature/papers/yang2025what]]).
   - Put the critical constraints first
     ([[literature/papers/jaroslawicz2025instructions]]).
3. **Hard invariants go in code, not prose of either style.** Use hooks,
   typed fields, runtime policy checks and permission gates. Expect some
   utility cost and measure it. `[strong]`:
   - Prompt-only policies are attacked successfully 5/5 times, against 0/5
     when enforced at runtime; utility can drop (83.7 → 62.5 on AgentDojo)
     ([[literature/papers/palumbo2026formal]]).
   - Rules lost in handoff: a typed audience allowlist leaked 0/48 times,
     against 58/288 for prompt-only mitigation
     ([[literature/papers/wang2026facts]]).
   - A model-judged permission gate still misses 17% of real overeager
     actions ([[literature/posts/hughes2026claude]]).
   - Moving a rule from prose into a controller helped a frontier model
     ([[literature/papers/rodionov2026improving]]).
   - Hub `typed-enforcement` and `constraint-pinning`.
4. **Expect procedural scaffolding to be absorbed. Keep structure that
   carries knowledge, tools, verification or enforcement, and re-test both
   on every model change.** `[moderate]`:
   - A harness's procedure added ~0 for a frontier model; its domain
     knowledge plus validation tool added +16
     ([[literature/papers/ye2026harnesszero]]).
   - Verification gave the largest multi-agent repair
     ([[literature/papers/cemri2025why]]).
   - Model-run planning and verifier loops help on GAIA L2, but the effect
     depends on model family. "The strongest model gained most" holds only
     within the Anthropic models, at L2, on one slice
     ([[literature/papers/starace2026scaffold]]).
   - Anthropic kept a planner and an evaluator across model generations and
     dropped the rest ([[literature/posts/rajasekaran2026harness]]).
5. **Hand over context, not just a task. Make rules travel as explicit
   imperatives.** The reader matches the author in capability, not in
   context. `[strong]`:
   - Under compression, facts survive at ~0.98 but rules only at 0.53–0.69.
     Soft phrasing ("use discretion") leaks
     ([[literature/papers/wang2026facts]]).
   - For a successor that must continue the same work, the raw trace was the
     only consistent gain in solve rate (+6.1 to +14.9). Structured notes
     didn't beat free-form ones ([[literature/papers/kc2026handoff]]).
   - Aggregator nodes lose more than linear chains
     ([[literature/papers/mazumder2026agentcollabbench]]).
   - Coupled parallel writes need one thread, not better briefs
     ([[literature/posts/yan2025multiagents]], `[weak]`).
6. **Don't restate what the reader can discover. Gate model-written
   instructions on a held-out eval.** `[moderate]`:
   - Context files did not raise success and added ~20% cost.
     Developer-written files beat LLM-generated ones by 4.2 points
     (p=0.038), but that comparison is uncontrolled. With the repo docs
     removed, the LLM files helped
     ([[literature/papers/gloaguen2026evaluating]]).
   - Iteration loops that patch failures accumulate rules without gains
     ([[literature/papers/zhu2026sage]], [[literature/papers/liu2026espo]]).
   - Inside a held-out eval loop, LLM-rewritten tool servers beat
     human-written ones ([[literature/posts/aizawa2025writing]]).
7. **Give weaker or cheaper readers more explicit structure.** `[weak]`:
   - Rule-heavy constraints helped a mid-tier model and hurt a frontier one
     ([[literature/papers/khan2025prompting]], cred 1, direction only).
   - Exemplars hurt a reasoning-specialised small model but still helped a
     general one ([[literature/papers/pushkin2026soft]]).
   - CoT prompting helps non-reasoning models a little and reasoning models
     ≤3 pp or negatively ([[literature/papers/meincke2025prompting]]).
   - A strong model writing a deterministic harness for a weak one is the
     extreme case (P3, P4).
   - The flip point is unmeasured and model-family-dependent (research-plan
     Q2).

## Open questions

See `research-plan.md` § Open questions.
