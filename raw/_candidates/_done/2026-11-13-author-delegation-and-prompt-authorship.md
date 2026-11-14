---
kind: candidates
topic: "Author side of briefs: commander's intent / delegation research, and author bias in LLM-written prompts"
discovered: 2026-11-13
source: discover
n_requested: 12
n_returned: 12
curated: 2026-11-14
---

Sweep scope: (A) human delegation and mission-command doctrine as tested
principles; (B) whether LLM-authored prompts/briefs over-specify and whether
they transfer across target models. Verification status is stated per entry:
most facts below come from search snippets, not full-text reads.

Headline gap for (B): no search surfaced a controlled study of orchestrator
or meta-prompt authors over-scripting relative to human authors. Evidence is
indirect (optimizer prompt bloat, overfitting, partial transfer). Founding
question 5 may be genuinely open; treat that as a finding, not a search failure.

## 1. Communication of Intent in Military Command and Control Systems (Shattuck & Woods, 2000)

- url: https://rd.springer.com/chapter/10.1007/978-1-4615-4229-2_19
- type: paper
- summary: Simulation study with Army battalion commanders and their company commanders; subordinates matched the commander's intent in only about 34% of episodes, and successful ones first established friendly/enemy disposition and actually consulted the intent statement.
- reason: Rare empirical test of whether stated intent is received as intended; the 34% figure (from secondary copies, verify) and the "doctrinal terms read differently" finding bear directly on the context-transfer and shared-doctrine variables.

## 2. How we built our multi-agent research system (Anthropic Engineering)

- url: https://www.anthropic.com/engineering/multi-agent-research-system
- type: post
- summary: Lead-agent/subagent system whose delegation lessons say each subagent needs an objective, output format, tool/source guidance and explicit task boundaries, with vague subtask descriptions causing duplicated or misdirected work.
- reason: Closest primary practitioner evidence on orchestrator-written subtasks; note it argues for MORE explicit boundaries, so it marks a place where the brief-not-script thesis needs care. (The "automotive chip crisis duplication" anecdote is from a third-party write-up; confirm in the post.)

## 3. Intelligent AI Delegation (Tomasev, Franklin, Osindero; Google DeepMind, arXiv 2602.11865)

- url: https://arxiv.org/abs/2602.11865
- type: paper
- summary: Framework treating delegation as transfer of authority, responsibility, accountability and role specification, with monitoring, trust calibration and delegation chains, mapped onto principal-agent problems.
- reason: Best current bridge from human delegation theory to agent-to-agent briefing and the specification problem; framework only, no empirical evaluation, so use for vocabulary and hypotheses.

## 4. Why Do Multi-Agent LLM Systems Fail? (Cemri et al., MAST, arXiv 2503.13657)

- url: https://arxiv.org/abs/2503.13657
- type: paper
- summary: Taxonomy of 14 failure modes from 150+ annotated traces in three groups (specification issues, inter-agent misalignment, task verification), including disobeying task specification and withholding information.
- reason: Empirical base rates for how briefs and handoffs fail in practice; check whether "specification" failures are under- or over-specification (percentages in summaries need checking against the PDF).

## 5. What Prompts Don't Say: Understanding and Managing Underspecification in LLM Prompts (arXiv 2505.13360)

- url: https://arxiv.org/abs/2505.13360
- type: paper
- summary: Shows many requirements go unspecified in real prompts yet models often infer them, that accuracy falls as more requirements are stated explicitly (about 85% at 19 requirements for gpt-4o), and proposes requirements-aware prompt optimization (+4.8% over specify-everything baselines).
- reason: Direct evidence on both sides of the intent-vs-script question (underspecification is often fine, stuffing everything in hurts) and on the author's choice of what to state.

## 6. Interpreting Commander's Intent: Do We Really Know What We Know and What We Don't Know (DTIC ADA481530)

- url: https://apps.dtic.mil/sti/html/tr/ADA481530/index.html
- type: paper
- summary: Military research report on how commander's intent is formulated and interpreted, in the line of Shattuck's four-part model (formulation, communication, interpretation, implementation); related Hoffman & Shattuck (2006, Military Review) found purpose statements often just restate the mission.
- reason: Tested failure modes of intent statements themselves (intent that merely recaps the task), which maps onto "rationale" sections that carry no information; contents not yet read, verify.

## 7. Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity (Klein, Woods, Bradshaw, Hoffman, Feltovich, 2004)

- url: https://archive.cps-vo.org/node/62405
- type: paper
- summary: Argues automation must support common ground, predictability, directability and goal negotiation to function as a teammate, and warns that coordination overhead can swamp task work.
- reason: Foundational human-AI teaming statement of the specification/common-ground problem and a counterweight (coordination cost) to "transfer all context"; 2023 follow-up arXiv 2303.12040 says the gaps remain.

## 8. Determinants of Delegation and Consultation by Managers (Yukl & Fu, 1999)

