---
kind: post
title: "Effective context engineering for AI agents"
author: "Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield (Anthropic Applied AI team)"
institutions: ["Anthropic"]
year: 2025
published: "2025-09-29"
venue: "Anthropic Engineering blog"
peer_reviewed: false
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
code_url: null
citations: null
source: "raw/web/anthropic.com-effective-context-engineering-for-ai-agents.md"
added: "2026-11-14"
relevance: 4
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/context-engineering]]", "[[concepts/degrees-of-freedom]]", "[[concepts/requirement-coverage]]", "[[concepts/instruction-density-decay]]"]
tags: [context-engineering, system-prompts, compaction, sub-agents, vendor-guidance]
---

# Effective context engineering for AI agents

## TL;DR

Anthropic's Applied AI team defines context engineering as curating "the
smallest possible set of high-signal tokens that maximize the likelihood of
some desired outcome". System prompts should be at the "right altitude",
between brittle hardcoded if-else logic and vague guidance that "falsely
assumes shared context". For long horizons it recommends just-in-time
retrieval, compaction, structured note-taking and sub-agents. This is
vendor guidance with essentially no measurements.

## Claims

Measured or cited:
- Context rot: cites external needle-in-a-haystack work (Chroma's "context
  rot" report) showing that recall degrades as context grows, "across all
  models". The data is not reproduced in the post.
- The sub-agent pattern "showed a substantial improvement over single-agent
  systems on complex research tasks". This points back to
  `hadfield2025multiagent`. No new number.

Asserted (guidance):
- **Right altitude.** "At one extreme, we see engineers hardcoding complex,
  brittle logic in their prompts to elicit exact agentic behavior. This
  approach creates fragility and increases maintenance complexity over
  time. At the other extreme, engineers sometimes provide vague, high-level
  guidance that fails to give the LLM concrete signals for desired outputs
  or falsely assumes shared context." The target is "specific enough to
  guide behavior effectively, yet flexible enough to provide the model with
  strong heuristics". The figure caption names the poles "brittle if-else
  hardcoded prompts" and prompts "overly general or [that] falsely assume
  shared context".
- **Minimal ≠ short.** "Strive for the minimal set of information that fully
  outlines your expected behavior. (Note that minimal does not necessarily
  mean short...)" Start with a minimal prompt on the best model, then add
  instructions and examples based on observed failure modes.
- Don't stuff "a laundry list of edge cases" in an attempt to articulate
  every rule. Use "diverse, canonical examples" instead.
- Section structure (XML tags or Markdown headers) helps, "although the
  exact formatting of prompts is likely becoming less important as models
  become more capable".
- Tools should be minimal and non-overlapping: "If a human engineer can't
  definitively say which tool should be used in a given situation, an AI
  agent can't be expected to do better."
- Just-in-time retrieval keeps lightweight references (paths, queries,
  links) and loads data on demand. Claude Code is the hybrid example:
  CLAUDE.md is loaded up front, and glob/grep are used just in time.
- **Compaction.** Summarize history near the limit and restart. Claude Code
  keeps architectural decisions, unresolved bugs and implementation details,
  plus the five most recently accessed files. Tune compaction prompts for
  recall first, then precision. Overly aggressive compaction loses "subtle
  but critical context whose importance only becomes apparent later".
  Tool-result clearing is the lightest-touch form.
- **Note-taking.** A persistent NOTES.md or to-do list. Claude Plays Pokémon
  is the anecdote.
- **Sub-agents.** Each explores with "tens of thousands of tokens or more"
  and returns a condensed summary "(often 1,000-2,000 tokens)".
- "Smarter models require less prescriptive engineering", and design will
  trend toward "progressively less human curation". "Do the simplest thing
  that works."

## Methods / basis

- Distilled practitioner guidance from Anthropic's Applied AI team, drawn
  from customer work and Anthropic products (Claude Code, the Developer
  Platform memory and context-management features). No experiments.

## Results

- None reported in the post.

## Critique / open questions

- **Evaluation quality.** There is no evaluation. Every recommendation is
  asserted, and the one empirical pointer is to another vendor post. Treat
  it as authoritative *guidance about the vendor's own models*, not as
  evidence that the guidance improves outcomes. Single lineage (Claude). It
  also promotes Developer Platform features.
- **On the 2x2.** It explicitly rejects both **verbose procedure** ("brittle
  if-else hardcoded prompts") and **terse intent** that "falsely assumes
  shared context". It lands on **verbose intent with heuristics**, plus
  canonical examples in place of rule lists. "Minimal does not mean short"
  is the clearest vendor statement that coverage, not brevity, is the
  objective.
- **Q2 tension.** "Smarter models require less prescriptive engineering" is
  an untested assertion. It cuts against 2606.08529 (the strongest model
  gained most from scaffolding). The guide should treat it as a vendor
  hypothesis.
- **Q3.** It says nothing about which instructions must stay explicit. The
  "add instructions based on observed failure modes" loop is the implied
  mechanism.
- **Compaction and handoff.** The warning that compaction drops context
  whose importance "only becomes apparent later" is the same failure
  Cognition describes (`yan2025multiagents`), seen from the single-agent
  side.
- **Discrepancy vs candidate summary.** The candidate says "brittle if/then
  logic". The body text says "complex, brittle logic", and the figure
  caption says "brittle if-else hardcoded prompts". The substance matches.

## Trust signals

- **Credibility:** 2. A primary vendor source with named authors, but pure
  guidance: no data, no artifacts, no peer review, and some product
  promotion. Its weight is as the model vendor's stated recommendation,
  which counts toward "consistent vendor guidance", not as a study.

## Follow-up

- **Relevance:** 4. This is the canonical vendor statement of the
  "right altitude" and "minimal but not short" positions that P1 and P2 are
  phrased around. It carries no evidence of its own.
- **Guide:** P1 supports. It is the vendor's explicit rejection of
  hardcoded if-else prompts in favor of heuristics. Vendor guidance only.
- **Guide:** P2 supports. "Minimal does not necessarily mean short", and
  vague prompts that "falsely assume shared context" are named as a failure
  mode.
- **Guide:** P4 in tension. It asserts that formatting and prescription
  matter less as models improve, which runs against the measured
  scaffolding result in 2606.08529. Flag this as a vendor claim, not
  evidence.
- **Guide:** P5 supports. Sub-agents return 1–2k-token distillations, and
  over-aggressive compaction loses late-relevant context.
