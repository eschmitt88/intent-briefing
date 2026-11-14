---
kind: decision
id: 1
title: Scope and framing of intent-briefing
status: superseded
superseded_by: 3
date: "2026-11-13"
---

# 0001 — Scope and framing

## Context

The user observed that AI-designed agentic systems over-script their prompts
and forget that the reader is at least as capable as the author. They want the
topic researched and then folded into claude-system, because it directly
affects max-agency runs, and they want a live reference that future skills,
hooks and agentic pieces are refined against. The founding decisions below
were made after consulting Fable.

## Decision

- **Own project, not a hub sub-topic.** agentic-research covers research
  agents and keeps experiments downstream. This question applies to every
  agentic piece and needs its own experiments.
- **The hub owns the concept.** `agentic-research/concepts/intent-level-briefing.md`
  holds the architectural idea. This project imports it and owns the
  empirical work: harness, task corpus, scoring, and the writing guide.
- **One path back to claude-system:** hub `/elevate` → `docs/system-proposals/`.
  No new bridge. The 2026-07-31 instruction-ablation program is the
  predecessor that new proposals extend.
- **Slug `intent-briefing`** names the practice without committing to a
  contested metaphor ("peer", "mission command") or a villain
  ("prescriptive prompting").
- **Public**, like the sibling meta projects. Anything quoted from this box
  is redacted first.
- **Experiment skills linked from day one**, `agency: max`, evaluation mode
  HCE. Literature comes first; the harness is what the July program lacked.
- **Framing:** two axes (intent/procedure × terse/verbose). The reader's
  deficit is context, not capability. Doctrine (shared rules) is a variable.
  Outcome metrics take precedence over LLM-judge rubrics.

## Consequences

Findings reach claude-system only after passing the `/elevate` gates. The
writing guide in this repo is allowed to run ahead of the evidence, but each
line in it is marked with the strength of its evidence.
