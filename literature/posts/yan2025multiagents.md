---
kind: post
title: "Don't Build Multi-Agents"
author: "Walden Yan"
institutions: ["Cognition"]
year: 2025
published: "2025-06-12"
venue: "Cognition blog"
peer_reviewed: false
url: https://cognition.ai/blog/dont-build-multi-agents
code_url: null
citations: null
source: "raw/web/cognition.ai-dont-build-multi-agents.md"
added: "2026-11-14"
relevance: 4
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/context-engineering]]", "[[concepts/commanders-intent]]"]
tags: [multi-agent, context-sharing, practitioner-opinion, coding-agents]
---

# Don't Build Multi-Agents

## TL;DR

Cognition (Devin) argues for a single-threaded agent over parallel
multi-agent systems, based on two principles. (1) Share context: share full
agent traces, not just individual messages. (2) Actions carry implicit
decisions, and conflicting decisions carry bad results. The post contains no
measurements. Its Flappy Bird example is a hypothetical the author calls
possibly "contrived".

## Claims

All asserted. The post reports no numbers and no experiments.
- **Principle 1:** "Share context, and share full agent traces, not just
  individual messages." Copying the original task into each subagent is not
  enough, because in production the parent conversation is multi-turn and
  includes tool calls whose details "could have consequences on the
  interpretation of the task".
- **Principle 2:** "Actions carry implicit decisions, and conflicting
  decisions carry bad results." Even with the parent's full context,
  parallel subagents that cannot see each other's actions make conflicting
  assumptions "not prescribed upfront".
- Principles 1–2 are "so rarely worth violating" that architectures breaking
  them should be ruled out by default. The recommended default is a
  single-threaded linear agent. For very long tasks, add a dedicated model
  that compresses history into "key details, events, and decisions". Cognition
  says it has fine-tuned a smaller model for this, and calls it "hard to get
  right".
- Supporting cases: Claude Code subagents (as of June 2025) never ran in
  parallel with the main agent and were mostly limited to answering
  well-defined questions, not writing code. 2024-era "edit apply" pipelines
  (a large model writes a markdown edit description, a small model applies
  it) failed on "the most slight ambiguities in the instructions".
- Agent-to-agent negotiation is not yet reliable in 2025. "Humans are quite
  efficient at communicating our most important knowledge to one another,
  but this efficiency takes nontrivial intelligence."

## Methods / basis

- A position essay from a coding-agent builder, grounded in their production
  experience. No data, no eval, no released artifacts.

## Results

- None measured. The **Flappy Bird example** is illustrative. Task "build a
  Flappy Bird clone" splits into a background-with-pipes subtask and a bird
  subtask. Subagent 1 builds a Super Mario-style background, and subagent 2
  builds a bird that neither looks nor moves like Flappy Bird's. A second
  revision gives each subagent the prior context, and the result is a bird
  and a background in "completely different visual styles", because neither
  could see the other's work.

## Critique / open questions

- **Evaluation quality.** There is no evaluation. The example is constructed,
  not observed, and the claims rest on undisclosed production experience.
  Single domain (coding, which is write-heavy) and single vendor. As
  evidence it is weak. Its value is as a well-argued hypothesis about where
  intent briefs stop working.
- **What it actually says vs the candidate summary.** The candidate framed
  it as "a subtask handed over as a summary loses implicit decisions". The
  post claims more than that. Principle 2 says that **even full shared
  context is not enough** when parallel workers make unobserved decisions:
  the problem is coordination between siblings, not only parent-to-child
  briefing. The post also endorses compression, but inside a single thread
  (a history-compression model), so it does not say context is
  incompressible.
- **On the 2x2.** The post is off the axis: it argues that no brief, in any
  quadrant, replaces a shared trace for tightly coupled work. In
  mission-command terms, sibling units acting on intent without shared
  doctrine or lateral communication produce inconsistent results. This is a
  candidate *boundary condition* for the intent-brief thesis (coupling
  between subtasks), not a claim about how to write the brief.
- Dated. "As of June 2025" claims about Claude Code and about agents being
  unable to negotiate may not hold for later models. Bears on Q2.

## Trust signals

- **Credibility:** 2. A named practitioner at a credible coding-agent
  company, but an opinion piece with a hypothetical example, no data, no
  artifacts, no peer review, and a commercial interest (it closes with a
  pitch for Devin).

## Follow-up

- **Relevance:** 4. This is the strongest practitioner statement of a limit
  on brief-only delegation (coupled, write-heavy parallel work). It frames
  Q3 and the context asymmetry, even though it supplies no measured
  evidence.
- **Guide:** P5 supports and refines. Some context must travel as full
  traces, as the guide says. But the post adds that for coupled parallel
  writes, sending context to each worker still fails. The fix is
  architectural (one thread, or serialize the decisions), not a better
  brief.
- Pair with `chase2025multiagent` (read vs write coupling) and
  `hadfield2025multiagent` (read-heavy research, where parallel briefs
  worked). Together they suggest a boundary of the form "brief-only
  delegation works when subtasks are read-only or decoupled".
