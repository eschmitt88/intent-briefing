---
kind: post
title: "How we built our multi-agent research system"
author: "Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford"
institutions: ["Anthropic"]
year: 2025
published: "2025-06-13"
venue: "Anthropic Engineering blog"
peer_reviewed: false
url: https://www.anthropic.com/engineering/multi-agent-research-system
code_url: https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents/prompts
citations: null
source: "raw/web/anthropic.com-multi-agent-research-system.md"
added: "2026-11-14"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/brief-anatomy]]", "[[concepts/requirement-coverage]]", "[[concepts/handoff-context-loss]]", "[[concepts/llm-authored-instructions]]"]
tags: [multi-agent, delegation, orchestrator-worker, vendor-account, prompt-engineering]
---

# How we built our multi-agent research system

## TL;DR

Anthropic's account of building Claude Research (an Opus lead agent that
spawns parallel Sonnet subagents). Its delegation lesson is that short,
topic-only subtask descriptions ("research the semiconductor shortage") led
subagents to misread tasks and duplicate each other. The fix was a delegation
spec: objective, output format, tool/source guidance and clear task
boundaries. The headline numbers come from an internal eval and an analysis
of variance, not from a controlled ablation of delegation style.

## Claims

Measured (internal data; no n, CIs or eval set released unless noted):
- Multi-agent (Opus 4 lead + Sonnet 4 subagents) "outperformed single-agent
  Claude Opus 4 by 90.2% on our internal research eval". The eval and its
  scoring are not described for this number. The eval section describes an
  LLM-judge rubric (0.0–1.0 + pass/fail), so the number is probably
  judge-scored.
- On BrowseComp, three factors explain 95% of performance variance. Token
  usage alone explains 80%. Number of tool calls and model choice are the
  other two.
- Upgrading to Sonnet 4 is "a larger performance gain than doubling the
  token budget on Claude Sonnet 3.7". No numbers are given.
- Agents use ~4x the tokens of chat. Multi-agent systems use ~15x.
- Parallelization (lead spawns 3–5 subagents at once, each subagent runs 3+
  tools in parallel) "cut research time by up to 90% for complex queries".
  That is a maximum, not a mean.
- A tool-testing agent that rewrote a flawed MCP tool description gave a 40%
  decrease in task completion time for later agents using the new
  description.
- Early eval set: ~20 queries drawn from real usage. "A prompt tweak might
  boost success rates from 30% to 80%" is illustrative, not a reported
  result.

Asserted (observation or design rationale, no numbers):
- **Delegation anecdote (verified in the post itself).** "We started by
  allowing the lead agent to give simple, short instructions like 'research
  the semiconductor shortage,' but found these instructions often were vague
  enough that subagents misinterpreted the task or performed the exact same
  searches as other agents. For instance, one subagent explored the 2021
  automotive chip crisis while 2 others duplicated work investigating current
  2025 supply chains, without an effective division of labor."
- Recommended delegation anatomy (post): "Each subagent needs an objective,
  an output format, guidance on the tools and sources to use, and clear task
  boundaries. Without detailed task descriptions, agents duplicate work,
  leave gaps, or fail to find necessary information."
- Agents misjudge effort, so explicit scaling rules went into the prompt: 1
  agent / 3–10 tool calls for fact-finding, 2–4 subagents / 10–15 calls each
  for comparisons, >10 subagents with divided responsibilities for complex
  research. Early failures included spawning 50 subagents for simple queries.
- "Our prompting strategy focuses on instilling good heuristics rather than
  rigid rules", plus "explicit guardrails" against spiralling. The best
  prompts are "not just strict instructions, but frameworks for
  collaboration that define the division of labor, problem-solving
  approaches, and effort budgets."
- Claude 4 models are "excellent prompt engineers" when given a prompt and a
  failure mode.
- Multi-agent suits breadth-first, parallelizable, read-heavy work. Domains
  where all agents must share context, or with many inter-agent
  dependencies, are a poor fit. Most coding is one of these.
- Appendix: subagents write outputs to a filesystem and pass back references
  to avoid a "game of telephone". Long-horizon agents summarize finished
  phases into external memory and hand off to fresh subagents.

## Methods / basis

