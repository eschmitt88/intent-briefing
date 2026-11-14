---
kind: paper
title: "When Do Multi-Agent Systems Help? An Information Bottleneck Perspective"
authors: ["Wendi Yu", "Lianhao Zhou", "Xiangjue Dong", "Sai Sudarshan Barath", "Declan Staunton", "Byung-Jun Yoon", "Xiaoning Qian", "James Caverlee", "Shuiwang Ji"]
institutions: ["Texas A&M University", "Brookhaven National Laboratory"]
year: 2026
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2607.16133"
code_url: "https://github.com/divelab/MAS-SAS"
citations: 2
source: "raw/papers/yu2026when.pdf"
added: "2026-11-14"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/context-engineering]]"]
tags: [multi-agent, single-agent, information-bottleneck, relay-compression, capability]
---

# When Do Multi-Agent Systems Help? An Information Bottleneck Perspective

## TL;DR

A multi-agent system (MAS) differs from a single agent (SAS) only through
*bounded relays* between isolated contexts. With unbounded relays a MAS can
simulate any SAS. Gains appear when cutting noisy context outweighs losing
task-relevant information in the relay. The theory predicts that stronger
models gain less from compression and lose more from relay loss. The
experiments partly bear that out.

## Claims

- Theorem: under infinite relay bandwidth, MAS is equivalent to SAS. So any
  non-trivial MAS effect comes from relay compression.
- Per-stage MAS gain = context-reduction benefit minus capability-weighted
  relay-loss cost. The effective beta rises with model capability.
- MAS helps consistently when relays are near-sufficient, especially for
  weaker models. Gains shrink or reverse when relays lose information,
  especially for stronger models.
- The operative mechanism is context isolation, not decomposition. A
  single agent given the same sub-instructions (SAS-Plan) does worse than
  plain SAS.

## Methods

- Three prototypes, all under the same step budget:
  - **SAS**: single shared context.
  - **SAS-contextflow**: same planner decomposition, full shared context.
  - **MAS**: same decomposition, isolated workers joined by compressed
    relays.
  - The key contrast is MAS vs SAS-contextflow.
- Five benchmarks, labelled by estimated relay complexity delta:
  - Low (delta near 0): ALFWorld (valid_unseen), WideSearch (66 English
    tasks), TravelPlanner-CS.
  - Higher: WebShop (100 items), TravelPlanner-HC (delta > 0); WorkBench
    multi-domain (210 tasks, delta >> 0).
- Three models as a capability axis: Qwen2.5-7B-Instruct ("weak"),
  GPT-4o-mini ("medium"), Qwen3.5-27B-AWQ-4bit ("strong").
- Temperature 0, a single run per cell. 18 comparisons in all.
- Ablations: SAS-Plan, and deliberately insufficient relays on ALFWorld and
  WebShop.

## Results

MAS minus SAS-contextflow, ordered weak / medium / strong:

- Low-complexity relays (all positive, shrinking with capability):
  - ALFWorld SR +0.194 / +0.157 / +0.023
  - WideSearch Item-F1 +0.079 / +0.063 / +0.028
  - TravelPlanner-CS +0.011 / +0.183 / +0.028
- Higher-complexity relays:
  - WebShop +0.080 / +0.086 / **-0.003**
  - TravelPlanner-HC +0.017 / +0.161 / **-0.233**
  - WorkBench **-0.005 / -0.086 / -0.014** (negative for all three)
- Insufficient-relay ablation (Table 4): removing downstream-needed fields
  always hurts. ALFWorld -0.015 / -0.015 / -0.052; WebShop -0.008 / -0.078 /
  -0.010.
- WorkBench case study (App. C.3, task `multi_domain_165`):
  - The task: "make a backlog task ... with a deadline of next Friday".
    Today is Thu 2023-11-30, so the answer is 2023-12-08.
  - SAS-contextflow succeeds on both models.
  - MAS fails on both, by different mechanisms:
    - GPT-4o-mini derives the right date, but its write call is blocked by
      the reader-phase tool whitelist. The relay collapses to
      `RESULT: NO_ACTION, FIELDS:{}`.
    - Qwen3.5-27B resolves "next Friday" to 2023-12-01 and locks that wrong
      date into the relay fields, which the writer then executes.
  - The relay carries only concrete write-tool fields, not the evidence
    needed to re-derive them.

## Critique / open questions

- **Verified with qualifications.**
  - "Stronger models lose more to relay loss" is the theoretical
    prediction. Empirically it holds on WebShop and TravelPlanner-HC, where
    the sign flips at the strongest model.
  - On WorkBench, the loss is largest for the *medium* model (-0.086), not
    the strongest (-0.014). WorkBench shows uniform relay loss, not a
    capability gradient.
  - The WorkBench "deadline drop" case is real but is a single illustrative
    task. For GPT-4o-mini the failure is a tool-whitelist artifact as much as
    relay compression.
- Evidence is thin:
  - One run per cell at temperature 0, with no confidence intervals. Several
    deltas (-0.003, -0.005, -0.014, +0.011) are almost certainly within
    noise.
  - The "capability axis" is three models from two families, the "strong"
    one 4-bit quantized. Capability is confounded with family.
  - No frontier models.
- The outcome metrics are task outcomes (success rate, F1, pass rates),
  which is good.
- The relay-complexity labels (delta) are assigned by the authors from task
  structure, not measured.
- 2x2 position: not about brief style. It is about what an inter-agent
  relay (in effect a brief to the next worker) must carry. Relays reduced to
  terse "fields" lose the evidence that lets a strong reader re-derive or
  check them. That is an argument for verbose-intent handoffs (context plus
  rationale) when downstream decisions are globally coupled.

## Trust signals

- Texas A&M (Shuiwang Ji, Caverlee) and Brookhaven.
- Preprint; Semantic Scholar lists only arXiv, with 2 citations (checked
  2026-11-14). Code released.
- **Credibility:** 2. Formal framing and released code, but single-run
  results with no CIs, small effect sizes, a confounded three-model
  capability axis, and no frontier models.

## Follow-up

- **Relevance:** 3. Gives a clean conceptual account of when splitting work
  across agents costs information. The empirical support for the capability
  claim is weak.
- **Guide:** P5 supports.
  - When downstream decisions depend on exact upstream evidence (WorkBench,
    TravelPlanner hard constraints), compressed relays lose to shared
    context.
  - The loss can grow with reader strength (TravelPlanner-HC: +0.161 for
    GPT-4o-mini vs -0.233 for Qwen3.5-27B).
  - Hand over the evidence behind a decision, not just the decided fields.
  - The suggested refinement is weak evidence only.
- Bears on Q2 (capability boundary): a hint that stronger readers are
  hurt more by lossy handoffs. It needs replication with frontier models and
  multiple seeds.
