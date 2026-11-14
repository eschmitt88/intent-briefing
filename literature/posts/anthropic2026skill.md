---
kind: post
title: "Skill authoring best practices (with companion post: Equipping agents for the real world with Agent Skills)"
author: "Anthropic (docs page, no named author); companion post by Barry Zhang, Keith Lazuka, Mahesh Murag"
institutions: ["Anthropic"]
year: 2026
published: "docs page undated (living doc, snapshot 2026-11-14); companion post 2025-10-16"
venue: "Claude Platform docs; Anthropic Engineering blog"
peer_reviewed: false
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
code_url: https://github.com/anthropics/skills
citations: null
source: "raw/web/platform.claude.com-agent-skills-best-practices.md"
source_companion: "raw/web/anthropic.com-equipping-agents-for-the-real-world-with-agent-skills.md"
added: "2026-11-14"
relevance: 5
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/degrees-of-freedom]]", "[[concepts/context-engineering]]", "[[concepts/brief-anatomy]]", "[[concepts/llm-authored-instructions]]"]
tags: [skills, progressive-disclosure, vendor-guidance, degrees-of-freedom, skill-md]
---

# Skill authoring best practices (+ "Equipping agents for the real world with Agent Skills")

Citekey year is the snapshot year. The docs page is a living document with no
publication date.

## TL;DR

Anthropic's normative guide to writing `SKILL.md` files, plus the launch post
that explains the architecture. The core rules: be concise, because
"**Default assumption:** Claude is already very smart"; "Match the level of
specificity to the task's fragility and variability" (high, medium or low
freedom); use progressive disclosure (metadata → body → bundled files, kept
one level deep); keep the body under 500 lines; write evals before
documentation. There are no measurements anywhere. This is vendor doctrine,
not evidence.

## Claims

All asserted. Neither source reports any measurement.
- **Concision.** "The context window is a public good." "Only add context
  Claude doesn't already have." Ask of each paragraph: "Does this paragraph
  justify its token cost?" The worked example is a ~50-token good version vs
  a ~150-token bad one (token counts of the examples, not an eval).
- **Degrees of freedom.** "Match the level of specificity to the task's
  fragility and variability."
  - High freedom (text heuristics) when "multiple approaches are valid" and
    decisions depend on context.
  - Medium (pseudocode, parameterized scripts) when "a preferred pattern
    exists".
  - Low ("Run exactly this script... Do not modify the command") when
    "operations are fragile and error-prone", "consistency is critical", or
    "a specific sequence must be followed".
  - The analogy: a "narrow bridge with cliffs on both sides" vs an "open
    field with no hazards".
- **Model dependence.** "What works perfectly for Opus might need more detail
  for Haiku". Test with every target model, and ask of Opus: "Does the Skill
  avoid over-explaining?"
- **Progressive disclosure** (post: "the core design principle").
  - Level 1: `name` + `description`, pre-loaded at startup.
  - Level 2: the `SKILL.md` body, read when the skill is relevant.
  - Level 3+: bundled files, read on demand.
  - Because of this, bundled context is "effectively unbounded" (post).
- **Size and structure.**
  - "Keep the `SKILL.md` body under 500 lines for optimal performance."
  - `name` ≤64 chars; `description` ≤1,024 chars, third person, says what
    the skill does *and* when to use it.
  - References one level deep, because Claude may `head -100` nested files.
  - Reference files over 100 lines get a table of contents.
- **Procedure where it earns its place.** "Break complex operations into
  clear, sequential steps", with copyable checklists. Feedback loops
  (validate → fix → repeat) "greatly improves output quality".
- **Code for determinism** (post): "many applications require the
  deterministic reliability that only code can provide". Scripts should
  "solve, don't defer" error handling, and constants should be justified.
- **Eval-first.** "Create evaluations BEFORE writing extensive
  documentation". Measure a no-skill baseline, then "write minimal
  instructions" that pass three scenarios. "There is not currently a built-in
  way to run these evaluations."
- **LLM-authored skills.** Claude A writes or refines, Claude B tests on
  real tasks, and the human observes. "Claude models can both write
  effective agent instructions and identify what information agents need."
  Review Claude A's output for unnecessary explanation. The post says the
  loop helps "discover what context Claude actually needs, instead of trying
  to anticipate it upfront."
- **Tension inside the doc.** In the iteration example, Claude A may suggest
  "stronger language such as 'MUST filter' instead of 'always filter'" when
  a rule is missed. The general prompting guide says to soften
  CRITICAL/MUST for newer models (see `anthropic2026prompting`).

## Methods / basis

- Vendor documentation and a launch blog. The basis is internal experience
  building skills (the PDF and docx skills are the worked example). No
  eval, no ablation, no numbers. The skills repo is public
  (`anthropics/skills`), so the doctrine's own artifacts can be inspected.

## Results

- None. The 500-line threshold and "one level deep" are unmeasured
  heuristics. The doc gives no evidence for where 500 comes from.

## Critique / open questions

- **Evaluation quality.** There is no task-outcome evidence. The guidance is
  plausible and internally coherent, but it can't by itself lift a
  writing-guide line above `[weak]`/vendor-guidance.
- **On the 2x2.** This is the clearest vendor statement that the cell is
  chosen *per task*, not globally.
  - Open field: terse intent.
  - Narrow bridge: terse or verbose **procedure**, down to "run exactly this
    script".
  - Complex multi-step workflows get explicit checklists.
  - "Concise" works against verbose *explanation* (don't explain what a PDF
    is), not against coverage of non-obvious rules (the doc's own example
    keeps "always exclude test accounts").
- **Q2 (capability boundary).** The doc expects weaker models to need more
  detail ("might need more detail for Haiku") and the strongest to be harmed
  by over-explaining. That matches the brief hypothesis on direction but is
  unmeasured. It also sits uneasily with 2606.08529 (strongest model gained
  most from scaffolding). Skills' scaffolding is mostly *knowledge and
  enforcement* structure, which the guide's P4 already distinguishes.
- **Q3.** The low-freedom tier and "code for deterministic reliability" are
  vendor endorsement of moving invariants out of prose.
- **Q5.** The doc recommends LLM-authored skills, but inside an observe/test
  loop with human review for verbosity. That is consistent with
  `aizawa2025writing`: LLM authoring with validation.

## Trust signals

- **Credibility:** 2. First-party vendor guidance from the team that built
  the feature, with a public skills repo, but no measurement, no peer
  review, and an undated living document that may change under the
  citation.

## Follow-up

- **Relevance:** 5. This is the canonical source for how claude-system
  skills are supposed to be written, and the origin of the
  degrees-of-freedom framing. It is load-bearing for P1 and P4 even though
  it is weak as evidence.
- **Guide:** P1 refines. "Brief, don't script" holds for open-field tasks;
  for fragile, consistency-critical or sequence-bound operations the vendor
  prescribes low freedom (exact scripts). P1 should name the
  fragility/variability test explicitly.
- **Guide:** P4 supports. Checklists, feedback loops, progressive-disclosure
  structure and bundled scripts are kept because they carry knowledge or
  enforce rules.
- **Guide:** P3 supports. Deterministic operations go into scripts ("only
  code can provide").
- **Guide:** P6 refines. Vendor-recommended LLM authoring (Claude A/B) is
  paired with real-task testing and human review for over-explanation.
- Proposed concept (not created): `progressive-disclosure`, if a second
  source beyond Anthropic's uses it. Currently covered by
  `context-engineering`.
