---
kind: post
title: "Harness design for long-running application development"
author: "Prithvi Rajasekaran (Anthropic Labs)"
institutions: ["Anthropic"]
year: 2026
published: "2026-03-24"
venue: "Anthropic Engineering blog"
peer_reviewed: false
url: https://www.anthropic.com/engineering/harness-design-long-running-apps
code_url: null
citations: null
source: "raw/web/anthropic.com-harness-design-long-running-apps.md"
added: "2026-11-14"
relevance: 5
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/durable-structure]]", "[[concepts/brief-anatomy]]", "[[concepts/handoff-context-loss]]"]
tags: [harness, long-running, planner-generator-evaluator, scaffolding, vendor-account, capability-boundary]
---

# Harness design for long-running application development

## TL;DR

A practitioner account of a planner → generator → evaluator harness for
multi-hour autonomous app builds. The author then simplified it as the
models improved. **Context resets** were dropped when moving from Sonnet 4.5
to Opus 4.5, because Opus 4.5 "largely removed" context anxiety. With Opus
4.6, the **sprint construct** was removed and the **per-sprint evaluator**
became a single end-of-run pass. The **planner** stayed because without it
the generator under-scoped. The **evaluator** stayed, but only as worth the
cost "when the task sits beyond what the current model does reliably solo."
The candidate quote is verbatim. All evidence is n = 1 builds per
configuration, judged by the author.

## Claims

Measured (single runs; cost and time only):
- Retro game maker, Opus 4.5, same one-sentence prompt:
  - Solo: 20 min, $9.
  - Full harness: 6 hr, $200 ("over 20x more expensive").
  - The planner expanded the prompt into a 16-feature spec over ten
    sprints. Sprint 3's contract alone had 27 criteria.
- DAW, updated harness (Opus 4.6, no sprints): 3 hr 50 min, $124.70.
  - Planner 4.7 min / $0.46.
  - Build rounds 2 h 7 min / $71.08, 1 h 2 min / $36.89, 10.9 min / $5.88.
  - QA rounds $3.24, $3.09, $4.06.
  - The builder "ran coherently for over two hours without the sprint
    decomposition that Opus 4.5 had needed."
- Frontend loop: 5–15 generator/evaluator iterations, runs up to 4 hours.
  Scores "improved over iterations before plateauing". No score values are
  given.

Asserted (author judgment from inspecting outputs and logs):
- **The principle (verbatim):** "every component in a harness encodes an
  assumption about what the model can't do on its own, and those assumptions
  are worth stress testing, both because they may be incorrect, and because
  they can quickly go stale as models improve."
- **What was removed, and why:**
  - *Context resets with structured handoffs.* These were essential for
    Sonnet 4.5's "context anxiety", where compaction "wasn't sufficient".
    Removed because "Opus 4.5 largely removed that behavior on its own";
    SDK auto-compaction replaced them.
  - *Sprint construct / one-feature-at-a-time decomposition.* Removed for
    Opus 4.6, citing its launch claims (plans more carefully, sustains
    agentic tasks longer, better long-context retrieval).
  - *Per-sprint grading.* Became "a single pass at the end of the run",
    a consequence of removing sprints.
- **What survived, and why:**
  - *Planner:* "Without the planner, the generator under-scoped: given the
    raw prompt, it would start building without first speccing its work,
    and end up creating a less feature-rich application".
  - *Evaluator* (final pass): "On 4.5, that boundary was close... On 4.6,
    the model's raw capability increased, so the boundary moved outward...
    for tasks within that boundary, the evaluator became unnecessary
    overhead. But for the parts of the build that were still at the edge of
    the generator's capabilities, the evaluator continued to give real
    lift." In the DAW run, QA still caught stubbed core features (clip drag,
    instrument panels, recording).
- **Method of removal.** The first, radical cut "wasn't able to replicate
  the performance of the original", and it became hard to tell which pieces
  were load-bearing. So the author moved to "removing one component at a
  time and reviewing what impact it had". Only the sprint removal is
  reported in any detail.
- **Planner briefed at intent level on purpose.** The planner was told to
  stay at product context and high-level design, not granular
  implementation, because spec errors "would cascade into the downstream
  implementation. It seemed smarter to constrain the agents on the
  deliverables to be produced and let them figure out the path as they
  worked."
- **Sprint contracts bridged intent to testable criteria.** Generator and
  evaluator negotiated "what 'done' looked like" before coding. This "kept
  the work faithful to the spec without over-specifying implementation too
  early."
