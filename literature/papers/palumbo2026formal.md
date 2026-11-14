---
kind: paper
title: "Formal Policy Enforcement for Agentic Systems"
authors: ["Nils Palumbo", "Sarthak Choudhary", "Jihye Choi", "Guy Amir", "Prasad Chalasani", "Isil Dillig", "Somesh Jha"]
institutions: ["University of Wisconsin–Madison", "NVIDIA", "The University of Texas at Austin", "Langroid"]
year: 2026
venue: "arXiv preprint (cs.CR), v4 2026-10-12"
peer_reviewed: false
url: "https://arxiv.org/abs/2602.16708"
code_url: "https://github.com/sasy-labs/forge"
citations: null
source: "raw/papers/palumbo2026formal.pdf"
added: "2026-11-14"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/invariants-in-code]]", "[[concepts/durable-structure]]"]
tags: [runtime-monitoring, datalog, policy-enforcement, prompt-injection, tau2-bench, agentdojo, security]
---

# Formal Policy Enforcement for Agentic Systems

## TL;DR

FORGE is a runtime reference monitor. It records an agent's messages, tool
calls and results as a causal event graph, and checks each proposed action
against a Datalog policy before it executes. Denied actions are blocked and
the agent gets structured feedback. **Yes, the full text has prompt-only
baselines**: the policy is stated in the prompt (or a prompt defense is
used) and compared with the same policy enforced at runtime. Prompt-only
agents violated the policies, sometimes in every trial. Enforcement drove
violations to zero or near zero. On τ²-Bench it *raised* task success. On
AgentDojo it cost utility.

## Claims

- Prompt-based defenses are "a best-effort heuristic that affords no formal
  guarantee". Runtime monitoring does not require the LLM to recognize
  attacks or obey a security prompt.
- Many agent policies need provenance: which messages and tool results
  causally fed an action. A per-call or linear-trace guard can't express
  that.
- Enforcement preserves or improves task success, at modest overhead
  (sub-millisecond authorization, under 7% runtime on τ²-Bench).

## Methods

- Policies are written in Datalog over an event graph and evaluated
  immediately before each action. A natural-language-to-Datalog translator
  is also provided.
- Four quantitative evaluations plus two case studies (OpenClaw, VS Code
  Copilot Chat). Arms are *instrumented* (FORGE) vs *noninstrumented*. The
  noninstrumented arm keeps the prompt-stated policy.
- Metrics: executed policy violations, task success (benchmark scorers),
  attack success rate (ASR), latency and cost. These are task-outcome and
  event-count metrics, with no LLM judge for the headline numbers. The
  τ²-Bench user is simulated by Claude Opus 4.5.

## Results (prompt-only vs enforced)

- **Information flow / exfiltration** (GPT-4.1-mini, 5 trials). The
  noninstrumented arm has an **anti-exfiltration prompt**: ASR 5/5. The
  model "complies with the injection's framing as a mandatory compliance
  audit… overriding the natural-language anti-exfiltration policy". All
  three FORGE policies: ASR 0/5. Benign utility is 5/5 in every arm.
  Runtime is 5.3 s vs 7.6–11.1 s.
- **τ²-Bench** (Claude Opus 4.5, GPT-5.2, Gemini 3.1 Pro; 50 airline + 114
  retail tasks × 4 trials per arm). **Both arms keep the benchmark's
  natural-language policy in the prompt.** FORGE adds a Datalog translation
  of it.
  - pass^1, airline: 74.7 → 81.5 (Claude 78.5 → 86.0; GPT 63.0 → 77.5;
    **Gemini 82.5 → 81.0**). Retail: 86.3 → 87.4.
  - pass^4, airline: 58.0 → 67.3 (Gemini **76.0 → 68.0**). Retail: 71.9 →
    74.6.
  - On task-model pairs where FORGE blocked something ("any denial": 33
    airline, 72 retail), pass^1 rises +31.1 (38.6 → 69.7) in airline and
    +8.3 in retail. pass^4 rises +45.5 and +18.1. "No denial" pairs move by
    ≤1.5 points, which is noise.
  - Audit of the prompt-only retail run: 32 product accesses before
    authentication, plus write-order and confirmation violations, that
    τ²-Bench's scorer does not penalize. So prompt-only compliance is worse
    than task success shows.
