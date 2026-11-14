---
kind: paper
title: "What Prompts Don't Say: Understanding and Managing Underspecification in LLM Prompts"
authors: ["Chenyang Yang", "Yike Shi", "Qianou Ma", "Michael Xieyang Liu", "Christian Kästner", "Tongshuang Wu"]
institutions: ["Carnegie Mellon University"]
year: 2025
venue: "ACL (per Semantic Scholar venue metadata; arXiv v3 2026-04-24)"
peer_reviewed: true
url: "https://arxiv.org/abs/2505.13360"
code_url: "https://github.com/malusamayo/underspec-analysis"
citations: 55
source: "raw/papers/yang2025what.pdf"
added: "2026-11-14"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["[[concepts/requirement-coverage]]", "[[concepts/instruction-density-decay]]", "[[concepts/cross-model-prompt-transfer]]"]
tags: [underspecification, requirements, prompt-optimization, model-drift, instruction-following]
---

# What Prompts Don't Say: Understanding and Managing Underspecification in LLM Prompts

## TL;DR

Models often satisfy requirements a prompt leaves unstated, but this is
fragile across prompt and model-version changes. Stating *every*
requirement does not fix it: accuracy on stated requirements falls as their
number grows. The best results come from choosing *which* requirements to
state (or restructuring how they are stated), not from maximal coverage.

## Claims

- LLMs "guess" unspecified requirements in 41.1% of cases (abstract, §3.2).
- Under-specified prompts are ~2x as likely to regress across model or
  prompt changes, sometimes by more than 20%.
- Specifying all requirements does not consistently help: models have
  limited instruction-following capacity and requirements can conflict.
  Specifying everything is called "an anti-pattern" (§3.4).
- Requirements-aware prompt optimization improves performance by 4.8% on
  average over baselines; the "what to specify" optimizer also cuts prompt
  tokens by 41-45% (abstract says -43%).

## Methods

- 3 main tasks (code-explain on CommitPackFT, trip-advisory on UltraChat,
  product-gen on Amazon ESCI), 2 more in Appendix D (health-consulting on
  HealthBench, lesson-planning). 200 examples per task, split 15/35/50
  (train n=30, test n=100).
- 20 requirements per task (60 total for the main tasks), elicited from
  real vendor/GPT prompts, LLM brainstorming and error analysis, then
  filtered by 3 human annotators.
- Prompts built cyclically: each holds N=10 consecutive requirements, so
  every requirement is specified in some prompts and unspecified in others.
  240 synthetic prompts in all; >1.5M LLM calls.
- Per-requirement validators: Python scripts or LLM validators, with 95.6%
  average human-LLM agreement on a sampled subset.
- Models: Llama-3.3-70B-Instruct, gpt-4o-2024-08-06, o3-mini (§3.2). For
  model drift: gpt-4o 05-13/08-06/11-20 and Llama-3/3.1/3.3-70B (§3.3).
  For density: N = 1, 5, 10, 19 on Llama-3.3-70B and gpt-4o (§3.4).
- Optimization (§4): starts from the N=19 prompt on Llama-3.3-70B. A budget
  of 9 explored prompts. Compared: OpenAI's static optimizer, DSPy COPRO,
  COPRO-R (COPRO scored on all requirement validators), and a Bayesian (TPE)
  search over which requirements to include.
- Agentic case study (App. E): a 25-requirement Cursor-community front-end
  system prompt, run in OpenHands with Qwen3-30B-A3B. Output scored by
  gemini-2.5-flash.

## Results

Exact figures and the conditions they hold under:

- **41.1%**: the share of (requirement x LLM+prompt) cases where an
  *unspecified* requirement still reaches >=98% accuracy. It is averaged over
  Llama-3.3-70B, gpt-4o-08-06 and o3-mini. It does **not** mean "readers
  guess unstated requirements right 41% of the time" in a per-output sense.
  The companion number: mean accuracy on a requirement drops by **22.6%**
  (up to 93.1%) when it is unspecified rather than stated.
  - Stronger models guess more: o3-mini 44.7%, which the paper calls a 20.2%
    increase over Llama-3.3-70B.
  - Format requirements are guessed 70.7% of the time, conditional
    requirements only 22.9%.
  - 65.2% of requirements taken from existing developer prompts are guessed
    when omitted, so real prompts carry much redundancy.
  - 65% of requirements are guessed by at least one LLM+prompt combination.
- **"2x"** comes from two separate measurements:
  - *Across model updates* (within-family version changes only): 22.9% of
    cases regress. **5.9%** of unspecified requirements regress by >20%,
    against **3.0%** of specified ones (Fig. 3). Example: gpt-4o 05-13 to
    08-06 is 48% less likely to "produce skimmable outputs".
  - *Across prompts*: the standard deviation of unspecified-requirement
    accuracy is **8.9%**, more than 2x the specified case. Controlling for
    requirement conflicts it is 7.9% vs 0.8%.
