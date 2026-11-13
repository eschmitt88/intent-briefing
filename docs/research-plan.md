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
it.

## Two axes, not one dial

"Over-prescriptive" mixes up two separate things:

|                | terse                        | verbose                          |
|----------------|------------------------------|----------------------------------|
| **intent**     | goal + constraints only      | goal + constraints + rationale + context |
| **procedure**  | short checklist              | full step-by-step script         |

Experimental conditions sample this 2×2. They do not sample a single
"prescriptiveness" slider.

## The asymmetry that matters

The reader is a peer in **capability** but not in **context**. A subagent or
fresh session has none of the author's working memory. An intent brief only
works if that context is actually transferred. Mission command also assumes
shared doctrine, which here means CLAUDE.md, rules and skills. So doctrine
availability is a variable to test, not a fixed background.

## Founding questions

1. **Effect size.** On matched tasks, does an intent brief match or beat a
   script for a frontier implementer? Measure outcome quality, tokens and
   turns.
2. **Capability boundary.** At what implementer strength (Haiku, Sonnet, Opus,
   older vs current) does the ordering flip? Prediction: scripts win below
   some threshold. Find that threshold.
3. **Invariant boundary.** Which instruction classes must stay explicit no
   matter how strong the model is: hard invariants (HCE holdout, paths,
   schemas), permission and safety limits, irreversible actions?
   Hypothesis: these belong in code or hooks, not in prose of either style.
   Test whether intent-only briefs violate them more often.
4. **Horizon and drift.** Over long chains (`/iterate --chain`, multi-hour
   max-agency runs), does intent framing drift more or less than a script?
   Which recovers better when the environment breaks the author's
   assumptions?
5. **Author bias.** When a frontier model writes briefs for peers, does it
   over-script by default? Does a one-line meta-instruction ("brief, don't
   script") fix that, or just produce vaguer scripts?
6. **Natural experiment.** Can the 2026-07-31 instruction-ablation program
   (claude-system skill prose cut from ~18k to ~7k words) be evaluated after
   the fact, using pre/post skill-failure and re-prompt rates?

## Phases

1. **Literature** (now). Prompt specificity and over-specification,
   instruction following vs instruction count, context engineering,
   delegation and briefing in multi-agent systems, mission-command doctrine,
   capability-dependent prompting effects, and the Bitter Lesson applied to
   scaffolding. Outputs: literature notes, concepts, a draft writing guide.
2. **Harness.** A small task corpus taken from real claude-system work
   (redacted), with brief variants per task cell, outcome-based scoring, and
   a held-out task split. Run through `claude -p` with pinned models.
3. **Experiments.** Q1–Q5 as experiments; Q6 from box telemetry.
4. **Fold-back.** `/elevate` proposals against claude-system skills, rules,
   hooks and subagent briefs, citing the July program as their predecessor.
   A living **writing guide** that future agentic pieces are written against.

## Evaluation discipline

HCE. Judges are strong models that will tend to *like* intent framing, so
rubric scores are secondary to task-outcome metrics: tests pass, invariants
held, artifact correct. Held-out tasks stay untouched during harness tuning.
