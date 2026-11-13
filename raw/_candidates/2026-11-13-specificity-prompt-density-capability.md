---
kind: candidates
topic: "prompt specificity and instruction density as a function of model capability (scaffolding help/hurt by model strength; instruction-count effects; over- vs under-specification; vendor guidance for reasoning models)"
discovered: 2026-11-13
source: discover
n_requested: 12
n_returned: 12
---

Verification note: items 2, 4, 10, 11, 12 were checked against the primary page
(abstract or vendor doc); the rest rest on search-result excerpts and should be
confirmed at /fetch-paper time. Items 7-10 are the disconfirming or cautionary
set. Items 11-12 are vendor docs, not controlled studies.

## 1. You Don't Need Prompt Engineering Anymore: The Prompting Inversion

- url: https://arxiv.org/abs/2510.22251
- type: paper
- summary: A constraint-heavy "Sculpting" prompt beats standard CoT on gpt-4o (97% vs 93%) but loses on gpt-5 (94.0% vs 96.4%, full GSM8K), which the author calls a "guardrail-to-handcuff" transition.
- reason: The closest single result to our capability-boundary question (Q2), with a direct ordering flip across model generations; weak evidence (single author, one benchmark, one lineage) so treat as a hypothesis generator.

## 2. Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve

- url: https://arxiv.org/abs/2608.03550
- type: paper
- summary: Pushkin, Jiang et al. (Aug 2026) show few-shot CoT examples hurt reasoning-specialized mid-size models relative to a zero-shot prompt (Mathstral GSM8K ~77% to ~84%) and propose a "guidance-distraction" tradeoff in which prescriptive scaffolding pulls capable models off their own reasoning.
- reason: Gives a named mechanism (style/format imposition distracts) for why scripts decay in value with capability, and the most recent controlled evidence; still math-only.

## 3. Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting

- url: https://arxiv.org/abs/2506.07142
- type: paper
- summary: On GPQA Diamond with five non-reasoning and three reasoning models, explicit CoT gives small average gains for non-reasoning models (with more variance and some new errors) and only marginal gains for reasoning models at a large token/latency cost.
- reason: Clean capability-split comparison with a cost axis (tokens, time) matching our effect-size metric; also notes that forcing direct answers can hurt, so "less prescription" is not monotonically better.

## 4. From Harm to Help: Turning Reasoning In-Context Demos into Assets for Reasoning LMs

- url: https://arxiv.org/abs/2509.23196
- type: paper
- summary: Reasoning models trained with verifier-based RL do worse with few-shot CoT than direct answering even with optimal R1-trace demos (more exemplars, lower accuracy), via semantic misguidance and strategy-transfer failure; distilling demos into abstract "insights" (I2S) recovers gains (e.g. GPT-4.1 +14.0% on AIME'25).
- reason: The insight-vs-copy result is a direct analogue of intent vs script: abstracted guidance helps where literal worked examples hurt. Disconfirming-adjacent because it shows some guidance form still adds value for strong models.

## 5. The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning

- url: https://arxiv.org/abs/2504.05081
- type: paper
- summary: On pattern-based in-context learning, CoT underperforms direct answering across model families, and long-CoT reasoning models spend ~40x the inference tokens for comparable or worse results (TMLR 2025).
- reason: Explanation-by-mechanism (explicit-implicit duality) for when procedural scaffolding backfires; narrow task class, so check how far it generalizes to agentic work.

## 6. When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs

- url: https://arxiv.org/abs/2505.11423
- type: paper
- summary: Across 15-20+ models (NeurIPS 2025), eliciting CoT often lowers instruction-following accuracy by diverting attention from constraint tokens, though it helps on formatting and lexical precision; selective-reasoning strategies recover the loss.
- reason: Speaks to the invariant boundary (Q3): more reasoning can cost adherence to simple hard constraints, supporting putting invariants in code or hooks rather than relying on prose.

## 7. Curse of Instructions: Large Language Models Cannot Follow Multiple Instructions at Once (ManyIFEval)

- url: https://arxiv.org/abs/2509.21051
- type: paper
- summary: Holding the task fixed and varying the number of instructions, the probability of satisfying all of them drops sharply as count rises, for proprietary and open models alike.
- reason: Cuts toward "scripts are brittle at density": per-instruction compliance compounds multiplicatively, giving a quantitative reason a long checklist is risky even for strong models; also the dose-response design we can copy for density conditions.

## 8. How Many Instructions Can LLMs Follow at Once? (IFScale)

- url: https://arxiv.org/abs/2507.11538
- type: paper
- summary: Scales simultaneous keyword-inclusion instructions from 10 to 500 over 20 models; the best frontier model reaches only ~68% at 500, with three degradation patterns and a primacy bias toward earlier instructions.
- reason: Gives a capability-ordered density curve and an ordering effect (put hard constraints first); caveat that keyword-inclusion is synthetic, and a non-peer-reviewed Arize post (arize.com/blog/llm-instruction-following-benchmark-2026) claims the ceiling moved from ~200-300 to ~2,000 in a year, so the boundary is moving fast.

## 9. What Prompts Don't Say: Understanding and Managing Underspecification in LLM Prompts

- url: https://arxiv.org/abs/2505.13360
- type: paper
- summary: CMU (ACL 2026 Findings) finds LLMs fill unstated requirements correctly only ~41% of the time and inconsistently, underspecified prompts are ~2x as likely to regress across model/prompt changes, yet listing every requirement also backfires from competing constraints.
- reason: Strongest evidence AGAINST a naive "terse is better" reading: intent briefs that omit requirements are fragile. It supports the project's context-transfer point (the reader needs the author's context) and shows the real axis is requirement coverage, not verbosity.

## 10. Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

- url: https://arxiv.org/abs/2602.11988
- type: paper
- summary: ETH/LogicStar (Feb 2026, ICLR 2026) find context files lower task success versus none and add >20% cost; agents obey them faithfully, which drives broader exploration and testing; LLM-written files hurt most, developer-written slightly help, and the authors advise minimal, requirements-only content.
- reason: Controlled agentic evidence that more (doctrine-like) prose can hurt strong agents precisely because it is followed; directly relevant to our doctrine-availability variable and to author bias (LLM-authored context underperforms).

## 11. GPT-5.5 prompting guide (OpenAI)

- url: https://developers.openai.com/api/docs/guides/prompt-guidance.md
- type: post
- summary: OpenAI states that shorter, outcome-first prompts usually beat process-heavy prompt stacks, that GPT-5.5 does best when given outcome, success criteria, constraints and context and then picks the path, and that migration should restart from the smallest prompt that works rather than port old prompts.
- reason: Vendor statement of nearly our exact thesis, including stopping rules and success criteria as the retained explicit parts; vendor assertion, not a controlled study, and secondary sources (MindStudio etc.) overstate it.

## 12. Prompting best practices for Claude's latest models (Anthropic)

- url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- type: post
- summary: Advises giving the reason behind instructions, "prefer general instructions over prescriptive steps" because Claude's reasoning often exceeds a hand-written plan, softening CRITICAL/MUST emphasis that now over-triggers, and removing over-prompting added for weaker models.
- reason: The implementer-side vendor guidance for our actual reader; also contains the counterweight that newer models read instructions more literally and need explicit direction for things like tool use and subagent behavior, which belongs in our invariant-boundary list.
