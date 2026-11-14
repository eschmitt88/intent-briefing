# Research plan — intent-briefing

## The claim under test

When AI designs agentic systems it tends to write **scripts** (numbered
procedures and if/then trees) for a reader that is as capable as the author or
more so. The working hypothesis is that strong readers do better with a
**brief**: the goal, the hard constraints, the reasons behind them, and the
context the author would otherwise take for granted. The reader then derives
the method itself. The military analogue is mission command: the commander's
intent is given, and the subordinate chooses how to achieve it.

The project's job is to **find where this stops being true**, not to confirm
it. It does this by **curating what others have measured**. It runs no
experiments of its own ([ADR 0003](decisions/0003-literature-and-reference.md)).

## Two axes, not one dial

"Over-prescriptive" mixes up two separate things:

|                | terse                        | verbose                          |
|----------------|------------------------------|----------------------------------|
| **intent**     | goal + constraints only      | goal + constraints + rationale + context |
| **procedure**  | short checklist              | full step-by-step script         |

Sources are read against this 2×2, not against a single
"prescriptiveness" slider.

## The asymmetry that matters

The reader is a peer in **capability** but not in **context**. A subagent or
fresh session has none of the author's working memory. An intent brief only
works if that context is actually transferred. Mission command also assumes
shared doctrine, which here means CLAUDE.md, rules and skills. So when reading a
source, ask whether shared doctrine was available.

## Open questions (the literature is watched for these)

1. **Effect size.** On matched agentic tasks, does an intent brief match or
   beat a script for a frontier implementer, in outcome quality, tokens and
   turns? *Gap as of 2026-11-13: no controlled goal-vs-procedure study on
   agentic tasks.*
2. **Capability boundary.** At what implementer strength does the ordering
   flip? *Counter-evidence already in hand: the strongest model gained the
   most from scaffolding (2606.08529).*
3. **Invariant boundary.** Which instruction classes must stay explicit (or
   move to code) no matter how strong the model is?
4. **Horizon and drift.** Does intent framing drift more or less than a
   script over long autonomous runs? *Gap: no long-horizon procedure-vs-intent
   comparison.*
5. **Author bias.** Do frontier models over-script when they write briefs for
   peers? *The literature is indirect here (AGENTS.md evaluation 2602.11988).
   Our own author is audited separately, in a private repo; see ADR 0003.*

The 2026-07-31 instruction-ablation program is a **qualitative case study**
motivating Q3, not a natural experiment (ADR 0002).

## Deliverables

1. **Curated literature** in `literature/` and `concepts/`, kept current by
   `/digest` and `/curate` under `agency: max`.
2. **The writing guide**, `docs/writing-guide.md`: how to write system
   prompts, subagent briefs, skills and hooks for strong models. **Every line
   is marked with its evidence strength** and cites the notes behind it. This
   is the live reference claude-system pieces are refined against.
3. **Fold-back.** Hub `/elevate` proposals against claude-system once the
   evidence clears its gates. One candidate already named: a regression check
   on real invocations before a rewritten skill is promoted (engineering
   practice for claude-system, not research for this repo).

## Reading discipline

Strong-model judges like intent framing, so weight **task-outcome results**
over rubric or LLM-judge scores. Grade each source by `/elevate`'s evidence
gates (peer review, released code, independent attestation, credibility).
Read `~/claude-system/claude/rules/evaluation.md` before judging a source's
evaluation.
