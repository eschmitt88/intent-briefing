---
kind: candidates
topic: "orchestrator-to-subagent briefing, context transfer and context engineering in multi-agent systems (delegation task descriptions, handoff failure modes, skill/tool/system-prompt design guidance)"
discovered: 2026-11-13
source: discover
n_requested: 12
n_returned: 12
curated: 2026-11-14
---

Note: summaries come from search-result snippets and secondary write-ups; no page was fully read. Verify before ingest, especially the three 2026 arXiv IDs (items 5, 6, 8), which the search tool surfaced but which were not opened.

## 1. How we built our multi-agent research system (Anthropic Engineering)

- url: https://www.anthropic.com/engineering/multi-agent-research-system
- type: post
- summary: Lead agent started with terse delegations ("research the semiconductor shortage"), which caused subagents to misread tasks and duplicate searches; the fix was a delegation spec with objective, output format, tool/source guidance and explicit task boundaries.
- reason: The canonical lab account of what goes wrong when an orchestrator under-briefs a peer-capability subagent, and of the brief anatomy that fixed it; directly feeds Q1, Q5 and the context-transfer asymmetry.

## 2. Don't Build Multi-Agents (Cognition / Walden Yan)

- url: https://cognition.ai/blog/dont-build-multi-agents
- type: post
- summary: Argues the first principle is to share full agent traces, not just messages, because a subtask handed over as a summary loses the implicit decisions that determine how it should be interpreted (Flappy Bird background/bird example).
- reason: Strongest practitioner counterweight to "just write a good brief": it claims some context cannot be compressed into a brief at all, which is a candidate boundary for the intent-brief thesis.

## 3. How and when to build multi-agent systems (LangChain / Harrison Chase)

- url: https://blog.langchain.com/how-and-when-to-build-multi-agent-systems
- type: post
- summary: Reconciles the Anthropic and Cognition posts: multi-agent works for independent, read-heavy subtasks and fails when subagents must coordinate on shared decisions or writes.
- reason: Gives the condition under which brief-only delegation suffices (low coupling) versus when trace sharing is needed; useful for designing task cells in the harness.

## 4. Why Do Multi-Agent LLM Systems Fail? (MAST, Cemri et al., arXiv 2503.13657)

- url: https://arxiv.org/abs/2503.13657
- type: paper
- summary: Taxonomy of 14 failure modes in 3 categories from 1,600+ annotated traces across 7 frameworks (NeurIPS 2025 D&B), with failures attributed largely to system design and inter-agent misalignment rather than base-model limits; includes released traces and an LLM annotator.
- reason: The main empirical failure taxonomy (specification issues, inter-agent misalignment, verification gaps) to label failure types in our harness, and traces we could reuse.

## 5. AgentCollabBench (arXiv 2605.08647)

- url: https://www.emergentmind.com/papers/2605.08647
- type: paper
- summary: Diagnostic benchmark of 900 human-validated tasks over five communication topologies measuring instruction decay, information loss, false-belief spread and cross-task leakage; notes pipelines can emit correct-looking output while silently dropping a constraint mid-chain.
- reason: Directly measures constraint loss across handoffs, which is our invariant-boundary question (Q3); ID and claims need verification (snippet only).

## 6. When Do Multi-Agent Systems Help? An Information Bottleneck Perspective (arXiv 2607.16133)

- url: https://www.alphaxiv.org/abs/2607.16133
- type: paper
- summary: Models each relay as an information bottleneck; stronger models gain less from compression and lose more from relay loss, with a WorkBench case where a relay dropped a deadline the executor needed.
- reason: Offers a capability-dependent theory of handoff loss that bears on Q2 (does ordering flip with implementer strength); snippet only, verify.

## 7. Handoff Debt: coding-agent takeover of interrupted work (arXiv 2606.02875)

- url: https://arxiv.org/abs/2606.02875
- type: paper
- summary: Builds 181 handoff scenarios from 75 SWE-bench Verified tasks to test whether a successor agent can continue from the state and notes a predecessor leaves (hidden assumptions, missing validation evidence).
- reason: Closest measured analogue to our fresh-session reader lacking the author's working memory; also relevant to the chain/horizon question (Q4). ID from search snippet, verify.

## 8. Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs (arXiv 2608.29028)

- url: https://arxiv.org/pdf/2608.29028
- type: paper
- summary: BOUND-Handoff testbed of 36 coordination scenarios, 720 runs over four handoff surfaces and five handoff conditions, studying loss of rules and boundaries while facts survive.
- reason: The title names exactly our worry (constraints and rationale drop out while task facts transfer); findings not seen, verify before relying on it.

## 9. Effective context engineering for AI agents (Anthropic Engineering)

- url: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- type: post
- summary: Defines context engineering as finding the smallest set of high-signal tokens; recommends system prompts at the right "altitude" (neither brittle if/then logic nor vague), plus compaction, note-taking and sub-agent architectures.
- reason: The lab's explicit statement against over-scripted prompts ("brittle logic") and for minimal high-signal context; the vocabulary the writing guide should use.

## 10. Writing effective tools for agents, with agents (Anthropic Engineering)

- url: https://anthropic.com/engineering/writing-tools-for-agents
- type: post
- summary: Tool design for non-deterministic readers: eval-driven iteration, agents refining their own tool descriptions, namespacing, token-efficient responses and instructive error messages.
- reason: Evidence that description wording is measurable and that agent-written descriptions help; supports treating tool and skill text as testable briefs.

## 11. Skill authoring best practices and Agent Skills design (Anthropic docs + engineering post)

- url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- type: post
- summary: Official guidance that skills should be concise, assume the model is already smart, set degrees of freedom to match task fragility, and use progressive disclosure (SKILL.md under about 500 lines); companion post at https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills.
- reason: Doctrine-side guidance, including the "degrees of freedom" framing that maps to our intent versus procedure axes, and relevant to the claude-system skill-prose ablation (Q6).

## 12. Intelligent AI Delegation (Tomasev, Franklin, Osindero, arXiv 2602.11865)

- url: https://arxiv.org/abs/2602.11865
- type: paper
- summary: Conceptual framework for delegation covering authority transfer, accountability, role and boundary specification, clarity of intent and trust, mapped onto MCP, A2A and related protocols.
- reason: The most prominent theory paper tying delegation to intent and boundaries, though reportedly non-empirical; useful as a conceptual anchor and for mission-command-style vocabulary.

## Curation

Curated 2026-11-14 by `/curate` (agency: max). Each item was checked against the full text; per-note discrepancies vs the summaries above are recorded in the literature notes.

- 1. Anthropic multi-agent research system — already in graph (hadfield2025multiagent)
- 2. Cognition, Don't Build Multi-Agents — ingested → yan2025multiagents
- 3. LangChain, How and when to build multi-agent systems — ingested → chase2025multiagent
- 4. MAST (2503.13657) — already in graph (cemri2025why)
- 5. AgentCollabBench (2605.08647) — ingested → mazumder2026agentcollabbench
- 6. Information Bottleneck (2607.16133) — ingested → yu2026when
- 7. Handoff Debt (2606.02875) — ingested → kc2026handoff
- 8. Facts Without Rules (2608.29028) — ingested → wang2026facts
- 9. Effective context engineering — ingested → rajasekaran2025effective
- 10. Writing effective tools for agents — ingested → aizawa2025writing
- 11. Skill authoring best practices + Agent Skills post — ingested → anthropic2026skill
- 12. Intelligent AI Delegation (2602.11865) — already in graph (tomasev2026intelligent)
