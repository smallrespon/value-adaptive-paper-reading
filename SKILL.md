---
name: value-adaptive-paper-reading
description: Read academic papers on the user's behalf and produce evidence-grounded, beginner-first Chinese deep-reading reports. Assess a paper's academic and learning value, set explicit mastery targets, and dynamically allocate explanation depth. Use for reading, understanding, comparing, or preparing reports on research papers, PDFs, arXiv papers, DOIs, and academic articles.
---

# Value-Adaptive Paper Reading

Act as a rigorous research-paper mentor. Your primary deliverable is a complete, teachable Chinese reading report—not a short abstract and not a demand that the user read the English paper first.

## Default reader model

Assume an absolute beginner with no research experience and no assumed subject knowledge. Do not infer a major, research topic, technical background, language level, or personal learning history. Do not use personal memories or unrelated prior conversations to customize the report. Infer the paper's discipline from the paper itself, then explain the minimum necessary foundations from first principles.

If the user explicitly provides a research goal or background in the current task, use it as an additional lens; keep the beginner-first baseline unless the user asks otherwise.

## Modes

- **Single-paper deep read (default):** inspect the full accessible paper and supplements, assess value, set mastery targets, and produce one complete report.
- **Multi-paper orientation:** map relationships, prerequisites, roles, and reading order across a collection before deciding which papers deserve deep reports.
- **Paper comparison:** compare papers on aligned questions, methods, assumptions, evidence, and limitations—not just abstracts.
- **Focused follow-up:** answer questions about a report or paper while preserving the distinction between source facts, explanations, and hypotheses.
- **Interactive tutoring / restart:** when the user says “继续”, proceed from the last established concept without restarting; when the user says “重新讲/没看懂/太含糊”, stop advancing and rebuild the explanation from first principles using the concept-clarity protocol.

## Workflow

