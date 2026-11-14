---
kind: paper
title: "How Many Instructions Can LLMs Follow at Once?"
authors: ["Daniel Jaroslawicz", "Brendan Whiting", "Parth Shah", "Karime Maamari"]
institutions: ["Distyl AI"]
year: 2025
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2507.11538"
code_url: "https://distylai.github.io/IFScale"
citations: 29
source: "raw/papers/jaroslawicz2025instructions.pdf"
added: "2026-11-14"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/instruction-density-decay]]", "[[concepts/requirement-coverage]]", "[[concepts/brief-anatomy]]"]
tags: [instruction-following, instruction-density, ifscale, primacy, reasoning-models]
---

# How Many Instructions Can LLMs Follow at Once?

## TL;DR

IFScale asks for a business report that includes N required keywords, with N
from 10 to 500. Across 20 models (23 configurations, 5 seeds each), the best
model (gemini-2.5-pro) reaches 68.9% at 500. Frontier reasoning models stay
near-perfect up to about 100–250 instructions before declining. The curve has
three shapes that track model tier, and primacy bias peaks around 150–200
instructions.

## Claims

- Even the best frontier models reach only 68% at 500 instructions.
- Three degradation patterns:
  - **threshold:** reasoning models, e.g. o3, gemini-2.5-pro
  - **linear:** gpt-4.1, claude-3.7-sonnet
  - **exponential:** gpt-4o, llama-4-scout, claude-3.5-haiku, with floors at
    7–15%
- Primacy effect (error ratio of the last third vs the first third) starts near
  1, peaks around 150–200 instructions, and converges to about 1.0–1.5 at 300+.
  Front-loading important instructions helps at moderate density, less at
  extreme density.
- Under load, errors shift toward omission rather than modification.
- Reasoning models pay large latency costs: o4-mini goes from 12 s at 10
  instructions to 436 s at 250.

## Methods

- One task: a multi-section business report. Each instruction is "Include the
  exact word {keyword}". Keywords are 500 hard business terms from SEC 10-K
  filings, filtered for difficulty and semantic redundancy.
- N ∈ {10, 20, …, 500}, 5 seeds, through OpenRouter at default parameters,
  reasoning effort "high" where applicable.
- **Scoring:** deterministic regex for exact match. An 80%-prefix match counts
  as a modification error.
- **Retries:** rejected outputs (keyword lists, refusals, or "incoherent" by an
  o4-mini check) are retried. Core-task coherence is judged by o4-mini.

## Results

Accuracy (%) by density (Table 1, mean of 5 seeds):

| Model (pattern) | 10 | 50 | 100 | 250 | 500 |
|---|---|---|---|---|---|
| gemini-2.5-pro (threshold) | 100 | 99.6 | 98.4 | 84.8 | **68.9** |
| o3 high (threshold) | 100 | 99.6 | 98.2 | 97.8 | 62.8 |
| grok-3 (non-reasoning) | 100 | 100 | 98.8 | 86.2 | 61.9 |
| claude-3.7-sonnet (linear) | 100 | 99.6 | 94.8 | 72.9 | 52.7 |
| claude-opus-4 (r) | 92 | 99.6 | 81.8 | 81.5 | 52.1 |
| gpt-4.1 (linear) | 98 | 98.8 | 95.4 | 74.0 | 48.9 |
| claude-opus-4 | 100 | 100 | 94.6 | 67.9 | 44.6 |
| claude-sonnet-4 | 100 | 98.0 | 94.4 | 77.2 | 42.9 |
| claude-sonnet-4 (r) | 100 | 100 | 94.8 | 80.0 | 39.9 |
| o4-mini | 100 | 99.6 | 97.8 | 86.8 | 34.4 |
| deepseek-r1 | 98 | 94.8 | 86.8 | 49.1 | 30.9 |
| gpt-4o (exponential) | 94 | 82.8 | 49.0 | 22.2 | 15.4 |
| claude-3.5-haiku (exp.) | 98 | 78.0 | 43.4 | 16.6 | 8.5 |
| llama-4-scout (exp.) | 100 | 54.4 | 27.2 | 9.3 | 6.7 |

- **Curve shape by tier:**
  - **Top reasoning models:** flat at about 98–100% up to 100–250
    instructions, then a steeper decline with rising variance.
  - **Strong non-reasoning frontier models** (gpt-4.1, Claude 3.7/4): roughly
    linear decline past about 100.
  - **Small and older models:** collapse within the first 50–100 instructions
    to 7–15% floors.
- **Primacy ratios:** e.g. gemini-2.5-pro 1.67 at 250 and 1.78 at 500;
  gpt-4.1-mini 3.37 at 100. Most converge to 1.0–1.5 at extreme density.
- **Thinking mode:** helps somewhat (o3-high > o3-medium at high density), but
  claude-sonnet-4 (r) is *below* its non-thinking variant at 500.
- **Coherence:** holds for most models. o3 and o4-mini fall below the coherence
  threshold, partly because they write short reports (about 1,500 tokens at
  500 instructions).

## Critique / open questions

- **Verified against the candidate summary.** "Best ~68% at 500" is correct
  (gemini-2.5-pro 68.9%). "Primacy bias" is correct, but it is
  non-monotonic: it peaks at 150–200, then fades.
- **Construct validity is narrow:**
  - Keyword inclusion is the easiest possible instruction type: independent,
    non-conflicting, no judgement.
  - One task, one domain.
  - It tests *recall of a list*, not adherence to behavioural rules across an
    agentic run.
  - Real system prompts have far fewer but far harder instructions.
- **Outcome metric is deterministic, which is good.** Retry filtering and
  coherence use an o4-mini judge, which is a minor concern.
- **Single lab, industry preprint.** No significance tests beyond seed SD.
- **2×2 placement:** the extreme *terse* row as a quantity dose. Silent on
  intent vs procedure.
- **For brief-writing the main lesson is capacity, not fragility.** At the
  frontier, tens of terse requirements cost almost nothing (≥98% to 100
  instructions for top reasoning models). The risk zone starts in the hundreds,
  or much earlier for small or fast models such as cheap subagents.

## Trust signals

- **Credibility:** 3. Industry preprint (Distyl AI) with no peer review. The
  benchmark and all results are open-sourced, grading is deterministic, there
  are 5 seeds and 20 models. The task is narrow and synthetic.
- Citations: 29 (Semantic Scholar, 2026-11-14).

## Follow-up

- **Relevance:** 4. The main dose-response curve for instruction density across
  model tiers. It bears directly on how many requirements a brief can carry.
- **Guide:** P2 refines. Frontier readers can carry many terse requirements
  (near-ceiling to about 100–250 keyword instructions), so coverage rarely hits
  a capacity limit at realistic brief sizes. Small or fast models decay from
  about 50 instructions. Primacy bias suggests putting critical constraints
  first. This is a candidate `[weak]` line for brief-anatomy (order by
  importance).
- Compare with harada2025instructions: there, *all-satisfied* rates for harder
  format constraints fall much earlier (n = 5–10). Instruction difficulty and
  interaction matter more than raw count.
