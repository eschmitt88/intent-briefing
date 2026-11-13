---
kind: candidates
topic: "Bitter Lesson applied to agent scaffolds and harnesses: ablations across model generations, minimal harnesses, long-horizon drift, and where deterministic structure stays necessary"
discovered: 2026-11-13
source: discover
n_requested: 12
n_returned: 12
---

Triage notes: arXiv abstract pages were fetched for items marked (abs-verified); others are blog/vendor pages read via WebFetch or only seen in search snippets (marked snippet-only). No full PDFs fetched. Ranked by fit to Q2 (capability boundary), Q3 (invariant boundary), Q4 (horizon/drift). Items 5, 6, 7 cut against the thesis.

## 1. Harness design for long-running application development (Anthropic engineering)

- url: https://www.anthropic.com/engineering/harness-design-long-running-apps
- type: post
- summary: Planner/generator/evaluator harness; when Opus 4.5 then 4.6 arrived, context resets, sprint decomposition and per-sprint evaluation were removed one component at a time, while the planner and a single end-of-run evaluator stayed; "every component in a harness encodes an assumption about what the model can't do on its own."
- reason: The closest primary-source, same-lab, cross-generation ablation of hand-built structure, and it also shows which parts survived (planner, selective evaluator), which is exactly the Q2 boundary.

## 2. In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks (arXiv 2604.27891, abs-verified)

- url: https://arxiv.org/abs/2604.27891
- type: paper
- summary: Putting the whole procedure in the system prompt and letting the model run its own flow beat a LangGraph controller in three domains (failure 24% vs 11.5%, 9% vs 0.5%, 17% vs 5%; judge quality 4.5-5.0 vs 4.2-4.8), with the authors arguing orchestration was only needed for earlier models.
- reason: Direct controlled evidence that external control structure became net-negative for a frontier model, but note the in-context arm is still a full script in prose, so it tests "who enforces the procedure" (code vs model) more than script vs intent; useful for the 2x2 design.

## 3. Improving Environment-Agnostic Agents: The Role of Scaffolding (arXiv 2610.22289, abs-verified)

- url: https://arxiv.org/abs/2610.22289
- type: paper
- summary: Tests whether developer-supplied procedures still help as models strengthen (Codex-based agent on ARC-AGI-3, AGI Maze, Terminal-Bench); one added instruction about reporting difficulty and returning control helped, a scripted reset controller recovered part of the gap to a task-specific reference, extra tutorial experience sometimes hurt, and the author concludes "supplied procedures still matter for the models tested."
- reason: Recent (Oct 2026), explicitly asks the Bitter Lesson question, and its mixed result (control and organization helped, tutorials hurt) is a good split of which kind of structure survives.

## 4. mini-swe-agent and the SWE-bench "bash only" leaderboard

