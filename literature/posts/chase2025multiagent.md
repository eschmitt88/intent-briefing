---
kind: post
title: "How and when to build multi-agent systems"
author: "Harrison Chase"
institutions: ["LangChain"]
year: 2025
published: "2025-06-16"
venue: "LangChain blog"
peer_reviewed: false
url: https://blog.langchain.com/how-and-when-to-build-multi-agent-systems
code_url: null
citations: null
source: "raw/web/blog.langchain.com-how-and-when-to-build-multi-agent-systems.md"
added: "2026-11-14"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/context-engineering]]"]
tags: [multi-agent, read-vs-write, commentary, vendor-framework]
---

# How and when to build multi-agent systems

## TL;DR

A commentary that reconciles Cognition's "Don't Build Multi-Agents" with
Anthropic's multi-agent research post. Both agree that context engineering
is crucial, and multi-agent systems that mostly **read** are easier than
those that **write**. No new evidence. Most of the post quotes the Anthropic
post and promotes LangGraph and LangSmith.

## Claims

All asserted, with no new data.
- Context engineering is the shared lesson of both posts. Cognition named
  the term. Anthropic does not use it, but addresses the same problem: long-
  horizon memory handoffs, and the subagent delegation spec, which the post
  quotes.
- "Read actions are inherently more parallelizable than write actions."
  Parallel writing faces a double problem: passing context between agents
  and then merging their outputs. "Conflicting write actions typically
  produce far worse outcomes than conflicting read actions."
- Claude Research fits this pattern. Subagents do the reading (research),
  and the writing (the final report) is "deliberately handled by a single
  main agent in one unified call". (The released Anthropic lead prompt
  confirms this: "NEVER create a subagent to generate the final report".)
- Even read-heavy systems need careful context engineering. The post quotes
  the Anthropic semiconductor-shortage duplication anecdote verbatim.
- No one-size-fits-all architecture. Frameworks should let you "slide
  anywhere on this spectrum" (a LangGraph pitch).

## Methods / basis

- A synthesis of two other vendors' posts, plus LangChain's framework
  position. No experiments, no data.

## Results

- None. The only numbers are restated from Anthropic (~20-query starter
  evals).

## Critique / open questions

- **Evaluation quality.** There is nothing to evaluate. It is an
  interpretation of two non-empirical or lightly empirical posts by a vendor
  of agent frameworks and observability tools.
- **Value.** The read/write distinction is a useful, testable framing. It
  turns Cognition's blanket "don't" into a condition: coupling between
  subtasks, with writes as the high-coupling case. That is a candidate
  boundary for Q3 and for when brief-only delegation suffices. The post does
  not formalize coupling or test it.
- **Discrepancy vs candidate summary.** The candidate said multi-agent
  "fails when subagents must coordinate on shared decisions or writes". The
  post is softer: read-heavy systems are "easier" and conflicting writes are
  "far worse". It does not claim that write-coupled multi-agent systems fail
  outright.
- **On the 2x2.** Off the axis. It is about task structure, not
  instruction style.
- It is also the probable "third-party write-up" through which the
  semiconductor / "2021 automotive chip crisis" anecdote circulated, but the
  anecdote is verbatim from the Anthropic post.

## Trust signals

- **Credibility:** 2. A named founder of a major agent-framework company,
  but secondary commentary with no data, no peer review and a clear product
  interest.

## Follow-up

- **Relevance:** 3. Cite-worthy for the read-vs-write coupling condition. It
  adds no evidence beyond the two primary posts.
- **Guide:** P5 refines. How much context must travel (a brief vs a full
  trace or a single thread) depends on coupling: read-heavy, decomposable
  subtasks can be briefed, while coupled writes should stay in one agent.
- Check whether any controlled study measures multi-agent performance
  against subtask coupling (e.g. MAST 2503.13657, information-bottleneck
  2607.16133 in the candidates).