- **Density decay** (§3.4, Fig. 4): requirements stated alone are met
  **98.7%** of the time. With **19** specified together, gpt-4o-08-06 averages
  **85.0%** on the specified ones and Llama-3.3-70B **79.7%**. The "19% drop"
  in Fig. 1 is this Llama gap (98.7 to 79.7).
  - 37.5% of requirements drop by >5%.
  - Some drops have no obvious conflict, e.g. "use analogies and examples"
    falls 81.3% on gpt-4o.
- **+4.8%** (Table 2) is the mean absolute accuracy gain of the two
  requirement-aware optimizers over the *original N=19 prompt* on
  Llama-3.3-70B, test split:
  - COPRO-R: +5.8 pts. code-explain 0.754 to 0.842, trip-advisory 0.803 to
    0.811, product-gen 0.835 to 0.913.
  - Bayesian subset selection: +3.8 pts (0.773 / 0.810 / 0.922), using
    41-45% fewer tokens.
  - Requirement-agnostic optimizers: about +2.8% on two tasks, -1.1% on
    trip-advisory.
  - The Bayesian optimizer mostly dropped global, format and
    developer-written requirements (56.5% / 77.0% / 57.9% dropped, against
    52.8% on average). These are the ones models follow by default.
  - Agentic website-gen: original prompt 0.441, COPRO 0.504, COPRO-R 0.535,
    Bayesian 0.474. The Bayesian prompt is 71.9% shorter.
- Appendix D: the patterns reportedly hold on the two extra tasks and on
  gemini-2.5-flash.

## Critique / open questions

- **The candidate summaries are both right, but each is half the story.**
  Summary (a) gives the abstract's numbers and drops the conditions.
  Summary (b) has the density and optimization figures right, with one fix:
  the +4.8% baseline is the N=19 prompt, i.e. "specify 19 of 20". The paper's
  own message is *selective* specification: state what the model won't do
  by default (conditional and corner-case requirements), leave out what it
  already does (format, global), and monitor everything.
- Evaluation is per-requirement satisfaction, mostly by LLM validators
  (95.6% human agreement). It is not end-task success. The agentic case is
  a single prompt scored by an LLM judge (gemini-2.5-flash). Under this
  project's weighting this is closer to rubric evidence than task outcome,
  though the validators are narrow and checkable.
- The models are now dated (gpt-4o, Llama-3.3-70B, o3-mini). The trend that
  stronger models guess more and follow long lists better suggests the
  density penalty shrinks for frontier models, but this is untested here.
- "Model updates" are within-family version bumps, not cross-vendor
  transfer.
- The optimization gains are uneven. Trip-advisory barely moves under any
  method, within one SD. Most of the Bayesian gain is from product-gen.
  Only Llama-3.3-70B was optimized.
- Small scale, by the authors' own account: 60 requirements, 240 synthetic
  prompts. No user study.
- 2x2 position: the requirements are declarative constraints (what, not
  how), so the paper varies coverage along the *intent* row, from terse
  toward exhaustive. It says nothing about procedure. Its finding is that
  neither end of that row is optimal.

## Trust signals

- CMU (Kästner, Wu); one author since moved to Google DeepMind.
- Code and data released.
- Semantic Scholar lists the venue as ACL, with 55 citations (checked
  2026-11-14). The PDF itself carries no venue line.
- Validators human-checked. Clear limitations section.
- **Credibility:** 4. Peer-reviewed (ACL per S2), released code and data,
  human-validated validators, careful design. Held back by LLM-validator
  scoring rather than task outcomes, a small requirement set and older
  models.

## Follow-up

- **Relevance:** 5. This is the primary source for writing-guide P2, and it
  qualifies that line rather than simply supporting it.
- **Guide:** P2 refines (partly contradicts "coverage beats brevity" as
  worded).
  - Unstated requirements are met reliably (>=98%) in 41.1% of cases. They
    regress by >20% across model updates about 2x as often as stated ones
    (5.9% vs 3.0%).
  - But stating everything costs accuracy (19 requirements: gpt-4o 85.0%,
    Llama 79.7%, vs 98.7% stated alone).
  - Selective specification beats near-exhaustive specification by +3.8 to
    +5.8 pts.
  - Suggested rewrite: "State the requirements the reader won't meet by
    default (conditional, corner-case, task-specific); omit what it already
    does; re-check unstated requirements on every model change."
- Also bears on `instruction-density-decay` (Q3/P3: what to keep explicit)
  and on `cross-model-prompt-transfer` (re-validate on model change).
- Watch for a replication on frontier models and on agentic task outcomes.