- url: https://github.com/SWE-agent/mini-swe-agent
- type: repo
- summary: A ~100-line, bash-only, linear-history agent that the SWE-agent authors built after concluding that many of their earlier tools and special interfaces became unnecessary as LMs improved; the companion bash-only leaderboard (https://www.swebench.com/bash-only.html) holds the scaffold fixed to compare models, with the README claiming >74% on SWE-bench Verified.
- reason: The canonical minimal-harness result, from the group that built the elaborate harness first; the README does not name the model behind 74%, so pull per-model rows from the leaderboard when ingesting.

## 5. Scaffold Effects on GAIA: A Controlled Comparison (arXiv 2606.08529, abs-verified) -- CUTS AGAINST THESIS

- url: https://arxiv.org/abs/2606.08529
- type: paper
- summary: Pre-registered comparison of ReAct, planner-actor-rater and planner-then-executor scaffolds across five models and three providers; scaffold choice moved accuracy by up to 28 points within one model, and the prediction that more capable models would be less scaffold-sensitive was rejected in direction (the strongest Anthropic model gained most from structured scaffolds at Level 2, which also recovered more often from mid-trajectory errors).
- reason: The best direct counter-evidence to "scaffolds fade with capability"; the size of the effect is a single narrow cell (Opus, Level 2), and model family rather than tier looks like the moderator, so it needs careful reading before it is cited.

## 6. Harness Zero / "Are agent harnesses dying? What harness distillation changes" (Arize, reporting a Peking University study) -- PARTLY CUTS AGAINST THESIS

- url: https://arize.com/blog/agent-harness-distillation/
- type: post
- summary: Fine-tuning Qwen3.5-9B on minimally corrected runs from an evolved harness and then removing the harness gave +21 points averaged over spreadsheet, multi-app and chemistry tasks, beating the full harness; but the distilled model still trailed by 8 points on chemistry (domain knowledge, validation tool), and context management did not fully transfer.
- reason: Gives a mechanism for how structure gets absorbed (step-by-step procedures easy, domain knowledge and environment-specific context hard), which maps onto the "context asymmetry" in the research plan; secondary source, so find the original paper before ingest.

## 7. AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses (arXiv 2608.12307, abs-verified) -- CUTS AGAINST THESIS

- url: https://arxiv.org/abs/2608.12307
- type: paper
- summary: A strong builder model writes an inference-time harness for a weaker target; average accuracy on four Theory-of-Mind benchmarks rose from 0.49 to 0.91, with gains attributed to moving unstable reasoning into deterministic code, routing, and strict answer-format enforcement, and weaker targets gained most.
- reason: Supports the predicted Q2 flip (scripts and code win for weaker readers) and shows a strong model authoring structure for a weak one, which is exactly the author-bias setting in Q5; also a reminder that the 5% validation split makes overfitting a live worry.

## 8. Formal Policy Enforcement for Agentic Systems (arXiv 2602.16708, abs-verified)

- url: https://arxiv.org/abs/2602.16708
- type: paper
- summary: Runtime monitor that checks each proposed tool call against Datalog policies using event-graph history and blocks violating actions before they execute (Palumbo et al., Dillig, Jha); the abstract gives no compliance numbers or prompt-only baseline, which would have to come from the full text.
- reason: The representative "invariants belong in code, not prose" source for Q3; check the PDF for a prompt-only baseline, since that is the comparison the project needs.

## 9. Claude Code auto mode (Anthropic engineering)

- url: https://www.anthropic.com/engineering/claude-code-auto-mode
- type: post
- summary: Users approved 93% of permission prompts (approval fatigue), so Anthropic put classifiers in the approver seat; on 52 real overeager actions the full pipeline misses 17%, on 1,000 synthetic exfiltration attempts 5.7%, and the post says it is not a replacement for careful review on high-stakes infrastructure, while a fixed read-only allowlist and dropped blanket-shell rules remain deterministic.
- reason: A frontier lab's own measured number for how often a model-in-the-loop boundary fails, which is the sharpest evidence that permission and irreversible-action limits cannot be left to model judgment; also shows the model-judged middle layer is not free.

## 10. The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break (arXiv 2604.11978, abs-verified)

- url: https://arxiv.org/abs/2604.11978
- type: paper
- summary: HORIZON benchmark with 3,100+ trajectories from GPT-5 variants and Claude models across four domains, plus an LLM-judge failure-attribution pipeline (kappa 0.84 vs human) to see where agents break as horizon grows; failure categories are not in the abstract.
- reason: The best available taxonomy of long-horizon failure for Q4; it does not compare procedure styles, so it supplies the drift metrics and failure labels rather than the answer.

## 11. Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents (arXiv 2609.00006, abs-verified)

- url: https://arxiv.org/abs/2609.00006
- type: paper
- summary: Source-code study of eleven coding harnesses (Claude Code, Codex CLI, Gemini CLI, OpenHands and others) finding a shared core (LLM loop, tools, context management, safety controls, orchestration), no framework or embedding-retrieval dependence, and behavioral policy migrating from prompt text into configuration.
- reason: Shows empirically which structure practitioners keep across the field (safety controls and context management persist), and the "prompt text into configuration" trend is the same move the project hypothesizes for invariants; related taxonomy at https://arxiv.org/abs/2604.03515 (not fetched).

## 12. Agent-harness simplification, practitioner write-ups: remove-one-component-per-model-release

- url: https://www.latent.space/p/attention-interface
- type: post
- summary: Dan McAteer's Latent Space piece argues models keep absorbing harness functions and engineers keep deleting what was absorbed, with an O'Reilly Radar post (https://www.oreilly.com/radar/?p=20067) recommending that each new model release trigger switching off harness components one at a time against your evals, and secondary reports that Manus rewrote its harness five times in six months, each stripping complexity.
- reason: Gives the operational protocol (per-release ablation) that could be adapted for the project's harness; weakest tier of evidence (snippet-level, secondary, unverified claims such as "80% of the Claude Code system prompt was deleted"), so treat as hypothesis sources only.
