---
kind: paper
title: "Improving Environment-Agnostic Agents: The Role of Scaffolding"
authors: ["Sergey Rodionov"]
institutions: ["SingularityNET"]
year: 2026
venue: "arXiv preprint (cs.AI), v3 2026-10-22"
peer_reviewed: false
url: "https://arxiv.org/abs/2610.22289"
code_url: "https://github.com/astroseger/envtraverse"
citations: 0
source: "raw/papers/rodionov2026improving.pdf"
added: "2026-11-14"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/invariants-in-code]]", "[[concepts/durable-structure]]", "[[concepts/scaffold-absorption]]", "[[concepts/guidance-distraction]]"]
tags: [scaffolding, bitter-lesson, codex, arc-agi-3, agi-maze, terminal-bench, return-of-control, controller]
---

# Improving Environment-Agnostic Agents: The Role of Scaffolding

## TL;DR

The setup is one Codex-based agent, deployed unchanged across ARC-AGI-3, AGI
Maze and Terminal-Bench 2.1, on GPT-5.5 (high, xhigh) and GPT-5.6-sol
(xhigh, max). Swapping one continuation sentence for a "stop and report when
unsure" instruction raises game scores. Moving an ARC reset convention,
*already stated in the prose description*, into a scripted controller
recovers 34–60% of the gap to a specialized ARC agent. Even at GPT-5.6-sol
max, the specialized agent leads by ~7 points. Extra tutorial *experience*
(practice mazes) hurt GPT-5.5 but helped GPT-5.6-sol xhigh. The gains come
with more tokens, which the author cannot separate from the gains.

## Claims

- A small, environment-independent instruction change can improve a general
  agent beyond the environment it was tuned on, without regressing others
  (Terminal-Bench: small and mixed).
- Developer-supplied procedures "still matter for the models tested",
  including GPT-5.6-sol at max effort.
- Having information and tools available is not the same as using them.
  Prescribed organization and control help even when they add no new facts.
- The experiments do not separate better information use from more, or
  differently allocated, inference.

## Methods

