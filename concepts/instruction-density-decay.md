---
kind: concept
name: "instruction-density-decay"
status: growing
added: "2026-11-14"
sources:
  - "[[literature/papers/harada2025instructions]]"
  - "[[literature/papers/jaroslawicz2025instructions]]"
  - "[[literature/papers/yang2025what]]"
  - "[[literature/papers/liu2026espo]]"
  - "[[literature/papers/zhu2026sage]]"
  - "[[literature/papers/shi2025loss]]"
  - "[[literature/papers/li2025thinking]]"
  - "[[literature/papers/wang2026longhorizon]]"
related_concepts:
  - "[[concepts/requirement-coverage]]"
  - "[[concepts/invariants-in-code]]"
  - "[[concepts/llm-authored-instructions]]"
related_experiments: []
tags: [instruction-following, density, compliance, instruction-design]
---

# instruction-density-decay

## Definition

The probability that a reader satisfies **every** instruction falls as the
number of simultaneous instructions grows. Per-instruction compliance can stay
high while joint compliance collapses, because the small misses compound.

## Why it matters here

This is the measurable cost of the "full script" cell of the 2x2, and of
checklists in general.

**ManyIFEval** ([[literature/papers/harada2025instructions]]) measures the share
of prompts with every instruction satisfied, going from 1 to 10 instructions:

| Model | 1 instruction | 10 instructions |
|---|---|---|
| o3-mini-high | 1.00 | 0.78 |
| Claude 3.5 Sonnet | 0.95 | 0.48 |
| GPT-4o | 0.94 | 0.21 |

- Per-instruction accuracy barely moves: Claude 3.5 Sonnet goes from 0.95 to
  0.93. The collapse comes from compounding.
- On code with 1 to 6 style rules, Claude 3.5 Sonnet falls from 0.96 to 0.01
  even though the code still passes its tests.
- A GPT-4o judge scored 0.657 where rule-based checks gave 0.213. Judges hide
  this effect.

**IFScale** ([[literature/papers/jaroslawicz2025instructions]]) shows three
curve shapes by tier:

- **Threshold.** Frontier reasoning models stay at ~98% through 100–250
  instructions. Gemini-2.5-pro reaches 68.9% at 500.
- **Linear.** gpt-4.1 and claude-3.7.
- **Exponential.** Small and fast models collapse after ~50 instructions.

Errors on later instructions peak at 150–200 instructions (primacy bias). The
instructions tested are keyword inclusion, the easiest type, so the curves
measure capacity more than fragility.

The ceiling moves with capability. For frontier readers, density matters
mainly for (a) hard rules that must all hold at once and (b) machine-grown
prompts:

- **Optimizer-grown prompts.** Prompts that accumulate rules grew without
  gaining accuracy ([[literature/papers/zhu2026sage]],
  [[literature/papers/liu2026espo]]). The most rule-heavy optimized prompt
  transferred worst ([[literature/papers/shi2025loss]]).
- **Long runs.** Over long horizons, constraints still in context get dropped
  ([[literature/papers/wang2026longhorizon]], anecdotal).

## Connections

- [[concepts/invariants-in-code]]: rules that must hold jointly and can be
  checked by code should be checked by code.
- [[concepts/requirement-coverage]]: state only the requirements that aren't
  met by default.
- [[concepts/brief-anatomy]]: put critical constraints first.
