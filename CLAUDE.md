# Project: intent-briefing

Short orientation only. User-level `~/.claude/CLAUDE.md` holds the durable
principles; this file refines them for this project.

## What this project is about

How to instruct strong models in agentic systems: when does an **intent-level
brief** (goal, constraints, rationale, context) beat a **step-by-step script**,
and where does that stop being true? The research exists to change
`~/claude-system` (skills, hooks, rules, subagent briefs, max-agency runs) and
to be the live reference those pieces are refined against.
**Literature and reference only, no in-house experiments** (ADR 0003).
Plan: `docs/research-plan.md`. Deliverable: `docs/writing-guide.md`.

## Layout (see user CLAUDE.md for the full rationale)

- `raw/` — immutable source material. Read only.
- `literature/` — processed notes on papers, repos, posts.
- `concepts/` — atomic ideas. Promote to `mocs/` when ≥5 cluster.
- `docs/decisions/` — lightweight ADRs.
- `journal/` — daily session files (hook-written).
- `_meta/` — index, log, templates.

## Scoped rules

Detailed conventions live in `.claude/rules/` and are auto-loaded when you
touch matching paths:

@.claude/rules/data.md

Framework rules in `~/claude-system/claude/rules/` can't be `@`-imported
(imports resolve only in-tree): read `evaluation.md` before designing or
judging an evaluation, `agency.md` before an autonomous run. Skills with
`respects:` do this automatically. Read `evaluation.md` before judging a
source's evaluation; weight task-outcome results over LLM-judge rubrics.

## Inherited architecture
Read these by path before relying on them (they don't auto-load):
- ~/projects/research/agentic-research/concepts/intent-level-briefing.md
- ~/projects/research/agentic-research/concepts/constraint-pinning.md
- ~/projects/research/agentic-research/concepts/typed-enforcement.md

## Budget & compute

Autonomous runs read `budget.yaml` at this project's root for hard
ceilings (wall time, tokens, disk) and model roles (ideator vs
implementer). Before proposing anything with non-trivial resource
demands — multi-hour training, large downloads, many seeds — read
`budget.yaml` and make sure the ask fits under the remaining headroom.
If it doesn't fit, say so in the proposal's `risks:` and either scope
down or explicitly flag the need to raise a ceiling.

@budget.yaml

## Project-specific facts

- Content: Markdown notes; no code beyond the template's lint.
- **Public repo.** Never quote this box's transcripts, logs or private-project
  content. Box-internal QA lives in a separate private audit repo.
- Results flow to claude-system only via agentic-research `/elevate` →
  `docs/system-proposals/`. Predecessor: `2026-07-31-instruction-ablation-program`.
- Environment: managed by `uv`; run `make env` to sync.
- Data: tracked by DVC. Large artifacts on SN850X via `~/projects/`.

## Keeping the guide live

When an ingest bears on a principle in `docs/writing-guide.md`, update its
evidence entry and its one-line rule in the same commit. Contradicting
evidence rewrites the principle; don't keep both versions. P-numbers are
stable IDs: add new ones at the end, never renumber. Run
`python3 scripts/check_guide.py` before committing (CI runs it too).

## Housekeeping

- End sessions with `/wrap`. The SessionEnd hook backstops this.
- Run `/lint` weekly.
