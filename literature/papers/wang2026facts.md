---
kind: paper
title: "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs"
authors: ["Yian Wang", "Agam Goyal", "Eshwar Chandrasekharan", "Hari Sundaram"]
institutions: ["University of Illinois Urbana-Champaign"]
year: 2026
venue: "EMNLP 2026 (per Semantic Scholar venue metadata; code repo also named for EMNLP 2026)"
peer_reviewed: true
url: "https://arxiv.org/abs/2608.29028"
code_url: "https://github.com/CrowdDynamicsLab/facts_without_rules_emnlp_2026"
citations: 1
source: "raw/papers/wang2026facts.pdf"
added: "2026-11-14"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/handoff-context-loss]]", "[[concepts/invariants-in-code]]", "[[concepts/brief-anatomy]]"]
tags: [handoff, privacy, boundary-metadata, compression, typed-fields, multi-agent]
---

# Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs

## TL;DR

When an agent compresses an upstream interaction into a handoff, it keeps
the operational facts and drops the *rules* attached to them: audience
limits, ownership, hedges, disclosure caveats. Whether downstream leakage
happens depends on how explicit the rule is. Vague hedges ("use
discretion") are about as bad as no rule at all. Explicit constraints
mostly work. Only a correct, typed audience allowlist removes leakage.

## Claims

- "Summary collapse": handoffs preferentially preserve facts while
  weakening boundary metadata. Fact survival and boundary survival are
  nearly uncorrelated per handoff.
- Marker strength, not just presence, causally controls audience-facing
  leakage.
- Prompt-only mitigation and exact-string redaction only partly work. A
  gold typed allowlist nearly eliminates leakage, and *correctness* of the
  boundary field is what matters.
- The failure is not just a property of multi-agent topology. A no-handoff
  single agent with full markers leaks more than an operationalized handoff.

## Methods

- **BOUND-Handoff** testbed:
  - 36 hand-authored scenarios across 7 domains: scheduling, enterprise IT,
    HR, customer support, legal/compliance, medical admin, project
    management.
  - Crossed with 4 handoff surfaces (explicit summary,
    forwarding-to-summary, memory replay, report writer).
  - And 5 conditions: free text, compressed free text,
    preserve-markers instruction, sectioned template, structured schema.
  - That gives **720 design cells (handoff prompts)**.
- Experiments:
  - E1 uses a stratified 180-prompt subsample.
  - E2 adds 40- and 25-word caps over all 36 scenarios (72 prompts).
  - Downstream leakage probes use 12 matched scenarios x variants x 4
    pressure conditions, typically n=48 per cell; 288 per model for E6/E7.
- Models:
  - Primary: GPT-5-mini and DeepSeek-R1-32B.
  - Targeted replication: Qwen3-32B.
  - Plus an unnamed "flagship" fixed-snapshot model.
  - Temperature 0.1.
- Survival scoring: GPT-5.5 Thinking judge on a 4-level rubric (preserved /
  paraphrased / weakened / absent). Accuracy 0.92, kappa = 0.74 on 100
  human-labeled items.
- Leakage scoring: an exact/alias detector plus a calibrated semantic judge
  (recall 0.95-0.98, precision > 0.97). Two external annotators were used
  for E7.
- Statistics: Fisher exact tests, scenario-bootstrap CIs.
- External check: 493 PrivacyLens traces.

## Results

Boundary survival under compression (sigma_b = boundary-marker survival,
sigma_op = operational-fact survival):

- Fact and boundary survival are decoupled: Pearson r = -0.042 (GPT-5-mini)
  and 0.086 (DeepSeek-R1-32B) over 180 handoffs.
- Handoffs with low sigma_b but high sigma_op (rules dropped, facts kept):
  7 (GPT) and 26 (DeepSeek) of 180.
- Compression stress (Table 2), sigma_b, ordered baseline / 40-word /
  25-word:

  | Model | Baseline | 40-word | 25-word | sigma_op range |
  |---|---|---|---|---|
  | GPT-5-mini | 0.954 | 0.919 | 0.690 | 0.990-0.997 |
  | DeepSeek-R1-32B | 0.880 | 0.774 | 0.580 | 0.972-0.980 |
  | Qwen3-32B | 0.915 | 0.711 | 0.557 | 0.977-1.000 |

  - The flagship at 25 words: sigma_b 0.526 vs sigma_op 0.983.
- At 25 words, 25-39% of markers are scored *absent*; 0% of facts are.
- PrivacyLens traces show it more sharply: sigma_b falls to 0.28 and 41%
  of handoffs land in the low-sigma_b / high-sigma_op quadrant.
- Relabeling the marker from [CONTEXT] to [INSTRUCTIONS] moves sigma_b only
  -0.069 to +0.072. Prompt-level salience is unreliable.

Marker strength and leakage (out of 48):

- No sensitive content plus a marker: 0 leaks.
- Content plus an explicit marker: 2 (GPT) and 1 (DeepSeek).
- Content with no marker: 48 and 37.
- Weak marker ("use discretion"): 44 and 38.
- E8 dose-response, exact detector, GPT / DeepSeek / Qwen:

  | Level | Example | Leaks |
  |---|---|---|
  | L0 | no marker | 44 / 38 / 35 |
  | L1 | vague hedge | 35 / 24 / 18 (73% / 50% / 38%) |
  | L2 | soft suggestion | 6 / 5 / 2 |
  | L3 | "X is confidential" | 2 / 2 / 3 |
  | L4 | "do not disclose X" | 2 / 2 / 1 |

  - The L1 to L2 step is the essential transition.
  - The semantic judge preserves the shape: GPT 48 / 44 / 10 / 8 / 2.
  - Qwen column order is reconstructed from the PDF text extraction and
    matches the abstract's 73/50/38%.
- Agents rarely add missing boundaries on their own: 3 of 40 neutral
  handoffs (7.5%), in a single-author review.

No-handoff control (E5): a single agent with the full markers still leaks
20/48 (GPT) and 11/48 (DeepSeek). That is worse than the operationalized
handoff (2/48).

Enforcement:

- Prompt-only mitigation leaks 58/288 (GPT) and 42/288 (DeepSeek), with
  task success near ceiling.
- Exact-string redaction gets exact leakage to 0/288, but semantic residue
  remains. The independent dual-annotator floor is 7.7%, kappa = 0.39.
- Gold typed allowlist: 0/48, 0/48, 4/48 (Qwen), at full utility.
- Label error degrades it gradually: 5% error gives 2-3 leaks; 30% gives
  11-15 leaks at utility 0.87-0.91.
- Negation-flipped allowlist: 44, 38 and 35 leaks.

Multi-hop: under partial memory recall, cumulative sigma_b loss from hop 1
to hop 3 is -0.381 (GPT) and -0.277 (DeepSeek). Under full replay the CI
includes zero.

## Critique / open questions

- **Setup verified, with one correction.** 36 scenarios and 720 are right,
  but 720 is the number of *design cells / handoff prompts* (36 x 4 surfaces
  x 5 conditions), not runs. The headline E1 analysis uses a 180-prompt
  subsample. The leakage tests use 48-sample cells on 12 scenarios.
  (Separately, E8 re-scores 720 outputs.)
- The abstract's "uncompressed free-text sigma_b ~0.80, 25-word ~0.57" fits
  DeepSeek and Qwen:
  - DeepSeek free text 0.781, 25-word 0.580.
  - Qwen 25-word 0.557.
  - GPT-5-mini is much higher: free text 0.976, 25-word 0.690.
  - So the abstract states the weaker models' figures as if general.
- Scenarios and audiences are synthetic and hand-authored. Sensitive-fact
  leakage is a privacy instance of a general problem: rules attached to
  facts don't survive summarization.
- Survival is LLM-judged (GPT-5.5, kappa 0.74). Leakage uses deterministic
  plus calibrated detectors, i.e. task-outcome-like checks. Downstream
  utility is reported.
- Most human labels come from the authors, blind to condition. Independent
  annotation covers only E7.
- Models are mid-tier: GPT-5-mini and 32B distills. The flagship
  replication covers compression only.
- 2x2 position: the dose-response separates *how* a constraint is phrased.
  Vague, discretion-style intent language fails; operational imperatives
  work. A typed field beats both. For boundaries, a terse-intent brief
  with soft language is the failure case. Rules must be explicit (L2+),
  and ideally carried in code-like typed fields.

## Trust signals

- UIUC (Chandrasekharan, Sundaram).
- Semantic Scholar lists the venue as EMNLP, with 1 citation (checked
  2026-11-14). The code repo is named `..._emnlp_2026`.
- Code, prompts and raw labels released.
- Human-validated judge, Fisher tests with large risk ratios (20-40x for
  E3), external PrivacyLens check, three model pipelines.
- **Credibility:** 4. Peer-reviewed (EMNLP per S2), a rigorous controlled
  design with released artifacts, and replication across pipelines. Held
  back by synthetic scenarios, mostly author-produced labels and mid-tier
  models.

## Follow-up

- **Relevance:** 4. Direct controlled evidence that handoffs keep facts and
  drop rules, and that rule phrasing and typing decide whether they hold.
  Canonical for the handoff side of P3 and P5.
- **Guide:** P3 supports.
  - Prompt-only mitigation leaks 15-20%.
  - Only a correct typed allowlist gets leakage to 0/48.
  - A corrupted typed field is as bad as none.
  - So hard boundaries belong in typed, machine-checked fields.
- **Guide:** P5 refines.
  - Compression keeps facts (sigma_op about 0.98) and strips rules (sigma_b
    0.53-0.69 at 25 words).
  - A brief or handoff must carry constraints explicitly, phrased as
    operational instructions. "Use discretion" leaks 38-73%; "X is
    confidential" leaks about 4-6%.
  - Readers almost never re-derive missing rules (7.5%).
- Also bears on Q3 (invariant boundary): audience and ownership rules are a
  class that must stay explicit regardless of model strength. The flagship
  shows the same collapse.
