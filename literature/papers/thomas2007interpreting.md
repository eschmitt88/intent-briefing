---
kind: paper
title: "Interpreting Commander's Intent: Do we really know what we know and what we don't know?"
authors: ["Jeffrey A. Thomas", "Linda G. Pierce", "Melissa W. Dixon", "Gwenda Fong"]
institutions: ["U.S. Army Research Laboratory, Human Research and Engineering Directorate", "SAF Center for Military Experimentation (Singapore)"]
year: 2007
venue: "12th International Command and Control Research and Technology Symposium (ICCRTS), Newport RI; DTIC ADA481530"
peer_reviewed: unknown
url: "https://apps.dtic.mil/sti/html/tr/ADA481530/index.html"
code_url: null
citations: null
source: "raw/papers/thomas2007interpreting.pdf"
added: "2026-11-14"
relevance: 2
credibility: 1
status: read
related_experiments: []
related_concepts: ["[[concepts/commanders-intent]]", "[[concepts/handoff-context-loss]]"]
tags: [military, commanders-intent, situational-awareness, signal-detection, interoperability, human-teams]
---

# Interpreting Commander's Intent: Do we really know what we know and what we don't know?

## TL;DR

A symposium paper proposing true/false probes, scored with signal detection
theory (d'), to measure how well a coalition staff has absorbed commander's
intent. In the one two-run demonstration, the run with **degraded**
collaboration tools discriminated intent-consistent statements far better than
the run with full tools (d' 1.35 vs 0.49). The comparison is heavily
confounded, so this is a measurement-method paper, not evidence about how to
write intent.

## Claims

- Commander's intent (CI) is the "driver" of situational awareness. The paper
  uses SA and CI interchangeably.
- True/false probes are a cheap, real-time, minimally intrusive way to measure
  how far CI has spread through a distributed team.
- More collaboration technology does not by itself improve intent
  understanding ("additional technological capabilities are not solutions in
  and of themselves").

## Methods

- Setting: DARPA-sponsored Singapore Armed Forces / ARL-HRED coalition C2
  experiment, October 2006. A peace-enforcement scenario with a role-played
  Coalition Task Force HQ (25 roles) and two brigades (12 roles each), run
  twice.
- IV: interoperability. Run 1 used degraded C2 software (text chat, email, a
  shared drive, face-to-face meetings). Run 2 had full tools (VOIP, video,
  collaborative editing, whiteboards, maps). Different people and different
  commanders in each run.
- Probes: 24 true/false statements (3 sets of 8, given at start, midpoint and
  end). They were written from scenario documents and the commander's
  briefings, then updated from observed chat and email. Example: "Sharing
  information with NGOs is in line with the Commander's intent to avoid
  civilian casualties. [T]". Each probe had a 1–7 confidence rating.
- Analysis: hits, misses, false alarms and correct rejections converted to d'.
  Bias (β) was dropped as uninterpretable. One-way ANOVA across runs.
- Analyzed n: only participants who completed all 3 probe sets, 21 (Run 1)
  and 23 (Run 2).

## Results

- d' by run: Run 1 (degraded tools) M = 1.35, SD = 0.16. Run 2 (full tools)
  M = 0.49, SD = 0.10. F(1,43) = 14.858, p < 0.01. The direction is opposite
  to the hypothesis.
- No significant difference in confidence ratings between runs.
- Observed (qualitatively) in Run 1: the commander had a "stronger presence"
  and gave direct tasking to brigades. He also re-tasked a staff member as a
  "Crisis Manager" whose sole job was to make sure CI was understood across the
  HQ and brigades, through face-to-face meetings and email to brigade
  commanders. In Run 2 the commander was more inclusive, pushed full tool use,
  and staff "may have become overwhelmed or lost in the C2 tools" (signal
  officers watched up to 8 chats at once).
- Run 1 participants had far more prior SSTR/peacekeeping experience: 67%
  (33/50) vs 18% (7/38).

## Critique / open questions

- **Confounded, n = 2 at the unit level.** Run is fully confounded with the
  commander, leadership style, staff, and prior operational experience (67% vs
  18%). The d' gap cannot be attributed to tooling, let alone to how intent was
  communicated.
- Internal inconsistencies. The text says the significant result "fails to
  reject the null hypothesis", which misstates a significant effect in the
  non-hypothesized direction. The reported SDs (0.16, 0.10) look implausibly
  small for individual d' scores. They may be standard errors, but the paper
  doesn't say.
- The probes are partly written from the commander's own outputs. They measure
  agreement with the commander's framing, which is close to an "LLM-judge
  rubric" analogue rather than a task outcome. No mission-outcome measure is
  reported.
- The "About the authors" section reads "[To be Completed]", and the PDF
  includes the slide deck. This is a working symposium paper.
- 2×2 placement: none. Nothing varies how intent is written (terse/verbose,
  intent/procedure). What carries over is the qualitative observation that a
  dedicated human channel for propagating intent coincided with better shared
  understanding than richer tooling did.
- Shared doctrine: both runs were professional soldiers with long service
  (most 10+ years), so doctrine was largely shared. The variable that differed
  was operational experience.

## Trust signals

- **Credibility:** 1. A government-lab symposium paper (ICCRTS review is light,
  so peer review is unknown). Single confounded two-run comparison, internal
  errors, unfinished manuscript, no data released. Citations not looked up.
- Open access: public-release DTIC report (distribution unlimited). Retrieved
  from the Internet Archive's 2024-05-06 snapshot of
  `https://apps.dtic.mil/sti/pdfs/ADA481530.pdf` because DTIC blocked direct
  fetches.

## Follow-up

- The cited Leggatt (2004, 9th ICCRTS, "Objectively measuring the promulgation
  of commander's intent in a coalition effects based planning experiment
  (MNE3)") is the origin of the probe method. It may hold better-controlled
  numbers.
- **Relevance:** 2. It is on-topic for commander's intent but offers a
  measurement technique and a confounded single comparison. There is no
  evidence on how to word an intent brief.
- **Guide:** P5 refines (weak). In the better run, intent was actively relayed
  through a dedicated person and direct tasking, and the higher-bandwidth
  tooling did not help. This hints that propagating context needs an owner, not
  just a channel. The confounding is too heavy to move the tag.