- Agents: **Baseline** ("Continue working until you have completed your
  task.") vs **Stop-and-report** ("Continue… as long as you can proceed
  confidently. If you encounter a problem, ambiguity, unexpected issue, or
  anything that makes you unsure how to proceed, stop and report it back to
  me before taking further action."). The controller answers each report
  with only a goal reminder and no task advice.
- ARC-only diagnostics. **Controlled_RESET** is Stop-and-report plus "You
  are forbidden to call RESET by yourself", with the controller issuing
  RESET at GAME_OVER. That convention was already in the environment
  description. **twma_v1.61** is the author's earlier ARC-specific agent: it
  organizes observations by level and attempt, manages resets in the
  controller, and *requires* a persistent textual world model.
- Benchmarks: ARC-AGI-3 (25 public games, RHAE). AGI Maze (106 targets, a
  custom RHAE70 score, single and curriculum settings; the curriculum adds 7
  tutorial mazes). Terminal-Bench 2.1 (89 tasks, verifier reward). All are
  **task-outcome metrics**, with no LLM judge.
- 3 evaluation blocks per condition (2 where blocks were excluded for
  web-search leakage). Means only, with no significance tests: "direction
  alone does not establish statistical significance".

## Results

ARC-AGI-3 mean RHAE (cost in M normalized tokens), Table 1:

| model / effort | Baseline | Stop-and-report | Controlled_RESET | twma_v1.61 |
|---|---|---|---|---|
| GPT-5.5 high | 27.57 (9.4) | 34.86 (14.2) | 45.92 (42.2) | 53.19 (64.1) |
| GPT-5.5 xhigh | 50.45 (16.1) | 52.36 (20.2) | 61.44 (45.5) | 71.11 (63.6) |
| GPT-5.6-sol xhigh | 70.81 (16.3) | 77.33 (16.6) | 84.59 (18.4) | 92.24 (27.0) |
| GPT-5.6-sol max | 89.59 (15.3) | 90.96 (18.0) | 93.31 (18.9) | 97.85 (26.3) |

- Stop-and-report beats Baseline in all four ARC configurations (+1.37 to
  +7.29) and in 7/8 AGI Maze comparisons (−0.20 to +5.23 RHAE70).
  Terminal-Bench differences run from −1.50 to +2.25 (mixed). Cost rises
  2–52% on ARC and 7–40% on Maze.
- The specialization gap (twma minus Stop-and-report) **shrinks as the model
  strengthens**: 18.3, 18.8, 14.9, 6.9 points (my arithmetic from Table 1).
  Part of that is ceiling, since twma reaches 97.85. Controlled_RESET closes
  60%, 48%, 49% and 34% of the gap respectively. That matches the paper's
  "34–60%".
- AGI Maze curriculum (tutorials first) vs single: lower RHAE70 for both
  GPT-5.5 agents at both efforts (e.g. Baseline xhigh 63.32 → 58.35). Higher
  for both agents at GPT-5.6-sol xhigh (60.35 → 62.62; 63.26 → 65.69). Mixed
  at max (Baseline 69.35 → 68.03; Stop-and-report 71.87 → 73.26).
  Curriculum always costs more tokens.

## Critique / open questions

- **The strongest finding for this project is Controlled_RESET.** A rule
  that was *already in the prose* ("reset after GAME_OVER, avoid it
  otherwise") gained 2.4–11 RHAE points when moved into controller code.
  That is a direct, if small, task-outcome instance of "invariants in code,
  not prose" for frontier models. Because the controller also performs the
  reset, it removes a decision as well as enforcing a rule.
- **Stop-and-report is closer to intent than to script.** It tells the agent
  *when* to hand back control, not *how* to solve the task. The controller's
  reply is a bare goal reminder. On the 2×2 it is a terse addition on the
  control axis, not procedure. twma is verbose procedure plus enforced
  organization. The result stacks up as: terse control instruction < code
  enforcement of one convention < full prescribed organization, with the
  gap narrowing at higher capability.
- **The confound is inference volume.** Score and cost orderings match
  exactly across the four ARC agents. The author says plainly that the gains
  may be extra compute, not better procedure. Comparisons are not at matched
  cost.
- **"Tutorials hurt" needs care.** These are practice episodes played in the
  same run (experience in context), not written tutorials. They hurt GPT-5.5
  and helped GPT-5.6-sol xhigh, so this is model-dependent, not a general
  "examples hurt" result. It fits loosely with guidance-distraction and
  context-load effects.
- Weaknesses: single author, n = 2–3 blocks with no inferential stats, one
  model lineage (OpenAI Codex), a custom Maze metric, and the Stop-and-report
  instruction was selected on ARC (though not on Maze). Strengths: three
  environments, an all-or-nothing replacement policy, documented leakage
  exclusions, code and run artifacts released.
- **Discrepancy vs candidate summary:** none material. "Extra tutorial
  experience sometimes hurt" is accurate. The orchestrator brief's
  "procedures… which hurt (tutorials)" overstates it: they hurt GPT-5.5 and
  helped one GPT-5.6-sol configuration, and they are experience, not a
  supplied procedure.

## Trust signals

- **Credibility:** 3. Code and full run artifacts released (EnvTraverse),
  task-outcome metrics on three public benchmarks, careful leakage controls
  and exclusion rules, results reported per run. But: single author, small
  company, not peer reviewed, 2–3 blocks with no significance testing, one
  model family.

## Follow-up

- **Relevance:** 4. A recent, controlled, task-outcome look at which supplied
  structure survives frontier capability. It isolates one prose-to-code move.
- **Guide:** P3 supports. Moving an already-stated convention from prose into
  the controller improved frontier-model outcomes (Controlled_RESET).
- **Guide:** P4 supports, with a refinement. Prescribed organization and
  control still help at GPT-5.6-sol max (~7 points). The advantage shrank
  from ~18 to ~7 points as capability rose, which fits scaffold absorption
  with a residual.
- **Guide:** P1 refines. A terse control-axis instruction (when to return
  control) helped, at more token cost. That is weak evidence that a brief can
  usefully say when to stop and escalate, not just state the goal.
- Look at the author's prior ARC-AGI-3 studies (refs [8], [9]) for the
  model-capability vs scaffold-variant comparison.
