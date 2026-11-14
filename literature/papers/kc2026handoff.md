---
kind: paper
title: "Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks"
authors: ["Dipesh KC", "Anjila Budathoki"]
institutions: ["Independent Researcher", "University of Tennessee, Knoxville"]
year: 2026
venue: "EMNLP 2026 (per Semantic Scholar venue metadata; arXiv v2 2026-08-30)"
peer_reviewed: true
url: "https://arxiv.org/abs/2606.02875"
code_url: "https://github.com/anjilab/agent-handoff-debt"
citations: 11
source: "raw/papers/kc2026handoff.pdf"
added: "2026-11-14"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/brief-anatomy]]", "[[concepts/context-engineering]]"]
tags: [handoff, coding-agents, swe-bench, takeover, context-transfer]
---

# Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks

## TL;DR

The protocol interrupts a coding agent at deterministic points on
SWE-bench Verified and hands the frozen repository to a successor under
four views: repository only, raw trace, summary notes, or structured notes.
Giving predecessor context cuts successor effort sharply (events -20 to
-59%, prompt tokens -42 to -63%). Solved-rate gains are smaller and depend
on the model. The raw trace is best for solving, and structured notes do
not beat free-form summaries.

## Claims

- "Handoff debt" is the extra rediscovery effort a successor pays when
  predecessor work is opaque. Resolution-only metrics can't see it.
- Context-bearing handoffs consistently reduce effort. Solved-rate effects
  are smaller and model-dependent.
- No single handoff format is best: the preferred view differs by successor
  model.

## Methods

- 75 SWE-bench Verified source tasks (15 min-1 h and 1-4 h tiers, fixed
  random order, seed 20260430).
- Predecessor: Qwen in an OpenHands-style runtime.
- Handoff points:
  - after the first source edit (75)
  - after the first validation result (75)
  - after the first post-failure edit (31)
  - **181 handoff-point tasks** in all
- Handoff states: 110 need completion, 61 already solved (preserve),
  10 existing behavior broken.
- Four views per handoff, giving 724 runs per successor:
  - repository only
  - raw trace (event log)
  - summary notes (written by the predecessor model from the log)
  - structured notes (fixed fields: changed files, artifacts, latest change
    and validation, state, error evidence, uncertainty, rollback notes, next
    action)
- Three successors, 2,172 runs in all: Qwen3.6-27B, Gemma-4-31B-it,
  Devstral-Small-2-24B.
- Outcome: official SWE-bench resolution. Cost: agent events and cumulative
  prompt tokens.
- Statistics: matched-pair bootstrap CIs. A robustness rerun of 3 attempts
  on 40 stratified handoff points (Qwen to Qwen).

## Results

Each row: solved rate / median events / prompt tokens. Deltas are against
repository-only for the same successor.

- **Qwen to Qwen**
  - Repository only: 46.4% / 99 / 1.63M
  - Raw trace: +6.1 pp / -59% / -50%
  - Summary notes: +5.0 pp / -46% / -63%
  - Structured notes: +4.4 pp / -44% / -60%
- **Qwen to Gemma**
  - Repository only: 42.5% / 49 / 738k
  - Raw trace: +6.6 pp / -57% / -59%
  - Summary notes: +1.7 pp / -33% / -57%
  - Structured notes: +1.1 pp / -20% / -57%
- **Qwen to Devstral**
  - Repository only: 34.3% / 175 / 3.94M
  - Raw trace: +14.9 pp / -58% / -58%
  - Summary notes: +9.4 pp / -30% / -42%
  - Structured notes: +10.5 pp / -29% / -42%

Significance and prompt sizes:

- All matched event-reduction CIs exclude zero.
- Raw-trace solved-rate gains hold for all successors.
- Note-based solved-rate gains are significant only for Devstral; for Qwen
  and Gemma they are n.s. at alpha = 0.05.
- Initial prompt size: raw trace median 87k chars, vs 7.2k (repository
  only), 9.8k (summary), 10.0k (structured).

Where the debt is largest:

- After the first post-failure edit. Repository-only successors need 122
  (Qwen) to 191 (Devstral) median events there.
- Context-bearing handoffs gain up to +12.9 pp (Qwen) and +19.4 pp
  (Devstral) at these points.
- On "needs completion" states, repository-only successors solve
  13.6-23.6%; the best view solves 23.6-28.2%.

The robustness rerun shows events -43 to -59%.

## Critique / open questions

- **Verified**: 181 handoff-point tasks from 75 SWE-bench Verified tasks is
  exact. Plus 724 runs per successor and 2,172 in total.
- Strong on this project's evaluation criteria:
  - Task-outcome scoring (official tests).
  - Matched design that holds the repository state fixed.
  - Bootstrap CIs and a rerun check.
- Weaknesses:
  - Single predecessor model (Qwen).
  - Mid-size open-weight successors only, no frontier models.
  - One run per cell in the main study.
  - One runtime (OpenHands-style).
  - Notes were written by the predecessor model, so note quality is bounded
    by that model.
- The structured "continuation contract" does not beat free-form summary
  notes on either solved rate or effort. A fixed schema is not, by itself,
  what makes a handoff good.
- 2x2 position: the views vary *context transfer* (none, summary,
  structured, full trace), not intent vs procedure. All successors get the
  same original task prompt. The structured notes resemble a terse-intent
  brief with fields. The raw trace is maximal context.
- "Shared doctrine" is held constant (same runtime and prompt), so the
  effect is purely about task-local context.

## Trust signals

- Two authors (an independent researcher and UT Knoxville).
- Semantic Scholar lists the venue as EMNLP 2026 Proceedings, with 11
  citations (checked 2026-11-14). Code released.
- Clean matched design with CIs.
- **Credibility:** 4. Peer-reviewed (EMNLP 2026 per S2), methodologically
  careful, outcome-scored, released code. Held back by a small team, open
  mid-size models only and one predecessor.

## Follow-up

- **Relevance:** 4. A direct controlled test of how much context to hand a
  successor agent, on real coding tasks, scored by outcome.
- **Guide:** P5 supports.
  - Handing over predecessor context cuts successor rediscovery by 20-59%
    in events and 42-63% in tokens.
  - The full raw trace gives the largest and only consistently significant
    solved-rate gains (+6.1 to +14.9 pp).
  - This backs "some context must travel as full traces".
  - Compressed notes, structured or not, recover most of the efficiency but
    less of the correctness.
- Note for brief anatomy: fixed-field handoff schemas did not outperform
  prose summaries. Content matters more than format.
