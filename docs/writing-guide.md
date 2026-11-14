---
kind: guide
title: Writing instructions for strong models
updated: "2026-11-14"
---

# Writing instructions for strong models

This is the live reference for claude-system skills, rules, hooks, system
prompts and subagent briefs. Every line carries an evidence tag and cites the
notes behind it. When a curated source moves a line's strength, update the
tag. When evidence contradicts a line, rewrite or delete it. Don't keep both
versions.

**Evidence tags**
- `[strong]`: passes `/elevate` Gate 1 (peer-reviewed, code released, or ≥3
  independent attestations at credibility ≥3).
- `[moderate]`: one credible controlled study, or consistent vendor guidance
  plus one study.
- `[weak]`: practitioner reports, single small studies.
- `[provisional]`: from discovery snippets, not yet ingested. Verify before
  relying on it.
- `[in-house]`: a de-identified observation from the private system audit.
  Not literature.

## Principles

1. **Brief, don't script, for procedure the reader can work out.** State the
   goal, the hard constraints and the reason for each. Leave the method to
   the reader. `[provisional]`: Anthropic and OpenAI guidance; literal demos
   hurt reasoning models while abstracted insights help (2509.23196).
2. **Coverage beats brevity.** Write down the requirements you know but
   would otherwise leave unsaid. Readers guess unstated requirements right
   only ~41% of the time, and underspecified prompts regress ~2× across
   model changes. `[provisional]`: 2505.13360.
3. **Hard invariants go in code, not prose of either style.** Use hooks,
   typed checks and permission gates. `[provisional]`: CoT lowers adherence
   to simple hard constraints (2505.11423); hub `typed-enforcement`,
   `constraint-pinning`.
4. **Keep structure that carries knowledge or enforces rules.** Scaffolding
   isn't automatically dead weight for strong models. In one pre-registered
   study, the strongest model gained the most from it. `[provisional]`:
   2606.08529, 2604.27891.
5. **Hand over context, not just a task.** The reader matches the author in
   capability, not in context. Some context must travel as full traces.
   `[provisional]`: Anthropic multi-agent post; Cognition "Don't Build
   Multi-Agents".
6. **Be suspicious of LLM-written context files.** In one evaluation they
   lowered task success and added >20% cost. `[provisional]`: 2602.11988.

## Open questions

See `research-plan.md` § Open questions.