- **MALADE multi-agent** (GPT-4.1, 15 trials). Noninstrumented: **40
  unauthorized FDA API accesses, 0/15 trials compliant**. FORGE: 15/15
  compliant, accuracy 15/15 in both arms, cost $0.059 → $0.071. The
  highlights frame the baseline as "prompt-based instructions". The appendix
  I read doesn't quote the noninstrumented instruction text.
- **AgentDojo** (built-in GPT-4o agent, 5 sweeps × 97 benign + 949 attacked
  tasks). With the prompt-level repeat-user-prompt defense only: ASR 14.1%,
  benign utility 83.7%, utility under attack 72.5%. Adding FORGE's
  provenance policy: ASR 0.9% (0.2% by effect), utility 62.5% / 63.8%. With
  the FIDES IFC policy: ASR 0.6%, utility 33.2% / 34.4%. With no defense at
  all: ASR 25.2%.

## Critique / open questions

- **Does the comparison answer Q3?** Mostly yes for the *adversarial and
  hard-constraint* class. Where a prompt-stated rule conflicts with an
  injected instruction (exfiltration) or with the model's eagerness to get
  on with the task (unapproved API use), prose failed outright and code held.
  On τ²-Bench, enforcing rules the model already had in its prompt added 7
  points of pass^1 in airline for frontier models. That is task-outcome
  evidence that even strong models don't reliably follow long prompt
  policies.
- **The models in the starkest comparisons are not frontier.** The 5/5 and
  40-violation results use GPT-4.1-mini and GPT-4.1 with n = 5–15 trials.
  The frontier evidence is τ²-Bench (Opus 4.5, GPT-5.2, Gemini 3.1 Pro), and
  there the effect is model-dependent: Gemini airline *dropped* slightly
  under enforcement, by 1.5 on pass^1 and 8 on pass^4.
- **Cost of rigidity.** On AgentDojo, enforcement cut utility by about 9–21
  points against the prompt-only defense. The cost depends on how permissive
  the policy is (provenance vs IFC, a 29-point utility gap). Code
  enforcement isn't free, and policy design is load-bearing.
- **2×2 position.** This is orthogonal to intent vs script. It tests prose
  of either style against code for hard invariants. The prompt arm's policy
  text was benchmark-native: long, rule-dense procedure in τ²-Bench, a short
  directive elsewhere.
- **Discrepancy vs candidate summary:** the summary says the abstract gives
  no compliance numbers or prompt-only baseline. The full text has both (see
  above). The candidate list didn't flag that the τ²-Bench comparison keeps
  the NL policy in both arms, which makes it a clean "prose + code vs prose
  alone" test.

## Trust signals

- **Credibility:** 3. A strong formal-methods and security group
  (UW–Madison / Jha, UT Austin / Dillig). Code plus evaluation code and
  results are released. Task-outcome and violation-count metrics on public
  benchmarks (τ²-Bench, AgentDojo). Not peer reviewed (arXiv v4). The
  headline prompt-vs-code compliance contrasts use small n and older models.

## Follow-up

- **Relevance:** 4. This is the representative Q3 source: prompt-stated
  policy vs runtime enforcement with numbers, including frontier models on
  τ²-Bench.
- **Guide:** P3 supports. Prompt-stated hard constraints were violated in
  every trial under injection (5/5) and in every MALADE trial (40
  violations). Enforcement brought both to zero, and lifted frontier-model
  τ²-Bench airline pass^1 from 74.7 to 81.5 with the same policy still in
  the prompt. The caveats for the guide: enforcement can cost utility
  (AgentDojo −9 to −21) and was slightly negative for one frontier model.
- Check v5 or a venue version for a frontier-model rerun of the exfiltration
  and MALADE cases.
