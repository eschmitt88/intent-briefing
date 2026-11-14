# NOTES

Running log of work sessions. `/wrap` appends a new dated section at the
end of each session with **Did / Findings / Next** subsections. The
SessionEnd hook backstops this if you forget.

<!-- entries go below this line, newest at bottom -->

## 2026-11-13

### Did
- Founded the project: scaffold, `docs/research-plan.md`, ADR 0001, agency max.
  Founding decisions made with Fable.
- Seeded hub concept `agentic-research/concepts/intent-level-briefing.md`;
  used_by synced.
- Ran four parallel `/discover` sweeps (specificity, delegation, scaffolding,
  author) → 48 candidates in `raw/_candidates/`. Unverified; most rest on
  search excerpts.

### Findings (provisional, pre-ingest)
- **The thesis narrows.** Evidence does not support "less structure is
  better". It supports something closer to: *drop procedure the model can
  derive; keep structure that carries knowledge, enforces invariants, or
  hands over context.*
  - Against: a pre-registered GAIA scaffold study (2606.08529) rejected
    "stronger models are less scaffold-sensitive"; the strongest model gained
    most. A full procedure in the system prompt beat a graph controller
    (2604.27891). Strong-model-written harnesses lift weak models 0.49→0.91 by
    moving reasoning into code (2608.12307).
  - For: Anthropic's harness-design post (newer models let them drop resets
    and decomposition, but they kept the planner and the evaluator); literal
    few-shot demos hurt reasoning models while abstracted insights help
    (2509.23196); vendor guidance on both sides now says outcome-first and to
    give the reason behind instructions.
- **Coverage, not length, is the live axis.** Unstated requirements are
  guessed right only ~41% of the time, and underspecified prompts regress ~2×
  across model changes (2505.13360). A terse brief is fragile when it is
  missing requirements, not because it is short.
- **LLM-authored context files hurt.** AGENTS.md evaluation (2602.11988): LLM-written files
  lower success and add >20% cost; human-written ones help slightly. This is
  direct evidence for founding question 5 and relevant to our own LLM-written
  skills.
- **Invariants → code** has support: CoT lowers adherence to simple hard
  constraints (2505.11423); the auto-mode classifier misses 17% of real
  overeager actions.
- **Human baseline:** intent transfer succeeded in ~34% of episodes in a
  command simulation (Shattuck & Woods 2000; verify).
- **Context handoff boundary:** Cognition argues some context must travel as
  full traces, not a brief. Pair this with the handoff-loss papers
  (2607.16133: stronger models lose more to relay loss).
- **Gaps:** no controlled study of goal-only vs procedural briefs on
  agentic tasks; no long-horizon procedure-vs-intent comparison. Both justify
  building our own harness.

### Next
- 03:00 curate sweep ingests the candidates; verify the snippet-sourced
  arXiv IDs during ingest.
- After ingest, revise research-plan Q1/Q3 around the coverage axis and
  the "derivable procedure vs knowledge-carrying structure" split. Consult
  Fable before reframing.
- Start sketching the harness task corpus from real claude-system skills
  (redacted).

## 2026-11-14

### Did
- ADR 0002 (decision-grade evaluation), then ADR 0003, which supersedes it
  and 0001: **literature and reference only, no in-house experiments.** Both
  made with Fable.
- Removed the experiment skill group, the experiment and notebook rules,
  and `experiments/`. Rewrote the research plan into open questions plus
  deliverables.
- Seeded `docs/writing-guide.md`; every line is `[provisional]` until ingest.

### Findings
- Our own experiments could never have passed `/elevate` Gate 1, so they had
  no path to the output they existed for.

### Next
- Overnight curate ingests the 48 candidates. Re-tag guide lines as
  sources are verified.
- Author-bias audit lives in a separate private QA repo (manual trigger).

### Later the same day: guide folded into claude-system

- The guide now leads with a rules block; P7 added; `scripts/check_guide.py`
  guards the duplicated evidence tags in CI.
- claude-system reviewed and updated against the guide (record:
  agentic-research `docs/system-proposals/2026-11-14-system-review-intent-briefing.md`).
  Its global `CLAUDE.md` carries P2, P1, P3 and P7 and points here.
- Finding from that review that belongs in the guide's evidence once a
  source backs it: restated contracts drift. Six skill contradictions were
  all two copies of one rule that had diverged. In-house only so far.
