---
kind: paper
title: "Intelligent AI Delegation"
authors: ["Nenad Tomašev", "Matija Franklin", "Simon Osindero"]
institutions: ["Google DeepMind"]
year: 2026
venue: "arXiv preprint (2602.11865)"
peer_reviewed: false
url: "https://arxiv.org/abs/2602.11865"
code_url: null
citations: 20
source: "raw/papers/tomasev2026intelligent.pdf"
added: "2026-11-14"
relevance: 2
credibility: 2
status: skimmed
related_experiments: []
related_concepts: ["[[concepts/brief-anatomy]]", "[[concepts/handoff-context-loss]]", "[[concepts/invariants-in-code]]", "[[concepts/degrees-of-freedom]]"]
tags: [delegation, multi-agent, position-paper, verification, accountability, authority-gradient]
---

# Intelligent AI Delegation

## TL;DR

A conceptual framework paper from Google DeepMind with no experiments. It
defines "intelligent delegation" as task allocation plus transfer of authority,
responsibility and accountability, "clear specifications regarding roles and
boundaries, clarity of intent", and trust mechanisms. It proposes protocols
(contract-first decomposition, verifiable completion, permission handling,
monitoring) for human↔AI and AI↔AI delegation chains. It is useful as
vocabulary and a checklist of what a delegation hand-off must carry. It is not
evidence.

## Claims

- Current multi-agent delegation relies on "simple heuristics" and hard-coded
  control flow that doesn't adapt or recover from failures.
- Delegation is characterized along axes: delegator and delegatee (human/AI);
  task traits (complexity, criticality, uncertainty, duration, cost,
  resources, constraints, verifiability, reversibility, contextuality,
  subjectivity); granularity; autonomy ("full autonomy" vs "far more specific
  and prescriptive"); monitoring; reciprocity.
- The **authority gradient** carries over from aviation and medicine. A more
  capable delegator "may make erroneous assumptions about the knowledge of the
  less experienced worker, resulting in under-specified requests". A delegatee
  may be reluctant to challenge a request because of sycophancy or
  instruction-following bias.
- The **zone of indifference**: as delegation chains lengthen, "subtle intent
  mismatches or context-dependent harms" propagate. Agents need "dynamic
  cognitive friction" so they challenge contextually ambiguous requests.
- **Contract-first decomposition**: delegate a sub-task only if its outcome can
  be precisely verified. Otherwise decompose further. The final specification
  "must explicitly define roles, resource boundaries, progress reporting
  frequency" and required capabilities, "beyond simple input-output pairs".
- **Atomic execution** (strict spec, narrow scope) is distinguished from
  **open-ended delegation** (authority to decompose and pursue sub-goals). The
  level of autonomy should be set by trust and task traits, not fixed.
- Below a "complexity floor" (low criticality, high certainty, short duration),
  the overhead of delegation exceeds its value, so execute directly.

## Methods

- Synthesis of organizational theory (span of control, principal-agent,
  authority gradient, zone of indifference, transaction costs, contingency
  theory) and prior AI work (expert systems, hierarchical/feudal RL, contract
  net, MCP/A2A). The paper then proposes a framework of 5 pillars mapped to 9
  protocol areas, plus ethics and protocol-extension sections.

## Results

- None empirical. No tasks, models, or measurements.

## Critique / open questions

- There is no evaluation of any kind, so it cannot move an evidence tag. Its
  value is conceptual framing and terminology.
- "Clarity of intent" appears in the definition but is barely developed. The
  operational content is about contracts, verification, permissions and
  monitoring, not about how to word the goal.
- 2×2 placement: it doesn't take a side on intent vs procedure for the
  instruction itself. It argues that the *interface* be explicit (roles,
  boundaries, verification criteria, reporting cadence) and that autonomy be
  matched to task traits. That fits "intent plus hard constraints, with
  invariants made checkable" more than "full script".
- Shared doctrine is assumed to be absent in open agentic markets. That is the
  opposite of the in-house subagent case this project cares about, where
  CLAUDE.md, rules and skills act as doctrine. Its prescriptions may be heavier
  than an intra-system hand-off needs.
- It is scoped to web-scale agent economies (markets, bids, smart contracts),
  much of which doesn't apply to subagent briefs.

## Trust signals

- **Credibility:** 2. Google DeepMind authors, but an un-peer-reviewed position
  paper with no data or code. 20 citations (Semantic Scholar, 2026-11-14).

## Follow-up

- Its "authority gradient → under-specified requests" claim is cited from
  aviation and medicine (Alkov et al. 1992, Cosby & Croskerry 2004). It is a
  candidate pointer if the project wants human-factors evidence for P2.
- **Relevance:** 2. A framing source for delegation hand-offs (what a brief
  must carry), with no measured evidence.
- **Guide:** P3 supports (conceptual only). Contract-first decomposition and
  verifiable completion put invariants in checkable contracts rather than
  prose. P5 supports (conceptual). The authority gradient and the transfer of
  context in long chains motivate handing over context explicitly.