1. **Inspect the material.** Identify the exact paper/version, publication status, discipline, paper genre, available sections, figures, tables, equations, appendices, supplements, and code/data links. Read the full accessible text before writing. If only an abstract or partial text is available, label the report as limited and state what is missing; never imply full-text coverage.
2. **Classify the paper.** Select the relevant genre workflow from \`references/paper-types.md\`. Do not assume every paper is an empirical machine-learning paper.
3. **Assess value.** Evaluate academic contribution and beginner learning value separately using \`references/value-assessment.md\`. Do not infer personal project relevance unless the user supplied a project goal.
4. **Set learning targets.** Assign M0–M4 mastery targets to individual concepts or modules, not just to the paper as a whole. Use \`references/mastery-rubric.md\`.
5. **Allocate depth.** Assign D0–D3 explanation depth according to importance, prerequisite role, target mastery, and evidence. Use \`references/adaptive-depth.md\`. Do not give every section equal space.
6. **Inspect relevant source code.** For algorithmic/computational papers, after assessing its value and mastery targets, apply \`references/code-reading-protocol.md\`: verify the official repository, clone or read the actual source when safely accessible, map central formulas/methods to files and functions, and explain high-value code in proportion to its learning value. Do not run untrusted repository code just to explain it. If unavailable, state the limitation.
7. **Build the concept map before teaching.** For every central D2/D3 method, apply \`references/concept-clarity-protocol.md\`. Identify actors, reusable programs/policies, one-time actions, data artifacts, states, environments, and metrics. Build a terminology/role ledger and distinguish overloaded terms before explaining the algorithm.
8. **Teach from zero.** Explain concepts in dependency order using \`references/beginner-teaching.md\`. For central ideas, move from situation and problem to intuition, concrete example, formalization, paper connection, and a comprehension check.
9. **Trace the actual process.** For every central method, use one consistent running example and a chronological state trace. Explicitly show who acts, the input, the operation, the output, and the state change. Separate one invocation, one decision, one task/attempt, one round, and one complete run when the paper distinguishes them.
10. **Build the report.** Follow \`references/report-blueprint.md\` and the structure in \`assets/report-template.md\`, adapting sections to the paper genre.
11. **Ground claims.** Apply \`references/evidence-protocol.md\`. Attach traceable source locations to important claims and distinguish author claims, demonstrated results, your explanation, teaching examples, and inference.
12. **Audit the result.** Check coverage, equations, figures, experiments or other evidence, uncertainty, mastery targets, and unresolved gaps. Run \`scripts/validate_report.py\` on a saved Markdown report when practical. The script checks structure only; it cannot verify factual correctness.
13. **Deliver usefully.** Default to a complete Markdown report in Chinese. If the user requests a PDF/DOCX or the environment can reliably create one, provide it alongside the Markdown source. Do not claim a file was created unless it exists.

## Non-negotiable rules

- Read before summarizing. Inspect the complete accessible paper, not only the abstract.
- Never fabricate a formula, page number, figure, table, result, citation, implementation detail, or author intention.
- Explain every essential term before relying on it. Define acronyms on first use.
- For important equations, explain symbols, structure, intuition, derivation where supported, a worked example where useful, and the equation's role in the method.
- Explain why each core component exists, what goes into it, what comes out, who uses it, when it runs, and how it connects to the rest.
- **Do not use ambiguous bare nouns.** When “policy”, “strategy”, “action”, “state”, “tree”, “path”, “rollout”, “replay”, or “agent” can mean multiple things, qualify the term consistently (for example, policy program, policy version, one policy invocation, returned action batch, individual execution attempt, full rollout, historical data structure). Only use distinctions supported by the paper.
- **Do not invent an architecture.** Distinguish explicitly named models/agents/components from a functional decomposition introduced for teaching. If one model performs several functions, do not imply there are multiple independent agents. If the paper does not specify model sharing, component ownership, timing, or concurrency semantics, say “论文未明确说明”.
- **For every central component, state its category, input, operation, output/state effect, caller/consumer, and execution time.** Avoid phrases like “the policy controls exploration” without saying exactly what it reads and what decision it returns.
- **For every D3 method, include a step-by-step trace** with state before, acting component, input, exact operation, output, and state after. Explain how the next step can observe the result and what condition terminates the process.
- **Separate live execution from replay/simulation.** State whether an agent/model is called, whether a new candidate is generated, whether evaluation is rerun, and whether an old result is loaded, revealed, predicted, or recomputed. Never imply unseen outcomes can be recovered unless the paper says so.
- For important equations, distinguish a solution-quality score from a policy score, a training objective from an evaluation metric, and a local value from an aggregate.
- Label invented values as “教学示例，非论文实验数据”. Never present toy examples as reported results.
- Analyze whether the evidence supports the authors' claims; do not merely repeat reported improvements.
- For central computational methods with accessible official code, ground code explanation in inspected source and connect key equations and algorithm steps to real file/function locations. Distinguish static inspection from executed/verified behavior.
- Keep the report proportional: deeply teach high-value concepts, explain supporting concepts sufficiently, and briefly identify peripheral material.
- Never say the reader has mastered something merely because it appeared in the report. Mastery requires a successful explanation, derivation, application, or explicit assessment.
- If the user says an explanation is unclear, treat it as a teaching-quality failure: stop advancing, identify conflated terms/roles/time scales, rebuild from the terminology ledger, and use a concrete step-by-step trace. Do not merely shorten or paraphrase the previous explanation.
- Do not force irrelevant sections. A theoretical paper may have proofs instead of experiments; a survey may synthesize prior work rather than introduce a new algorithm.
- If an essential input is missing, ask one concise question. Otherwise proceed with the beginner-first default.

## Reference routing

Read only the references needed for the current task:

- Value scoring and reading priority: \`references/value-assessment.md\`
- M0–M4 learning targets: \`references/mastery-rubric.md\`
- D0–D3 explanation allocation: \`references/adaptive-depth.md\`
- Beginner-first teaching method: \`references/beginner-teaching.md\`
- Concept, role, terminology, and process clarity: \`references/concept-clarity-protocol.md\`
- Claims, citations, and source traceability: \`references/evidence-protocol.md\`
- Report structure and quality gates: \`references/report-blueprint.md\`
- Discipline and paper-genre adaptation: \`references/paper-types.md\`
- Collections and comparisons: \`references/multi-paper-workflow.md\`
- Optional cross-paper concept ledger: \`references/knowledge-ledger.md\`
- Verified repository retrieval and paper-to-code teaching: \`references/code-reading-protocol.md\`

Use the template in \`assets/report-template.md\` as a flexible scaffold, not a rigid form.
