---
kind: paper
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
authors: ["Thibaud Gloaguen", "Niels Mündler-Sasahara", "Mark Niklas Müller", "Veselin Raychev", "Martin Vechev"]
institutions: ["ETH Zurich", "LogicStar.ai"]
year: 2026
venue: "arXiv preprint (v3, 2026-09-29)"
peer_reviewed: false
url: "https://arxiv.org/abs/2602.11988"
code_url: null
citations: null
source: "raw/papers/gloaguen2026evaluating.pdf"
added: "2026-11-14"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: ["[[concepts/llm-authored-instructions]]", "[[concepts/context-engineering]]", "[[concepts/guidance-distraction]]"]
tags: [agents-md, context-files, coding-agents, swe-bench, cost]
---

# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

## TL;DR

Across 4 coding agents on SWE-bench Lite and a new 138-task benchmark from repos
that ship developer-written context files, neither LLM-generated nor
developer-written AGENTS.md/CLAUDE.md files significantly changed task success.
Both raised cost by about 20%. Agents follow the files' instructions, which means
more testing and exploration, but the repository overviews don't help them find
the relevant files faster.

## Claims

- Context files "do not generally improve task success rates" and raise inference
  cost by over 20%. This holds across LLMs, agents, and both file origins.
- Developer-written files beat LLM-generated ones by about 7% on average. Our
  arithmetic says this is relative: +4.2 pp absolute, p = 0.038.
- Instructions in context files are followed. For example, `uv` is used 1.6×
  per instance when the file mentions it vs <0.01× when it doesn't. So the null
  result is not an instruction-following failure.
- Repository overviews don't work as navigation aids.
- LLM-generated files mostly repeat existing documentation. With docs removed,
  they help.
- Recommendation: omit LLM-generated context files for now. Human-written ones
  should hold only what isn't already in the README (non-standard conventions,
  non-functional requirements).

## Methods

- **Agents/models:** Claude Code + Sonnet-4.5, Codex + GPT-5.2, Codex + GPT-5.1
  mini, Qwen Code + Qwen3-30B-Coder. Temperature 0 (0.7 for Qwen). **One sample
  per agent per instance.**
- **Benchmarks:**
  - SWE-bench Lite: 300 tasks, 11 repos, no developer context files.
  - CTXbench (new): 138 tasks, 12 niche Python repos that each commit a context
    file. Task descriptions and tests were LLM-generated (GPT-5.2 + Codex), then
    manually reviewed. 25 of 138 tests were hand-edited for over-specification.
- **Conditions:** None / LLM (generated with each agent's own recommended init
  command and model on the pre-patch repo) / Dev (the repo's committed file;
  CTXbench only).
- **Metric:** resolution rate, where all tests pass. This is a task outcome, not
  an LLM judge. Steps and USD cost are also reported.
- **Statistics:** Cochran–Mantel–Haenszel tests for success and stratified
  permutation tests for cost and steps.
- **Trace analysis:** GPT-OSS-120B classified tool-call intents. This is
  behavioural description only, not the outcome metric.
