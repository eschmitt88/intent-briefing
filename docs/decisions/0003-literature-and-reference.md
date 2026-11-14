---
kind: decision
id: 3
title: Literature-and-reference project; no in-house experiments
status: accepted
date: "2026-11-14"
supersedes: [1, 2]
---

# 0003 — Literature and reference only

## Context

ADR 0002 established that in-house experiments cannot reach significance
inside the budget, and that AI-generated tasks would not translate to real
work. The user then proposed dropping experiments altogether. Fable agreed
(2026-11-14) and flagged two earlier mistakes:

- ADR 0001's "needs its own experiments" was decided before any literature
  had been read. The first sweeps showed the field publishing the
  controlled studies we would have attempted, several per quarter.
- `/elevate` admits only peer-reviewed sources, sources with released code,
  or ≥3 independent attestations at credibility ≥3. A home-grown n≈20
  result is credibility ~2. **Our experiments could never have passed the
  gate they existed to feed.**

## Decision

- **This repo curates; it does not experiment.** The experiment skill group,
  scoped experiment/notebook rules and `experiments/` are removed.
  `agency: max` stays so curation runs unattended.
- **Deliverables:** curated literature, plus an evidence-graded writing guide
  (`docs/writing-guide.md`) that serves as the live reference for
  claude-system. Changes reach claude-system via hub `/elevate`.
- **Gaps become digest watch items**, not experiments: goal-vs-procedure on
  agentic tasks, long-horizon drift.
- **Our own author-bias question (Q5) moves to a separate private repo**, a
  manually triggered QA audit of this box's agent system. Its inputs are
  real transcripts from private projects. That cannot be published, and an
  audit is not literature. Only general, de-identified lessons may come back
  here, and only as a clearly labelled in-house observation in the writing
  guide.
- **A skill-rewrite regression check** is engineering practice for
  claude-system, proposed via `/elevate` when the evidence is ingested. It is
  not this repo's job.
- The field A/B tripwire from ADR 0002 is dropped.

## Kept from ADR 0002

The power and validity analysis, and model pinning (now inert here; it
applies if the audit repo ever replays anything).
