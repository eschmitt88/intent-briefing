---
kind: decision
id: 2
title: Decision-grade boundary-finding instead of factorial significance
status: accepted
date: "2026-11-14"
---

# 0002 — Decision-grade evaluation

## Context

The user doubted two things: that we can run enough tests for significance,
and that AI-generated tests would translate to real work. Both doubts check
out.

- **Power.** A paired binary outcome with ~20% discordant pairs needs ~154
  task pairs to detect a 10pp difference and ~620–800 for 5pp. At ~50–200k
  tokens per agentic run, one two-arm frontier comparison costs ~20–40M
  tokens, against a 5M per-run ceiling. A 2×2 × 3-model factorial at
  significance is out of reach.
- **Validity.** Synthetic tasks come from what models find natural. They are
  biased toward styles the model already reads well, and they miss the
  messy, unstated requirements where terse briefs actually fail.

Reviewed with Fable (2026-11-14).

## Decision

1. **Goal: decision-grade, not publication-grade.** The bar is "rewriting
   skill X doesn't regress on its real workload". It is a head-to-head
   promotion gate, the same pattern the box uses for model promotion. The
   literature carries the general claim. We look for **boundaries and
   failure modes**, where existence proofs need few runs.
2. **Real tasks only. No LLM-invented tasks.** Sources: the box's own
   transcripts, real subagent briefs, and commits paired with the transcript
   that produced them. For replays, **withhold the requirements the author
   knew but never wrote down**, so the context gap is real.
3. **Cheap outcome signals first, full replays last:**
   - *Comprehension probe.* The implementer restates goal, constraints and
     plan; this is scored against the author's hidden requirement checklist.
     About 2k tokens instead of 200k, and it measures coverage directly.
   - *Hook-logged invariant violations.* Machine-checkable, no judge.
     This is Q3's metric.
   - *Correction rate in existing transcripts.* The next user message after
     an agent turn, and re-dispatch after a subagent handback, serve as
     free real-world failure labels.
   - Full replays only where the probe and the outcome would disagree.
4. **Ordinal/continuous paired outcomes** (fraction of tests passed,
   invariants held, tokens, turns) with several seeds per task, not binary
   pass/fail.
5. **Pin concrete model slugs for the whole program.** Floating aliases
   confound any comparison that spans weeks.
6. **Field A/B on recurring jobs only as a gate/tripwire, never as an
   estimator.** Rotate variants by day, not by run. Log the variant id in
   the job's own log line. Exclude `/elevate` (zero-variance outcome). Keep
   invariants in hooks whatever the variant, because curate writes into live
   knowledge graphs.

## Question order (supersedes research-plan ordering)

1. **Q5 author bias, now.** Classify the box's real subagent briefs. Pure
   text analysis, the cheapest and most ecologically valid question.
2. **Q3 invariant boundary.** Hooks plus probes.
3. **Q1 effect.** Small paired corpus; the probe is the primary metric.
4. **Q2 capability boundary.** Cheap Haiku/Sonnet arms, a small frontier
   arm.
- **Q4 horizon:** demoted until the field tripwire has months of data.
- **Q6 July natural experiment: dead as stated.** There are no pre-07-31
  transcripts, and that program's five confounded phases included moving
  logic *into* code. Kept as a qualitative case study motivating Q3.
