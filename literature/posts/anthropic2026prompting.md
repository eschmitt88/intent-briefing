---
kind: post
title: "Prompting best practices (Claude's latest models)"
author: "Anthropic (docs page, no named author)"
institutions: ["Anthropic"]
year: 2026
published: "undated living doc (snapshot 2026-11-14; covers models through Claude Fable 5.2 / Opus 5.5)"
venue: "Claude Platform docs"
peer_reviewed: false
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
code_url: null
citations: null
source: "raw/web/platform.claude.com-claude-prompting-best-practices.md"
added: "2026-11-14"
relevance: 4
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/commanders-intent]]", "[[concepts/brief-anatomy]]", "[[concepts/scaffold-absorption]]", "[[concepts/cross-model-prompt-transfer]]"]
tags: [vendor-guidance, anthropic, prompt-engineering, migration, literal-following]
---

# Prompting best practices (Claude's latest models)

## TL;DR

Anthropic's main prompt-engineering reference, a ~10k-word living doc that
routes to per-model pages. All four candidate claims are present, but three
are narrower in the source than in the candidate summary:
- **Give the reason** is general, and verified.
- **Prefer general instructions over prescriptive steps** appears only in
  the *thinking/reasoning* section. It is about hand-written reasoning
  plans, not agentic procedure in general.
- **Soften CRITICAL/MUST** is a fix for *overtriggering* on Opus
  4.5/4.6 when prompts were tuned against undertriggering.
- **More literal reading** is model-specific: it is stated on the Opus 4.8
  and Sonnet 5 pages; the main page only says "precise instruction
  following".

The page also tells the reader to use sequential steps "when the order or
completeness of steps matters". Measured claims are rare and unquantified,
except one ("up to 30 percent").

## Claims

Verified against the full text. Wording is quoted.
- **Reasons behind instructions (general).** "Providing context or motivation
  behind your instructions, such as explaining to Claude why such behavior is
  important, can give Claude more information about your goals". The
  example: "NEVER use ellipses" becomes "Your response will be read aloud by
  a text-to-speech engine, so never use ellipses...". The section ends:
  "Claude can generalize from the explanation."
- **General over prescriptive (scoped to reasoning).** Under "Leverage
  thinking": "Prefer general instructions over prescriptive steps. A prompt
  such as 'think thoroughly' often produces better reasoning than a
  hand-written step-by-step plan. Claude's reasoning frequently exceeds what
  a human would prescribe." The same section adds that multishot worked
  examples still shape thinking.
- **Steps when order matters (general principles).** "Provide instructions as
  sequential steps using numbered lists or bullet points when the order or
  completeness of steps matters." Also: "Think of Claude as a brilliant but
  new employee who lacks context on your norms and workflows."
- **Soften aggressive language (Opus 4.5/4.6).** "more responsive to the
  system prompt than previous models. If your prompts were designed to reduce
  undertriggering on tools or skills, these models might now overtrigger. The
  fix is to soften any aggressive language. Where you might have said
  'CRITICAL: You MUST use this tool when...,' you can use more normal
  prompting such as 'Use this tool when...' instead." The migration list
  says the same ("Tune anti-laziness prompting... reduce that guidance").
  Instructions like "If in doubt, use [tool]" are said to "cause
  overtriggering".
- **Literal reading.**
  - Main page: "Claude's latest models are trained for precise instruction
    following". The example is "can you suggest some changes" yielding
    suggestions, not edits.
  - The per-model table lists "literal instruction following" for Opus 4.8
    and Sonnet 5.
  - The Opus 4.8 page (consulted, not snapshotted) says it "interprets
    prompts literally and explicitly, particularly at lower effort levels.
    It does not silently generalize an instruction from one item to
    another, and it does not infer requests you didn't make."
- **Guidance is not enforcement.** On payments: "The block guides Claude and
  doesn't enforce anything, so have a person approve each call to any tool
  that can move money." It recommends tool-surface design: give no tool that
  can move money.
