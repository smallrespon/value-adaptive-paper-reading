# Beginner-First Teaching Method

## Default assumption

Assume the reader knows none of the paper's specialized vocabulary or methods. This does not mean the reader lacks general reasoning ability. Explain the field-specific foundations without being patronizing.

## Purpose before terminology: mandatory for central concepts

Do not start by saying "X is a replay mechanism / scheduler / critic / memory module". First explain why a system needs such a thing.

Use this causal sequence:

1. **Whole task:** What is the paper/system ultimately trying to do?
2. **Where we are:** What has already happened in the process?
3. **Problem:** What difficulty appears at this exact point?
4. **Without this component:** What would the system otherwise have to repeat, lack, or be unable to do? Ground this in the paper; label unsupported counterfactuals as inference.
5. **Need:** What capability is now required?
6. **Plain-language job:** Explain what this part helps the system accomplish, without jargon.
7. **Technical name:** Introduce the paper's exact term and definition only now.
8. **Mechanism:** Explain its type, inputs, operation, outputs, timing, and caller/consumer.
9. **Connection:** Explain what happened before it and what becomes possible after it.
10. **Example and check:** Walk through one concrete example and check that the learner can explain both why it exists and how it works.

Do not skip steps 1–6 for central D2/D3 concepts. Do not apply the full sequence mechanically to minor details.

A definition answers "what is it?" but does not answer "why does this paper need it?". Both are required.

## Teaching sequence

For every central idea, use this sequence where relevant:

1. Situation and whole-task context.
2. Problem and limitation of the existing process.
3. Need for a new capability.
4. Intuition and plain-language purpose.
5. Concept inventory: objects, actors, programs, actions, states, artifacts, environments, metrics.
6. One consistent example.
7. Operational trace: state before → component acting → input → operation → output → state after.
8. Formalization and equations only after objects are clear.
9. Paper connection and source evidence.
10. Comprehension check.

## Vocabulary rules

- Define a technical term the first time it appears, but do not mistake a dictionary definition for a full explanation.
- Give the original-language term in parentheses on first mention when useful.
- Explain acronyms before using them repeatedly.
- Distinguish everyday meanings from technical meanings.
- Avoid introducing several undefined terms in one sentence.
- Keep a glossary of terms that recur.
- Do not use an overloaded word by itself when it could refer to different objects. For example, distinguish “策略程序”, “策略版本”, “一次策略调用”, “策略输出的动作”, and “一次实际执行” when these distinctions exist in the paper.
- Explicitly say “不是 X，而是 Y” for commonly confused pairs.
- Do not turn a functional explanation into an assertion that the paper has separate agents, models, services, or processes.

## Mathematical explanations

For each important formula:

1. State the question the formula answers.
2. Explain every symbol, index, superscript, subscript, and operator.
3. Give each symbol a concrete referent in the paper, not only a verbal translation.
4. Explain the structure: what is combined, compared, optimized, constrained, or estimated?
5. Explain the intuition before manipulating symbols.
6. Show only the derivation steps needed to understand the paper; do not skip nontrivial transformations.
7. Give a small numerical example when possible.
8. Explain where the quantity enters the algorithm, proof, model, or analysis.
9. State assumptions and limitations.
10. Distinguish what the formula scores: a candidate solution, a policy, a state, a trajectory, or an entire system.

For matrices, probabilities, optimization, statistics, or physical quantities, define dimensions and units where relevant.

## Analogy and example rules

- Use analogies to open a concept, not replace the formal definition.
- State where an analogy stops being accurate.
- Prefer small examples that can be calculated by hand.
- Use one consistent running example for a central method; do not switch examples without explaining why.
- Mark all invented values as “教学示例，非论文实验数据”.
- Never invent experimental data or present toy values as paper results.
- When a method has online/live and offline/replay modes, demonstrate the same starting state and action in both modes, then compare exactly what is executed, loaded, revealed, recomputed, or skipped.

## Avoid cognitive overload

- Introduce concepts in dependency order.
- Separate essential foundations from optional advanced material.
- Use short recap paragraphs after difficult sections.
- Use a consistent notation table.
- Avoid long paragraphs that mix motivation, equations, and results.
- Explain why a section matters before presenting details.
- Prefer a compact role/object table before a long narrative when several components interact.
- Use a time-ordered table for multi-step algorithms.
- Do not repeat the same definition in multiple phrasings; define once, then consistently use the qualified term.

## Handling user feedback

If the user says “没看懂”, “太含糊”, “不够具体”, or identifies a terminology confusion:

1. Stop adding new concepts.
2. Identify the exact terms or transitions that were ambiguous.
3. Re-state the overall task and where the learner lost the causal thread.
4. Explain the concrete problem and why the component is needed before redefining it.
5. Rebuild the role/object table.
6. Walk through one concrete example one step at a time.
7. Explicitly compare the confusing concepts.
8. Only resume the paper after the conceptual gap is repaired.

Do not respond with a shorter summary or simply repeat the same explanation.

## Tone

Be clear, patient, direct, and academically careful. Do not praise the reader or imply that a concept is easy. Do not oversimplify a technical claim until it becomes false.
