---
kind: paper
title: "In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks"
authors: ["Simon Dennis", "Michael Diamond", "Rivaan Patil", "Kevin Shabahang", "Hao Guo"]
institutions: ["i14", "University of Melbourne"]
year: 2026
venue: "arXiv preprint (cs.AI), v2 2026-05-05"
peer_reviewed: false
url: "https://arxiv.org/abs/2604.27891"
code_url: null
citations: null
source: "raw/papers/dennis2026incontext.pdf"
added: "2026-11-14"
relevance: 4
credibility: 2
status: read
related_experiments: []
related_concepts: ["[[concepts/scaffold-absorption]]", "[[concepts/handoff-context-loss]]", "[[concepts/durable-structure]]"]
tags: [orchestration, langgraph, procedure-in-prompt, llm-judge, customer-service, simulated-user]
---

# In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks

## TL;DR

The same model (Claude Sonnet 4.5) runs a known multi-turn customer-service
procedure in two ways. In one, the whole flowchart sits in the system prompt
and the model routes itself. In the other, a LangGraph orchestrator injects
per-node prompts and makes separate LLM routing calls at each decision hub.
The in-context version wins on all 15 judge comparisons, and judge-defined
"failures" fall from 24/9/17% to 11.5/0.5/5%. Both arms are full scripts,
though. What changes is who enforces the script (the model or external
code), not whether it is a script or a brief.

## Claims

- For procedural conversations, an external orchestrator is "dominated" by
  putting the whole procedure in the prompt. The cause given is that
  per-node generation fragments reasoning and adds routing failure modes.
- Orchestration costs 1.2–1.7× more LLM calls. In-context costs 1.3–1.4×
  more dollars, because the serialized procedure rides in every call.
- "External orchestration may have been necessary for earlier models." This
  is asserted. No earlier or weaker model is tested.

## Methods

- Three synthetic domains: travel booking (14 nodes, 3 hubs), Zoom support
  (14 nodes, 3 hubs) and insurance claims (55 nodes, 6 hubs). Each domain has
  n = 200 scenarios per condition, 1,200 conversations in total.
- Agent model: `claude-sonnet-4-5-20250929` in both arms. The user simulator
  is also Claude Sonnet and does not see the flowchart.
- In-context arm: the serialized flowchart (~6k characters for travel, ~4k
  tokens for insurance) is appended to the system prompt with "You must
  follow this procedure step by step… Do NOT mention step numbers." LangGraph
  arm: the node template is inserted per turn, plus an extra routing LLM call
  at each hub.
- Evaluation: a Claude Sonnet LLM judge scores five 1–5 rubric criteria (Task
  Success, Info Accuracy, Consistency, Graceful Handling, Naturalness). All
  1,200 conversations were re-scored by a GPT-4.1 judge. Mann-Whitney U with
  Holm-Bonferroni correction.

## Results

- **Failure rates (Table 5), verified.** Travel 24.0% (48/200) LangGraph vs
  11.5% (23/200) in-context. Zoom 9.0% (18) vs 0.5% (1). Insurance 17.0% (34)
  vs 5.0% (10). **"Failure" means the Claude judge scored Task Success ≤ 3.
  This is a judge-rubric metric, not a task-outcome metric.** No environment
  state or verifier is checked. Task Success is itself a rubric about
  reaching a terminal state.
- Claude judge (Table 1): in-context 4.53–5.00 vs LangGraph 4.17–4.84. All
  15/15 differences are significant, d = 0.37–1.01.
- GPT-4.1 judge (Table 2): 11/15 significant for in-context, 0 for
  LangGraph. Naturalness collapses to near-parity (Δ ≤ 0.06), which the
  authors concede fits self-preference. Graceful Handling is non-significant
  in Zoom and insurance, and LangGraph trends higher (−0.06, −0.13). Task
  Success Δ under GPT-4.1 is +0.17 to +0.27.
- Efficiency (Table 3): LLM calls/conversation 8.7 vs 10.8, 6.9 vs 9.4 and
  10.0 vs 17.3. Tokens/conversation are higher for in-context (27.7k vs
  17.6k, 21.4k vs 12.5k, 68.1k vs 42.9k). Turns are 16.4 vs 16.5, 12.7 vs
  14.7 and 19.0 vs 26.4.

## Critique / open questions

- **Metric class.** Every quality number, including the headline failure
  rates, comes from an LLM judge. The primary judge is from the same family
  as the agent and the user simulator. The GPT-4.1 replication helps, and the
  Task Success / Info Accuracy / Consistency direction survives it, but there
  is no task-outcome check: no booking database state, no correct Zoom fix
  verified, no claim adjudication. Per the project's reading discipline, the
  effect size is weak evidence. The direction is moderately robust.
- **Single model, single lineage.** One agent model (Sonnet 4.5), one
  orchestrator (LangGraph), synthetic procedures, a simulated user from the
  same family. The "earlier models needed it" framing is untested: there is
  no weaker-model arm, so it says nothing about the Q2 capability boundary.
- **Confound in the LangGraph arm.** The per-node arm also loses the global
  procedure view, and it adds a separate routing call. "Orchestration" here
  bundles three things: context fragmentation (the model sees only the
  current node's template), external routing by a separate classifier call,
  and template constraint. The appendix examples (lost per-person budget,
  re-asking answered questions) look like context loss, not control-flow
  enforcement as such.
- **2×2 position.** Both arms are **verbose procedure**. The in-context
  prompt is a full numbered flowchart with explicit routes and "follow this
  procedure step by step". So this is not evidence for intent over script.
  It is evidence that a script the model holds whole beats the same script
  fed node-by-node by code. Shared doctrine is not at issue.
- No released code or conversation logs are mentioned. "i14" appears to be a
  company. The judge-anchor rule "cap at 3 if no challenges" interacts with
  the scores. GPT-4.1 applied it more strictly to the smoother in-context
  runs.
- **Discrepancy vs candidate summary:** the numbers are quoted correctly.
  But the summary's "failure 24% vs 11.5%…" reads like task failure, and it
  is a judge-score threshold. Its framing of the paper as evidence that
  "external control structure became net-negative for a frontier model" is
  fair. Its own caveat (still a full script) is correct and important.

## Trust signals

- **Credibility:** 2. Small-company and university preprint, not peer
  reviewed, no code or logs released, single model, judge-only metrics with
  a same-family primary judge. The cross-family judge replication and n =
  200 per cell with corrected tests earn it a 2 rather than a 1.

## Follow-up

- **Relevance:** 4. This is the cleanest controlled comparison in hand of
  "who holds the procedure" (model context vs external code) for a frontier
  model. It bears directly on P4 and P5, and it is often miscited as an
  intent-vs-script result.
- **Guide:** P4 refines. The guide cites it in support of "keep structure",
  but it shows that *externally enforced control flow* that fragments context
  hurt a frontier model. The structure that helped was the same procedure
  kept whole in the prompt. So the line should separate "structure as
  knowledge given to the model" (kept) from "structure as code that hides
  context from the model" (harmful here). It does not support the
  strongest-model-gains-most claim.
- **Guide:** P5 supports. The failure modes are context-loss failures across
  node boundaries.
- Check the companion paper (Dennis et al. 2026, "Compiling agentic workflows
  into LLM weights") for a weaker-model arm.