- **Per-model scoping.** "Where a technique names a specific model, treat it
  as measured on that model and re-check it against your own evals before
  applying it to another." Self-check instructions help generally, but
  "Claude Opus 5 is the exception... remove these instructions rather than
  rewriting them."

Measured (stated as test results, no n or method):
- "Queries at the end can improve response quality by up to 30 percent in
  tests, especially with complex, multidocument inputs." This is a maximum,
  with no baseline described.
- "In Anthropic's testing, an instruction to answer directly without
  deliberating didn't stop the model from thinking at `medium` effort and
  above" (Fable 5.2).
- The Fable 5.2 page (consulted, not snapshotted) reports that "some
  instructions and interventions designed for earlier models raised cost,
  caused side effects, or no longer had an effect". Removing an in-prompt
  token budget "lowered cost, with equivalent performance" on coding tasks.

## Methods / basis

- Vendor documentation that aggregates model-launch findings. Internal
  testing is referenced a handful of times but never described (no tasks,
  n or metrics).

## Results

- One bounded number ("up to 30 percent"). Everything else is qualitative.

## Critique / open questions

- **Evaluation quality.** Weak. It is the vendor's internal testing, mostly
  unquantified. Its value is that it is *the* reference claude-system prompts
  are written against, and that it scopes advice per model.
- **Discrepancies vs the candidate summary.**
  1. "Prefer general instructions over prescriptive steps" is about
     reasoning plans under thinking, not a blanket rule for agentic
     procedure. The same page recommends sequential steps when order or
     completeness matters.
  2. "Soften CRITICAL/MUST" is a migration fix for overtriggering in
     specific models, not a general style rule.
  3. "Newer models read instructions more literally" is attributed to
     specific models (Opus 4.8, Sonnet 5), not stated as a general trend on
     this page.
- **On the 2x2.** It favors **verbose intent**: reasons, context, "new
  employee" framing, explicit scope ("Include as many relevant features...").
  It also keeps **terse procedure** wherever order or completeness matters.
  Literal reading pushes toward *coverage*: if you want an instruction
  applied broadly, say so. That is P2, not "say less".
- **Q2 / scaffold absorption.** It gives many model-version-specific
  reversals: drop anti-laziness prompting, drop self-check instructions on
  Opus 5, drop delegation nudges and in-prompt token budgets on Fable 5.2.
  This is consistent with scaffolding going stale as models change, but the
  direction differs by behavior (some models need *more* explicit scope).
- **Q3.** The payments block is the clearest vendor statement that prose
  doesn't enforce. Put the invariant in the tool surface and a human
  approval gate.
- **Tension.** The skill-authoring doc's Claude-A example suggests escalating
  to "MUST filter" when a rule is missed (`anthropic2026skill`). This page
  says aggressive language overtriggers on newer models. Both may hold
  (escalation for a missed hard rule vs softening for tool triggering), but
  the guide should say which.

## Trust signals

- **Credibility:** 2. First-party vendor guidance with a few unquantified
  "in Anthropic's testing" results. No n, no method, not peer reviewed, and
  a living doc whose model list and advice change over time.

## Follow-up

- **Relevance:** 4. This is the canonical Anthropic source behind P1's
  vendor citation and the reference claude-system prompts target. It is
  narrower than summarized on the key P1 line.
- **Guide:** P1 refines. "Give the reason" is verified. "General over
  prescriptive" is verified only for reasoning steps, and the same source
  keeps sequential steps when order or completeness matters. P1 should cite
  it for rationale, not as a blanket anti-procedure rule.
- **Guide:** P2 supports. Literal-following models "do not infer requests you
  didn't make", so unstated scope gets dropped.
- **Guide:** P3 supports. "The block guides Claude and doesn't enforce
  anything". Move money-moving and other invariants to the tool surface and
  approvals.
- Candidates: snapshot the per-model pages that hold the actual measured
  statements: `prompting-claude-fable-5-2` (stale-harness review, token
  budget removal) and `prompting-claude-opus-4-8` (literal following).
