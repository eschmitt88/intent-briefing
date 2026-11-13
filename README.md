# intent-briefing

**Brief, don't script: when should agentic systems give strong models intent instead of procedure, and where does that stop working?**

📂 **[Browse this repo →](https://eschmitt88.github.io/intent-briefing/)** —
interactive, always-live view of experiments, concepts, literature, and maps of
content. Served via GitHub Pages from `docs/index.html`; reads the live file
tree, no build step. _(Link is live once the repo is public and Pages is enabled
— `/new-project` does both by default.)_

## What this is

People and models designing agentic systems tend to write step-by-step
scripts for readers that are as capable as the author, or more. This project
tests the alternative, an **intent-level brief** (goal, hard constraints,
rationale, transferred context), against scripts across model strengths,
instruction classes and task horizons. The aim is to find the boundary, not
to confirm the hunch. Success means a measured, evidence-graded writing guide
for system prompts, subagent briefs and skills, and accepted changes to the
[claude-system](https://github.com/eschmitt88/claude-system) harness it
builds on. Plan: [`docs/research-plan.md`](docs/research-plan.md).

## How it's organized

Plain Markdown + flat YAML frontmatter, cross-linked with `[[wikilinks]]`:

- `concepts/` / `mocs/` — atomic ideas; promoted to a map of content when ≥5 cluster.
- `literature/` — processed notes on papers, repos, posts (0–5 relevance scored).
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs (hypothesis → result, config, metrics, log).
- `raw/` — immutable source captures · `docs/decisions/` — ADRs · `_meta/` — index, log, templates.

## Local use

```sh
make env    # uv sync
make lint   # knowledge-graph / experiment health check
```

Built on the [claude-system](https://github.com/eschmitt88/claude-system)
research framework (upstream attribution — this project is its own repo).
See `CLAUDE.md` for the agent-facing orientation and `~/.claude/CLAUDE.md`
for the framework's durable principles.