- A practitioner retrospective on a production system. Evidence comes from
  internal evals (an LLM-judge rubric covering factual accuracy, citation
  accuracy, completeness, source quality and tool efficiency; the authors
  say a single-call judge was the most consistent with human judgement),
  human testing, the public BrowseComp benchmark, and Console simulations
  where the authors watched agents step by step.
- The lead-agent, subagent and citation-agent prompts were released in the
  Claude Cookbooks repo (`patterns/agents/prompts/`, first committed
  2025-06-13). The released lead prompt extends the four-part spec to seven
  items: one core objective, expected output format, background context and
  how the subtask fits the plan, key questions, suggested starting
  sources plus a definition of source quality, specific tools, and "if
  needed, precise scope boundaries". It also contains a worked "good" version
  of the semiconductor delegation. That example names specific sources (TSMC/
  Samsung/Intel investor relations, SEC EDGAR, SEMI/Gartner/IDC, CHIPS Act
  portals), focus questions and an output contract.

## Results

- No result isolates the delegation change. The terse-to-detailed
  delegation fix is reported qualitatively, with no before/after numbers.
- The 90.2% gain is token-unmatched: multi-agent is ~15x chat tokens against
  ~4x for a single agent. The post's own variance analysis attributes most
  performance to token spend.

## Critique / open questions

- **Evaluation quality.** The headline 90.2% is on an unreleased internal
  eval, probably LLM-judged, with no n, variance or comparison protocol.
  BrowseComp is a task-outcome benchmark (exact answers), so the
  80%/95%-of-variance figures carry more weight, but the regression, the
  sample and the model set are not reported. Single lineage (Claude only),
  single domain (web research).
- **Token confound.** "Token usage explains 80% of variance" means
  architecture comparisons that don't match spend mostly measure spend. A
  brief-vs-script comparison has the same problem: a detailed delegation also
  makes subagents spend differently.
- **On the 2x2.** The failing starting point was not even terse intent. It
  was a bare topic with no goal, constraints or boundaries. The fix moves to
  **verbose intent** (objective, context, output contract, boundaries), with
  some **terse procedure** added: effort-scaling numbers, parallelism
  counts, "start wide then narrow". The released example also carries
  procedural hints (where to look first). The authors frame the result as
  "heuristics rather than rigid rules", so this is coverage, not scripting.
- **Q5 (author bias).** Left alone, the orchestrator model *under*-specified
  its subtasks. It did not over-script. That is evidence against a pure
  "models over-script" view, at least for 2025-era orchestrators writing
  briefs on the fly. The post does not say which model was the lead during
  that early phase.
- **Q2.** "Sonnet 4 > 2x tokens on Sonnet 3.7" suggests capability buys more
  than budget. It says nothing about instruction style.
- **Q3.** Effort budgets and guardrails were made explicit because the model
  misjudged them. They are a candidate class of instruction that stays
  explicit.

## Trust signals

- **Credibility:** 3. This is a primary builder account from the model
  vendor, with named authors and the production prompts released (a real
  artifact). But it is not peer reviewed, the key numbers come from
  unreleased internal evals with no n or variance, and the delegation lesson
  itself is anecdotal.
- Commentary by others (e.g. LangChain's write-up, `chase2025multiagent`)
  quotes the semiconductor anecdote verbatim from this post.

## Follow-up

- **Relevance:** 5. This is the canonical primary account of an orchestrator
  under-briefing a peer-capability subagent and of the delegation anatomy
  that fixed it. It feeds Q1, Q3, Q5 and the context asymmetry directly.
- **Guide:** P1 refines. The brief that worked was not "goal only": it adds
  output format, tool/source guidance and explicit boundaries, plus numeric
  effort budgets. "Brief, don't script" has to mean full coverage, not
  terseness.
- **Guide:** P2 supports. Unstated boundaries and output contracts caused
  duplicated and misdirected work.
- **Guide:** P5 supports. The lead's plan and division of labor have to
  travel to each subagent, and filesystem artifacts avoid the "game of
  telephone".
- **Guide:** P6 refines. LLM-rewritten tool descriptions *helped* (40%
  faster completion), but only inside a test-against-failures loop, unlike
  the unguided generation in 2602.11988.
- Candidate follow-up: ingest the released prompts
  (`anthropics/claude-cookbooks` `patterns/agents/prompts/`) as a repo
  snapshot. They are a concrete specimen of a vendor-written delegation
  brief.
