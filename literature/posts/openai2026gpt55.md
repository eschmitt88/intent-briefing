---
kind: post
title: "Using GPT-5.5 (model guide incl. prompting best practices)"
author: "OpenAI (docs page, no named author)"
institutions: ["OpenAI"]
year: 2026
published: "undated living doc; GPT-5.5 released 2026-04-24 per the OpenAI API changelog"
venue: "OpenAI API docs"
peer_reviewed: false
url: https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5.md
code_url: https://github.com/openai/skills/tree/main/skills/.curated/openai-docs
citations: null
source: "raw/web/developers.openai.com-latest-model-gpt-5.5.md"
added: "2026-11-14"
relevance: 5
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/brief-anatomy]]", "[[concepts/scaffold-absorption]]", "[[concepts/cross-model-prompt-transfer]]", "[[concepts/invariants-in-code]]"]
tags: [vendor-guidance, openai, outcome-first, migration, stopping-rules]
---

# Using GPT-5.5 (OpenAI prompting guide)

## TL;DR

OpenAI's GPT-5.5 model guide tells developers to write **outcome-first**
prompts. Describe "the expected outcome, success criteria, allowed side
effects, evidence rules, and output shape", and "avoid step-by-step process
guidance unless the exact path matters". Keep success criteria and stop rules
explicit. On migration, start "with the smallest prompt that preserves the
product contract" rather than carrying the old prompt stack forward. Every
claim is asserted. The page contains no measurement.

**Retrieval note.** The candidate URL `/api/docs/guides/prompt-guidance.md`
now redirects to `/latest-model.md`, which covers **GPT-6** (GPT-6 Astra /
GPT-6.1 Sol). The GPT-5.5 guide was fetched from
`/api/docs/guides/latest-model/gpt-5.5.md`. The page is titled "Using
GPT-5.5" and has a "Prompting best practices" section. There is no
standalone "GPT-5.5 prompting guide" page.

## Claims

All asserted (vendor observation, no numbers).
- **Outcome-first.** "Stronger task execution with outcome-first prompts:
  GPT-5.5 is better at working from a clear goal, preserving constraints,
  and turning product intent into concrete next steps... Avoid step-by-step
  process guidance unless the exact path matters."
- **Process-heavy legacy stacks hurt.** "Legacy prompts often over-specify
  the process because earlier models needed more help staying on track. With
  GPT-5.5, that can add noise, narrow the model's search space, or lead to
  overly mechanical answers." Migration checklist: "Reduce or remove detailed
  step-by-step process guidance. Let GPT-5.5 choose the path unless the
  product requires that path."
- **Smallest prompt on migration.** "treat it as a new model family to tune
  for, not a drop-in replacement... Begin migration with a fresh baseline
  instead of carrying over every instruction from an older prompt stack.
  Start with the smallest prompt that preserves the product contract, then
  tune reasoning effort, verbosity, tool descriptions, and output format
  against representative examples."
- **Success criteria and stop rules stay explicit.** "Define success
  criteria and stopping rules, especially for long-running, tool-heavy, or
  evidence-gathering workflows." The suggested prompt skeleton is Role /
  Personality / Goal / Success criteria / Constraints / Output / Stop rules:
  "Keep each section short. Add detail only where it changes behavior."
- **Absolutes reserved for invariants.** "Use those words [ALWAYS, NEVER,
  must, only] for true invariants, such as safety rules, required output
  fields, or actions that should never happen. For judgment calls... prefer
  decision rules instead."
- **Literal reading.** "GPT-5.5 interprets prompts in a literal and thorough
  manner, enabling specific, descriptive instructions when the product
  requires them."
- **Coding agents need *more* explicitness.** "For coding agents, be explicit
  about reuse, subagent delegation, test expectations, acceptance criteria,
  and when to continue versus ask for help."
- **Effort and weak stopping criteria interact.** "If the task has
  conflicting instructions, weak stopping criteria, or open-ended tool access,
  higher effort can lead to overthinking, unnecessary searching, or output
  quality regressions."
- Retrieval budgets are framed as "stopping rules for search". Put
  tool-specific guidance in tool descriptions (what, when, inputs, side
  effects, retry safety, error modes). Move output schemas to Structured
  Outputs instead of prose.

## Methods / basis

- Vendor model-launch documentation. Statements like "GPT-5.5 is better
  at..." imply internal evals, but none are cited or quantified. The example
  prompts are illustrative. A Codex skill (`openai-docs`) automates the
  migration.

## Results

- None reported.

## Critique / open questions

- **Evaluation quality.** There is no outcome evidence, no comparison of
  outcome-first vs process prompts, and no numbers. This is a second
  vendor's doctrine. Its value is cross-lineage *agreement* with Anthropic
  guidance, not evidence of effect size (Q1 stays open).
- **On the 2x2.** It recommends **terse intent plus explicit success
  criteria and stop rules**. Rationale and context are optional ("Keep each
  section short"). Procedure is kept only "unless the exact path matters".
  That makes it closer to "terse intent + contract" than to verbose intent.
  The coding-agent caveat pushes back toward explicit acceptance criteria and
  delegation rules, which is coverage, not scripting.
- **Q2 / scaffold absorption.** It states outright that process scaffolding
  existed "because earlier models needed more help". That is a vendor
  version of the absorption hypothesis, and it is unmeasured.
- **Cross-model transfer.** "Not a drop-in replacement" and "fresh baseline"
  amount to an admission that prompts don't transfer cleanly across model
  versions even within one lineage.
- **Q3.** Absolutes are reserved for invariants, and output schemas go to
  Structured Outputs. Both line up with the invariant boundary (an API
  constraint over prose).
- **Successor page.** The GPT-6 guide (now at the old URL) says GPT-6 Astra
  "can be more sensitive to instructions contained in skills and other files,
  such as `AGENTS.md`" and "strongly recommend[s] auditing skills". That is
  relevant to P6/Q5, but it was not snapshotted here.

## Trust signals

- **Credibility:** 2. First-party vendor guidance for its own model,
  undated, with no measurement and no peer review. Credible as a statement
  of what the vendor believes; weak as evidence.

## Follow-up

- **Relevance:** 5. This is the clearest non-Anthropic vendor statement of
  outcome-first over process, and the OpenAI half of P1's "Anthropic and
  OpenAI guidance" citation.
- **Guide:** P1 supports, with a refinement. It verifies the wording
  "outcome-first... avoid step-by-step process guidance unless the exact
  path matters". It also makes success criteria and stop rules mandatory
  parts of the brief, and coding agents get explicit acceptance criteria.
- **Guide:** P2 supports (weakly). Success criteria, allowed side effects,
  evidence rules and output shape should be stated, not left implicit.
- **Guide:** P3 supports. ALWAYS/NEVER are reserved for true invariants, and
  schemas move to Structured Outputs.
- Candidate: snapshot the GPT-6 guide (`/api/docs/guides/latest-model.md`)
  for its claims about skill/AGENTS.md sensitivity and its prompt for
  surfacing which skill instruction caused a pause (P6, Q5).
