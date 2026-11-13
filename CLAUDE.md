# Project: intent-briefing

Short orientation only. User-level `~/.claude/CLAUDE.md` holds the durable
principles; this file refines them for this project.

## What this project is about

How to instruct strong models in agentic systems: when does an **intent-level
brief** (goal, constraints, rationale, context) beat a **step-by-step script**,
and where does that stop being true? The research exists to change
`~/claude-system` (skills, hooks, rules, subagent briefs, max-agency runs) and
to be the live reference those pieces are refined against.
Plan + questions: `docs/research-plan.md`. Scope: `docs/decisions/0001-*`.

## Layout (see user CLAUDE.md for the full rationale)

- `raw/` — immutable source material. Read only.
- `literature/` — processed notes on papers, repos, posts.
- `concepts/` — atomic ideas. Promote to `mocs/` when ≥5 cluster.
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs.
- `docs/decisions/` — lightweight ADRs.
- `journal/` — daily session files (hook-written).
- `_meta/` — index, log, templates.

## Scoped rules

Detailed conventions live in `.claude/rules/` and are auto-loaded when you
touch matching paths:

@.claude/rules/experiments.md
@.claude/rules/notebooks.md
@.claude/rules/data.md

Framework rules in `~/claude-system/claude/rules/` can't be `@`-imported
(imports resolve only in-tree): read `evaluation.md` before designing or
judging an evaluation, `agency.md` before an autonomous run. Skills with
`respects:` do this automatically. Evaluation mode: **HCE** — a prompting
harness overfits to its own judge; outcome metrics, held-out tasks.

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

- Primary language: Python (harness); briefs and prompts as Markdown.
- LLM access: `claude -p` on the subscription, never a raw API key; pin
  `--model` in unattended jobs; run from a neutral cwd outside any project.
- Public repo: anything quoted from this box's prompts, logs or skills goes
  through redaction first (no hostnames, IPs, private-project names).
- Results flow to claude-system only via agentic-research `/elevate` →
  `docs/system-proposals/`. Predecessor: `2026-07-31-instruction-ablation-program`.
- Environment: managed by `uv`; run `make env` to sync.
- Data: tracked by DVC. Large artifacts on SN850X via `~/projects/`.

## Housekeeping

- End sessions with `/wrap`. The SessionEnd hook backstops this.
- Use `/new-experiment <slug>` — don't hand-roll experiment folders.
- Run `/lint` weekly.
