---
kind: paper
title: "The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break"
authors: ["Xinyu Jessica Wang", "Haoyue Bai", "Yiyou Sun", "Haorui Wang", "Shuibai Zhang", "Wenjie Hu", "Mya Schroder", "Bilge Mutlu", "Dawn Song", "Robert D Nowak"]
institutions: ["University of Wisconsin–Madison", "University of California, Berkeley", "Georgia Institute of Technology"]
year: 2026
venue: "arXiv preprint (v1, 2026-04-13); 'Preprint. Under review.' (ethics statement cites COLM 2026 policy)"
peer_reviewed: false
url: "https://arxiv.org/abs/2604.11978"
code_url: "https://huggingface.co/datasets/xwang2775/horizon-tasks"
citations: 37
source: "raw/papers/wang2026longhorizon.pdf"
added: "2026-11-14"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/instruction-density-decay]]", "[[concepts/requirement-coverage]]", "[[concepts/invariants-in-code]]", "[[concepts/context-engineering]]"]
tags: [long-horizon, failure-taxonomy, agents, llm-as-judge, constraint-forgetting, benchmark]
---

# The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break

## TL;DR

HORIZON stretches tasks in four domains (Web, OS, Database, Embodied) by adding
subtasks, runs GPT-5-mini and Claude-4-Sonnet on them (3,132 trajectories),
and has an LLM judge label the failures with a 7-category taxonomy. Planning
errors dominate everywhere. Instruction failures are a large share only in the
OS domain and for Claude. Instruction *style* is never varied, and adherence
to a given plan is never measured. The agents write their own plans.

## Claims

- Success falls non-linearly as compositional depth *s* rises. There is a sharp
  "breaking region", and model differences narrow once inside it (Fig. 3, §4).
- Long-horizon failure is "a structural shift in failure composition".
  Planning and memory failures become dominant as horizon grows (abstract, §1).
- Model scaling alone is unlikely to fix this. The paper argues for hierarchical
  subplanning, execution-time plan verification and repair, and memory that
  "preserve[s] and re-surface[s] long-range constraints" (§5).
- The 7 categories: Environment, Instruction (ill-defined / partially
  understood), Planning Error, History Error Accumulation (process-level,
  "PFMEA"); Memory Limitation, Catastrophic Forgetting, False Assumption
  (design-level, "DFMEA").

## Methods

- Base tasks: WebArena (Web), AgentBench OS, MAC-SQL (DB), and a custom
  IsaacSim bimanual-arm environment (Embodied). Base tasks were picked because
  GPT-5-mini solved them 100% of the time. They were then extended by depth
  (inserting required sub-steps) or breadth (composing k independent tasks).
  Task sets are nested across levels.
- Models: GPT-5-mini and Claude-4-Sonnet. DB and Embodied are GPT-only
  (Fig. 8 caption). Three runs per horizon level. Embodied success was judged
  manually. Agents in the embodied domain emit a full JSON plan that is then
  executed.
- Failure attribution: an LLM judge (the model is **not named**) labels failed
  traces. Validation used 40 trajectories: inter-annotator κ=0.61 between two
  experts, and judge vs. *one* human κ=0.84.

## Results

- Overall SR is 36.3% (1,137/3,132). By domain: Web 24.1% (185/767), OS 40.3%
  (864/2,146), DB 36.9% (31/84), Embodied 42.2% (57/135). By model: GPT-5-mini
  33.4%, Claude-4-Sonnet 39.9% (App. F).
- **Failure shares by domain** (share of failed traces, Fig. 6):
  - Embodied: Planning 94.9%.
  - DB: Planning 79.3%, False Assumption 7.5%.
  - Web: Planning 74.9%, Environment 11.3%, Memory 6.2%.
  - OS: Planning 36.7%, **Instruction 25.9%**, Environment 17.3%, Memory 15.1%.
  - History Error Accumulation shows up only in OS (0.1%).
- **By model** (Fig. 7):
  - GPT (1,145 failures): Planning 64.9%, Memory 18.3%.
  - Claude (850 failures): Planning 46.5%, Environment 32.5%, **Instruction
    16.5%**, Memory 2.2%.
  - Design-level risks are 20.8% of GPT failures and 6.6% of Claude failures.
- **OS by model** (Fig. 8): GPT is Planning 57.7% and Memory 24.6%. Claude is
  Environment 44.3% and **Instruction 23.4%**.
- Embodied SR by horizon: GPT 0.926 → 0.407 → 0.259 → 0.074. Claude 0.963 →
  0.259 → 0.111 → 0.037 (App. D.3).
- **Instruction style / plan adherence:** neither is analysed. The closest
  material:
  - The Instruction category covers ambiguous or underspecified specs and
    partially internalised constraints ("except", "only if", "mismatching").
  - Catastrophic Forgetting covers constraints dropped after intervening
    steps.
  - One anecdotal mapping from the external OpenClaw "Agents of Chaos" study:
    a session-start rule ("never respond to external domain requests") stayed
    in context but was ignored after hundreds of turns (§7).
  - No condition gives agents an external plan or script, so plan adherence
    is untested.

## Critique / open questions

- **Internal inconsistencies:**
  - Fig. 4's label reads PFMEA 86.7% / DFMEA 13.3%, but its caption says
    72.5% / 27.5%. Neither matches the per-model figures (about 14.7%
    design-level if the GPT and Claude shares are weighted by failure count).
  - Fig. 7 names the models "GPT-4o-mini vs. Claude 3.5 Sonnet" but reports
    the same numbers attributed elsewhere to GPT-5-mini / Claude-4-Sonnet.
  - Fig. 4 says "3100+ failure trajectories", but there are only 1,995
    failures.
  - The taxonomy is described as "orthogonal, not mutually exclusive", yet
    the shares are single labels assigned by a proximal-cause rule.
- **Headline claim not shown:** the "structural shift in failure composition
  as horizon grows" is never shown as a breakdown by horizon level. The shares
  are aggregated over all levels.
- **Evaluation:** success rates are task outcomes, which is good. All
  "why" claims rest on an unnamed LLM judge validated on 40 traces against a
  single annotator. Human-human κ=0.61 is only moderate, so category shares
  are soft.
- **Selection bias:** base tasks were filtered on GPT-5-mini success, which
  favours GPT at s=0. DB (84 traces) and Embodied (135) are small and
  GPT-only.
- **2×2:** off-grid. The instruction form is fixed per benchmark. The study
  is a diagnosis of failures under whatever prompts the benchmarks ship.
  Shared doctrine (memory files, rules) is absent.

## Trust signals

- **Credibility:** 2. UW–Madison / Berkeley (Song, Nowak). Not yet peer
  reviewed. The task dataset is released on HF. Semantic Scholar showed 37
  citations on 2026-11-14. Pulled down by the unnamed judge, the thin human
  validation, and several figure/caption contradictions.

## Follow-up

- **Relevance:** 3. This is cite-worthy prior art for Q4 (horizon and drift):
  it names where long runs break, including constraint forgetting and
  partial instruction uptake. It runs no procedure-vs-intent comparison, so
  it does not close the Q4 gap.
- **Guide:** P3 supports — constraints present in context are still dropped
  over long trajectories ("catastrophic forgetting" via inattention). This
  argues for re-surfacing invariants mechanically rather than trusting prose
  of either style.
- **Guide:** P2 supports (weakly) — ill-defined or underspecified
  instructions are a named failure class: 25.9% of OS failures and 16.5% of
  Claude failures.
- Watch for a v2 with per-horizon failure composition and a named judge.