- **Self-evaluation is lenient.**
  - Agents "confidently prais[e] the work" they produced.
  - "Out of the box, Claude is a poor QA agent". It found issues, then
    talked itself into approving.
  - Tuning a separate skeptical evaluator was "far more tractable".
  - The evaluator prompt went through several rounds of log-reading and
    prompt fixes.
- **Criteria wording steers output.** "museum quality" pushed designs toward
  convergence. First-iteration outputs with criteria beat a no-prompt
  baseline.

## Methods / basis

- Single-author engineering exploration on the Claude Agent SDK, with the
  Playwright MCP for the evaluator. Comparisons are one run per arm (solo vs
  harness, Opus 4.5) and one run of the simplified harness (Opus 4.6, a
  different app). Quality is judged by the author clicking through the apps
  and reading logs. The evaluator's sprint verdicts are LLM judgments, but
  they rest on concrete Playwright tests (e.g. a FastAPI route-order bug
  returning 422).

## Results

- There is no quantitative quality metric. Cost and time are the only
  numbers. The Opus 4.6 simplified harness was not run on the same prompt as
  the Opus 4.5 harness, so there is no matched before/after for the
  simplification.

## Critique / open questions

- **Evaluation quality.** Weak as evidence:
  - n = 1 per arm and different tasks across harness versions.
  - Outcomes are judged by the author, who also designed the harness.
  - No ablation table: "one component at a time" is described, but only
    one removal (sprints) is reported, and its effect isn't quantified.
  - Single lineage (Claude), single domain (greenfield web apps).
  - The model-capability attributions lean on launch-blog claims.
  - Still valuable as a primary practitioner trace of *why* each piece was
    kept or cut.
- **Verification vs the candidate summary.**
  - The summary's list of removed components and survivors is correct.
  - It glosses over sequencing. Context resets were not part of the
    one-at-a-time Opus 4.6 ablation: they were dropped earlier, when the
    harness was rebuilt on Opus 4.5 (relative to the prior Sonnet 4.5
    harness). The one-at-a-time removals happened under Opus 4.6.
  - Per-sprint eval wasn't removed independently. It became a final pass
    because sprints were gone.
  - "A final evaluator stayed" needs qualifying: kept, but explicitly
    conditional on task difficulty relative to the model.
- **On the 2x2.** This is the most direct vendor example of the brief
  pattern working inside a pipeline. The planner writes a **verbose-intent**
  spec (product context, deliverables, no implementation detail), and the
  generator chooses the path. Coverage is restored through **negotiated
  acceptance criteria** (27 criteria in one sprint), not procedure. The
  procedural scaffold (sprints) was the part that got absorbed by a stronger
  model.
- **Q2 (capability boundary).** The evaluator-boundary passage is the
  clearest qualitative statement of a *moving* boundary. Scaffold value
  depends on where the task sits relative to solo capability, not on model
  strength alone. That fits 2606.08529, where the strongest model still
  gained: a harder task restores the gain. The closing claim is that the
  harness design space "doesn't shrink as models improve. Instead, it
  moves."
- **Q4 (horizon).** Context resets as structured handoffs, then their
  removal, is a model-specific finding: Sonnet 4.5's context anxiety. It is
  not a general verdict on handoffs.
- **Q5.** Unprompted, the generator under-scoped (it did not over-script).
  That matches the multi-agent post (`hadfield2025multiagent`).

## Trust signals

- **Credibility:** 2. Named Anthropic Labs author, real cost tables and
  concrete bug examples. But n = 1 per arm, outcomes judged by the author,
  no released harness code or prompts (only the frontend-design skill is
  public), and no peer review.

## Follow-up

- **Relevance:** 5. A primary source for scaffold absorption across model
  generations, with explicit reasons why the planner and evaluator survived.
  It bears directly on P4, Q2 and P1.
- **Guide:** P4 refines. Keep structure whose job the model still can't do
  solo: the planner (the model under-scopes without it) and the evaluator
  (self-evaluation is lenient). Delete structure the model has absorbed:
  context resets on Opus 4.5, sprints on Opus 4.6. Re-test each component
  per model and per task difficulty, one at a time.
- **Guide:** P1 supports. The planner was deliberately briefed at the
  deliverable level, not the implementation level ("constrain the agents on
  the deliverables... let them figure out the path"). Testable acceptance
  criteria carried the coverage.
- **Guide:** P2 supports. Negotiated sprint contracts (27 criteria in one
  sprint) made "done" explicit before work began.
- **Guide:** P5 supports (historical). Structured handoff artifacts were
  needed whenever context was reset.
- Candidate: the predecessor post "Effective harnesses for long-running
  agents" (`anthropic.com/engineering/effective-harnesses-for-long-running-agents`)
  for the Sonnet 4.5 context-reset baseline.
