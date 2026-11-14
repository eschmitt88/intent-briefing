---
kind: post
title: "How we built Claude Code auto mode: a safer way to skip permissions"
author: "John Hughes (Anthropic)"
institutions: ["Anthropic"]
year: 2026
published: "2026-03-25"
venue: "Anthropic Engineering blog"
peer_reviewed: false
url: https://www.anthropic.com/engineering/claude-code-auto-mode
code_url: null
citations: null
source: "raw/web/anthropic.com-claude-code-auto-mode.md"
added: "2026-11-14"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/invariants-in-code]]", "[[concepts/durable-structure]]", "[[concepts/handoff-context-loss]]"]
tags: [permissions, classifier, safety, overeagerness, claude-code, vendor-account]
---

# How we built Claude Code auto mode

## TL;DR

Auto mode replaces per-action human approval in Claude Code with three
tiers:
1. A deterministic allowlist (read-only tools plus user rules, minus
   rules that grant arbitrary code execution).
2. Free in-project file edits.
3. A two-stage Sonnet 4.6 transcript classifier for everything else.

A prompt-injection probe screens tool outputs. Every candidate number checks
out:
- Users approve 93% of manual prompts.
- The full pipeline misses **17%** of real overeager actions (n = 52) and
  **5.7%** of synthetic exfiltration attempts (n = 1,000).
- It blocks 0.4% of real benign traffic (n = 10,000).

The author calls the 17% "the honest number", and says prompt engineering
could not fix the main failure: telling consent for *this* action apart from
approval-shaped evidence.

## Claims

Measured (internal datasets, n reported; no CIs, data not released). Values
are from the results figure, transcribed into the raw file:

| Dataset | Stage 1 alone | Full pipeline (stage 1 → 2) |
|---|---|---|
| Real internal traffic, n = 10,000 (FPR) | 8.5% | 0.4% |
| Real overeager actions, n = 52 (FNR) | 6.6% | **17%** |
| Synthetic data exfiltration, n = 1,000 (FNR) | 1.8% | **5.7%** |

- "in practice users accept 93% of them anyway" (manual permission
  prompts). No n or period given.
- Context ablation, no numbers: "Including assistant messages and tool
  results caused a drop in performance on our overeagerness testset." A
  tool-calls-only variant "had the lowest false-negative rate still but lost
  the user-intent anchor", over-blocking requested actions.
- Escalation backstop: 3 consecutive or 20 total denials stop the session,
  and in headless mode the process terminates.

Asserted:
- **The main miss mode is consent scope.** "In the majority of misses we
  examined, the classifier correctly identifies the danger... What it gets
  wrong is whether a real consent signal in the session actually covers
  *this* action... We've tried prompt-engineering around this and haven't
  found a fix that doesn't cost more than it gains."
- **The deterministic layers are retained and tightened.** Tier 1 is "a fixed
  allowlist" of non-state-modifying tools. Entering auto mode *drops*
  user rules that grant arbitrary code execution (blanket shell, wildcarded
  interpreters, package-manager run). Otherwise "the classifier never sees
  the commands most capable of causing damage". Tier 2 lets
  in-project edits skip the classifier because they are "reviewable via
  version control".
- **The classifier prompt mixes a fixed procedure with policy slots.** A
  fixed template (evaluation rules, user-intent rules, and "a step-by-step
  classification process": block rules → exceptions → user intent →
  decision) plus three customizable slots (environment trust boundary, 20+
  block rules, allow exceptions). The intent rule is conservative:
  "everything the agent chooses on its own is unauthorized until the user
  says otherwise."
- **Delegation strips authorization context.** "Inside the subagent, the
  orchestrator's instruction *is* the user message, so tasks look fully
  authorized." So the check runs at delegation and again at return.
- Auto mode is "not a drop-in replacement for careful human review on
  high-stakes infrastructure".

## Methods / basis

- Three evaluation sets, described with n and provenance:
  - Employee Claude Code traffic.
  - Curated overeager actions: denied by the employee or flagged post hoc.
    The set is small "because it requires Claude attempting something
    dangerous in a real session".
  - Generated exfiltration attempts, many obfuscated.
- The metrics are binary classification (FPR/FNR) on actions, which is a
  task outcome, not an LLM-judged rubric score of quality.

## Results

- The deployed pipeline trades recall for friction: stage 2 cuts FPR 8.5% →
  0.4% while FNR rises 6.6% → 17% (overeager) and 1.8% → 5.7% (exfil).

## Critique / open questions

- **Evaluation quality.** Good for a vendor post: n stated per set, real plus
  synthetic, unflattering numbers reported. Limits:
  - n = 52 for the headline risk number gives a wide interval (9 misses ≈
    17%, Wilson 95% roughly 9–30%).
  - The data come from Anthropic employees (a single population).
  - The labels come from employee denials or post-hoc flags.
  - There are no CIs and the data are not released.
  - The context-ablation claims have no numbers.
- **Not a briefing study.** It doesn't compare intent vs script framing.
  Its relevance is the **invariant boundary (Q3)**: a frontier model with a
  carefully engineered prompt still misjudges authorization scope 17% of the
  time on real cases. Anthropic responded by keeping deterministic tiers and
  hard denial limits, not by adding more prose.
- **On the 2x2.** The classifier prompt is deliberately **procedural**
  (fixed step-by-step classification order) with **verbose policy context**
  in slots. For a judge or gatekeeper role the vendor chose a script plus
  policy, which is a useful counterexample to "brief, don't script"
  everywhere.
- **Context finding.** Removing the agent's own prose and tool outputs
  *improved* the classifier. That suggests "hand over context" (P5) has an
  exception when the context is the agent's own rationalization.
- **Handoff context loss.** The subagent-authorization point is a concrete
  mechanism: delegation erases the provenance of intent. That is relevant to
  P5 and the brief-anatomy asymmetry.

## Trust signals

- **Credibility:** 3. First-party measured numbers with stated n on three
  datasets (including real traffic), candid negative results, a named
  author, and a shipped product. It is not peer reviewed, the data are not
  released, n = 52 is small, and the population is internal only.

## Follow-up

- **Relevance:** 4. Strong, measured evidence on Q3: prompt-level judgment
  of authorization scope leaves a residual miss rate that prompt engineering
  didn't close, so deterministic structure stays. Indirect for the
  brief-vs-script question.
- **Guide:** P3 supports. The vendor keeps a deterministic allowlist, drops
  arbitrary-execution rules, and adds hard denial limits. The 17% FNR
  (n = 52) and 5.7% FNR (n = 1,000) are measured residual risk of
  model-judged rules, and prompt engineering "haven't found a fix".
- **Guide:** P5 refines. Handing over context isn't always better. The
  classifier did better *without* the agent's messages and tool outputs, and
  subagent handoffs strip intent provenance, so intent must be re-checked at
  delegation.
- **Guide:** P1 refines (minor). For gatekeeper/judge roles the vendor used
  a fixed step-by-step procedure plus policy slots, not an intent brief.