- url: https://core.ac.uk/download/205208894.pdf
- type: paper
- summary: Survey and interview study showing how much managers delegate depends on subordinate characteristics and relationship quality (LMX), with managers reluctant to hand important decisions to inexperienced subordinates.
- reason: Organizational-science grounding for the capability/trust boundary (Q2): delegation breadth tracks perceived subordinate competence and trust, the human analogue of a Haiku-vs-Opus threshold.

## 9. When Mission Command Fails: Limitations and Historical Examples (Vandergriff) and the 2025 NATO senior-officer study it cites

- url: https://donvandergriff.substack.com/p/when-mission-command-fails-limitations
- type: post
- summary: Lists prerequisites for mission command (clear intent, trained subordinates, mutual trust, flexible environment, robust communication) with historical breakdowns (Antietam, France 1940, Market Garden); cites a 2025 study finding NATO officers interpret written mission-command doctrine differently.
- reason: Direct statement of where the doctrine breaks, mapping onto doctrine-availability and context-asymmetry variables. Secondary source: chase the underlying NATO study and the NATO AJP-01 text before ingesting any claim.

## 10. GRACE: Gated Refinement and Adaptive Compression for Prompt Optimization (arXiv 2509.23387)

- url: https://arxiv.org/abs/2509.23387
- type: paper
- summary: Prompt optimizer that adds compression; prompts optimized on DeepSeek-V3 transfer to Llama-3.3-70B and GPT-4.1 with gains largest on the source model and occasionally below the initial prompt on the target.
- reason: Concrete cross-target-model transfer numbers for machine-authored prompts, plus an optimizer that explicitly fights prompt growth.

## 11. Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis (Gong & Wen, arXiv 2605.26655)

- url: https://arxiv.org/abs/2605.26655
- type: paper
- summary: Edit-level analysis of optimizers finding that an optimized prompt's advantage on one benchmark often fails to transfer to another, even across different LLM backbones.
- reason: Tells us which kinds of edits optimizers make carry over (content) versus not (model/benchmark-specific); related Amazon ICLR 2026 paper reports semantic directives transfer while schema/format must be adapted.

## 12. Prompt bloat in optimizer-written prompts: SAGE (arXiv 2606.18902) and ESPO (arXiv 2609.04197)

- url: https://arxiv.org/abs/2606.18902
- type: paper
- summary: Report that reflective optimizers such as GEPA accumulate rules and edge cases, growing prompts (one to about 12K tokens, claims of up to 3x longer) without matching accuracy gains, tracking overfitting; a Decagon production blog reports the same.
- reason: Best available indirect evidence that LLM authors over-specify when left to iterate; the 3x figure is from an aggregator, so verify in the papers. Also see Smartling's GEPA vs expert prompts (arXiv 2603.25169): no consistent winner, no length comparison.

---

Considered, not included: Suzgun & Kalai meta-prompting (arXiv 2401.12954; conductor/expert design, no author-bias analysis); Ambig-SWE (arXiv 2502.13069) and "Ask or Assume?" (arXiv 2603.26233) on agents failing to detect underspecification (likely better under the sibling reader-side sweep); practitioner delegation guides (no empirical content).

## Curation

Curated 2026-11-14 by `/curate` (agency: max). Each item was checked against the full text; per-note discrepancies vs the summaries above are recorded in the literature notes.

- 1. Shattuck & Woods 2000 — declined — the Springer chapter is paywalled (closed access); the only open copy is an unofficial Scribd upload, not used. A secondary reproduction (Shattuck, "Communicating Intent and Imparting Presence", on coloradofirecamp.com, venue unverified) reports 11/32 episodes (34%) matched intent; ingest that if its venue can be confirmed.
- 2. Anthropic multi-agent research system — ingested → hadfield2025multiagent
- 3. Intelligent AI Delegation (2602.11865) — ingested → tomasev2026intelligent
- 4. MAST (2503.13657) — ingested → cemri2025why
- 5. What Prompts Don't Say (2505.13360) — ingested → yang2025what
- 6. Interpreting Commander's Intent (DTIC ADA481530) — ingested → thomas2007interpreting
- 7. Klein et al. 2004, Ten Challenges — declined — position paper with no measurements; its common-ground/directability framing is covered by measured handoff sources (wang2026facts, kc2026handoff).
- 8. Yukl & Fu 1999 — declined — tangential: a 1999 survey of what drives managers to delegate; the capability/trust analogy tests nothing about instruction design.
- 9. Vandergriff, When Mission Command Fails — declined — secondary blog; its load-bearing claim (a 2025 NATO study of how officers read doctrine) should be found and ingested from the primary source.
- 10. GRACE (2509.23387) — ingested → shi2025loss
- 11. Gong & Wen (2605.26655) — ingested → gong2026prompt
- 12. SAGE (2606.18902) + ESPO (2609.04197) — ingested → zhu2026sage, liu2026espo