- **Ablations:**
  - generator model (strong model's file used by a weak model)
  - generation prompt (Codex vs Claude Code init prompt)
  - file length
  - removing the Overview, Tooling, or Testing category (GPT-5.4 edits, rerun on
    GPT-5.2)
  - documentation-stripped repos
  - contamination split by knowledge cutoff

## Results

Success rates (%) from Table 5 (± ~3–4 SE):

| Model | SWE None | SWE LLM | CTX None | CTX LLM | CTX Dev |
|---|---|---|---|---|---|
| Sonnet-4.5 | 59.9 | 58.7 | 73.2 | 65.2 | 70.3 |
| GPT-5.2 | 56.6 | 54.4 | 65.2 | 68.1 | 68.1 |
| GPT-5.1 mini | 47.7 | 47.6 | 54.3 | 50.7 | 55.8 |
| Qwen3-30B | 31.1 | 32.4 | 45.7 | 47.1 | 53.6 |

- **LLM vs None:**
  - −0.5 pp on SWE-bench (p = 0.87) and −1.8 pp on CTXbench (p = 0.37).
  - Drops in 5 of 8 settings.
  - Largest single drop: Sonnet-4.5 / Claude Code on CTXbench, −8.0 pp.
- **Dev vs None:** +2.4 pp (p = 0.21, n.s.). Dev helped every agent except
  Claude Code (−2.9 pp).
- **Dev vs LLM:** +4.2 pp absolute, about 7% relative (p = 0.038). This is the
  only significant success effect.
- **Cost:**
  - LLM files: +20% (SWE) and +23% (CTX), p < 0.001%.
  - Dev files: "at most 19%".
  - Steps: +2.45 / +3.92 (LLM) and +3.34 (Dev).
  - Reasoning tokens with LLM files: +22% for GPT-5.2 and +10% for 5.1 mini on
    SWE-bench.
- **Overviews:**
  - Present in 100% of Sonnet-generated files, 99% of GPT-5.2, 95% of Qwen,
    36% of 5.1 mini.
  - They don't reduce the steps before first touching a gold-patch file.
- **Stronger generator ≠ better file:** GPT-5.2- or Sonnet-written files used by
  weaker agents gave +2 pp on SWE-bench but −3 pp on CTXbench.
- **Generation prompt:** effect is small and inconsistent.
- **Length:** no relationship with success or cost.
- **Category removal** (GPT-5.2):
  - No category changes accuracy significantly.
  - Removing the Testing section cuts cost (CTX $0.47 → $0.37, p = 0.023;
    SWE p = 0.0035).
- **Docs removed** (App. B; excludes Claude Code): LLM files now improve
  success by +2.7 pp on average and *beat* developer files. This points to
  redundancy with existing docs, not authorship, as the driver.
- **Contamination:** the pre/post-cutoff split shows no consistent difference.

## Critique / open questions

- **Evaluation quality is good on the outcome side.** Results come from executed
  tests with paired significance tests on the same instances, which is the kind
  of evidence this project weights. Limits:
  - one sample per condition
  - n = 138 for CTXbench, so SE ≈ 4 pp and a 4 pp effect is barely detectable
  - Python only
  - CTXbench task specs and tests are LLM-written (more on this below)
- **The LLM-written vs human-written comparison is not controlled.** The two
  files differ in content, length, and redundancy with the README.
  - Developer files are shorter and score lower on an AI detector, but that
    doesn't prove they are human-written.
  - The "human" arm is just **12 files**, one per repo, so authorship is
    confounded with repo.
  - The App. B result (LLM files win once docs are removed) suggests the
    variable that matters is *redundancy with what the reader can already find*,
    not who wrote it.
- **The candidate summary overstates the harm.** "Context files lower success"
  came from the v1 abstract ("tend to reduce task success rates"). v3 (Sep 2026)
  rewrites this as "does not generally improve … neither statistically
  significant". v3 also uses different models (GPT-5.2, Sonnet-4.5).
  - "LLM-written files hurt most": directionally true, but the harm is not
    significant vs None.
  - "Developer-written ones slightly help": +2.4 pp, n.s.
  - ">20% cost": confirmed.
- **CTXbench descriptions are LLM-standardised, detailed specs** (6 sections).
  SWE-bench with the same rewrite gained about 15 pp. A detailed task spec may
  leave little for a context file to add, so the null could be weaker with
  sparse issues.
- **Doctrine question** (research plan): the context file *is* the shared
  doctrine. A null effect with real cost says generic doctrine that repeats what
  the repo already shows is wasted. It doesn't test doctrine that carries
  non-discoverable conventions.
- **2×2 placement:** context files are mostly *verbose intent/context*
  (overviews) mixed with *terse procedure* (tooling and test commands). Style is
  not manipulated. The Testing-section ablation hints that procedural "run the
  tests like this" lines drive cost without changing success.
- **Q5 bearing (author bias):** this is indirect evidence. Frontier agents' `/init`
  produces near-universal overviews, even Claude Code, whose prompt warns
  against listing discoverable components. Those overviews don't help. Stronger
  models don't write better files.

## Trust signals

- **Credibility:** 3. A strong SE-benchmark group (ETH SRI, the SWT-Bench and
  BaxBench authors), task-outcome metrics, paired significance tests, many
  ablations. But it's a preprint with no peer review, no code or benchmark
  release linked in the paper (none found on GitHub), single runs, and the
  headline wording changed substantially between v1 and v3.
- Citations not looked up: the Semantic Scholar API was rate-limited.

## Follow-up

- **Relevance:** 5. This is the source principle 6 and research-plan Q5 rest on,
  and the only controlled task-outcome study of context files in hand.
- **Guide:** P6 refines. Rewrite the line. Context files didn't significantly
  lower success; they failed to raise it and added ~20% cost. The LLM-vs-human
  gap (+4 pp, p = 0.04) is confounded with redundancy and reverses once
  in-repo docs are removed. The defensible rule is "don't restate what the
  reader can discover; keep only non-discoverable conventions and requirements",
  not "LLM-written is bad". Evidence tag: `[moderate]` (one credible controlled
  study, not peer-reviewed).
- Watch for: a v4 or venue version, a code/benchmark release, and replication on
  non-Python repos or with sparse issue text.
