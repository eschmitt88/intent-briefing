---
kind: paper
title: "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems"
authors: ["Paul Barbaste", "Tristan Darrigol", "Germain Vu", "Tom Wiltberger"]
institutions: ["Inclusive Brains", "Wavestone AI Lab"]
year: 2026
venue: "arXiv preprint (v1, 2026-07-15; second, expanded edition of an April 2026 study)"
peer_reviewed: false
url: "https://arxiv.org/abs/2609.00006"
code_url: null
citations: null
source: "raw/papers/barbaste2026harness.pdf"
added: "2026-11-14"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/invariants-in-code]]", "[[concepts/cross-model-prompt-transfer]]", "[[concepts/durable-structure]]", "[[concepts/context-engineering]]"]
tags: [harness-engineering, coding-agents, system-prompts, skills, permissions, source-code-study, longitudinal]
---

# Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents

## TL;DR

A descriptive source-code study of 11 coding-agent harnesses, re-pinned to
July 2026:

- Claude Code, Codex CLI, Gemini CLI and Mistral Vibe;
- OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode and OpenClaw;
- plus the Omnigent meta-harness as a contrast point.

It maps a shared seven-subsystem core and diffs eight of the systems across
one quarter. Over that quarter, behavioural policy moved out of system-prompt
prose and into configuration, flags and policy files. The study has no
outcome measurements at all.

## Claims

- **Shared core:** every harness takes a position on seven subsystems: agent
  loop, LLM integration (prompt assembly / caching), tools & actions, memory &
  context, safety & permissions, orchestration, and extensibility (Table 1).
  Mini-SWE-Agent covers all seven in ~100 lines.
- **Two absences across ~4M lines:** no runtime imports a general agent
  framework (LangChain, LangGraph, AutoGen and others), and none uses vector
  embeddings for code retrieval. Retrieval is deterministic (ripgrep,
  tree-sitter, glob, auto-discovered Markdown context files).
- **Skills lead MCP in adoption:** 9/11 vs 8/11. The first agent-authored
  skills appear (Hermes' self-improving loop, Gemini CLI's extraction inbox).
- **Obs. 3: prompt rhetoric converges, then thins as trust calibrates.**
  - Anti-gold-plating directives appear in near-isomorphic wording across six
    independent scaffolds.
  - The April 2026 "no autonomous commit" rule was universal in the prompts
    that mention git.
  - By July, Mistral Vibe had reversed it, and Codex's GPT-5.6 prompts dropped
    both the commit rule and the anti-gold-plating directives.
- **§14.5, "Policy migrated out of prose":** "behavioral policy is moving
  from the prompt (where the model reads it) to configuration (where the
  platform enforces it)". Examples:
  - Codex feature flags (`codex_git_commit`, itself retired by July);
  - Mistral Vibe's seven-level precedence contract, A/B-tested server-side;
  - policy-as-data rules (Starlark execpolicy, PreToolUse hooks, TOML
    per-mode rules).
- **Model-conditional prompting is its own axis.**
  - OpenCode ships 9 base prompts keyed by model-id substring.
  - Hermes sends tool-use enforcement blocks to GPT/Codex/Gemini/Grok/Qwen/
    DeepSeek but never to Claude, with code comments citing observed
    per-model failures.
  - Codex ships per-generation prompts as server-delivered data.
- **Prompt text can overclaim.** OpenCode's edit-tool description says it
  "will error if you attempt an edit without reading the file", but no
  read-tracking exists in the source: "prompt text is a behavioral wish, not
  a mechanism" (§7.3).

## Methods

- Static reading of source trees: dependency manifests, import grep across
  Python/TS/Rust, and the canonical system prompts.
- Eight systems were re-pinned from an April 2026 snapshot, which gives a
  90-day longitudinal diff.
- Claude Code was analysed from a "publicly circulated source snapshot from
  March 2026", not an official release. The authors flag this as the weakest
  link (§15).

## Results

- 13 observations, a catalogue of 29 patterns, 18 design recommendations and a
  90-line minimal harness.
- Instruction-relevant recommendations:
  - **Rec. 11:** "codify safety rules as data or dedicated policy files
    rather than as imperative code", and keep a floor beneath any YOLO mode.
  - **Rec. 6:** auto-discover hierarchical Markdown context files and surface
    nested ones just-in-time.
  - **Rec. 5:** match the edit-tool contract to the model tier (exact match
    for frontier models, fuzzy cascades for weaker ones).
- Verbosity directives appear in 9/11 prompts. No prompt contains policy-level
  harmful-request refusal language (11/11). Emphasis follows three schools:
  uppercase tags, structural rule blocks / precedence contracts, and
  exemplar pairs.

## Critique / open questions

- **No outcome measurements.** This is an inventory of what vendors ship, not
  evidence that any choice works. The paper says so: it "does not benchmark
  or rank". "Policy thinning as models internalize the norms" is the authors'
  reading of the motive. No behavioural test shows that the dropped rules are
  no longer needed.
- **Thin longitudinal sample.** It is one quarter, mostly one vendor's
  prompts (Codex) plus Mistral Vibe. The authors themselves note that
  inventory claims "decay in weeks".
- The Anthropic-guidance-to-architecture mapping (Obs. 10) is correlational,
  and the authors note it.
- **2×2:** off-grid as evidence. As description, production prompts sit
  mostly in *terse procedure + hard rules*, trending toward *terse intent +
  enforced configuration* for the newest models.
- **Shared doctrine is present by construction.** These harnesses are the
  doctrine-delivery layer (AGENTS.md / CLAUDE.md / skills).

## Trust signals

- **Credibility:** 2. Industry lab (Wavestone AI Lab) plus a startup. Not
  peer reviewed, and no companion code or artifacts released. Claims for 10/11
  systems can be re-derived from public Git history. Claude Code rests on an
  unofficial snapshot. Purely descriptive, but careful about separating dated
  inventory claims from structural ones. Citations not retrieved (Semantic
  Scholar rate-limited).

## Follow-up

- **Relevance:** 3. Cite-worthy prior art for P3 and Q3. It shows practice
  converging on enforcement outside the prompt, and model-conditional prompt
  matrices. It does not show effect sizes.
- **Guide:** P3 supports (practice, not outcome) — production harnesses move
  hard rules (commit policy, permissions, safety floors) from prompt prose
  into flags, policy files and hooks. The OpenCode overclaim shows prose
  "enforcement" can be fictional.
- **Guide:** P1 supports (weakly, practice only) — the newest Codex prompts
  drop procedural don'ts (anti-gold-plating, no-commit) as models improve.
  This is vendor behaviour, not a measured effect.
