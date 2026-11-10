# Adaptive Explanation Depth

## Purpose

Allocate report space according to learning value, not paper length or mathematical appearance. The goal is a report that is deep where it matters and concise where it does not.

## Depth levels

### D3 — Full teaching treatment
Use for high-value concepts, central mechanisms, key assumptions, and core equations/proofs needed for the target mastery level.

Include as relevant:
1. why the concept/problem exists;
2. the gap in prior approaches;
3. intuitive explanation;
4. a concrete example or worked calculation;
5. formal definition or mathematical structure;
6. step-by-step reasoning or derivation;
7. the paper's exact use of it;
8. links to other components;
9. what the reader should be able to do afterward.

### D2 — Substantial explanation
Use for important supporting concepts and evidence.

Explain context, definition, operating principle, role in the paper, and important caveats. Include an example when it materially improves understanding.

### D1 — Minimum sufficient explanation
Use for prerequisites or secondary details that are needed to follow the main argument.

Give a clear definition, why it appears, and how it connects to the current section. Avoid a broad unrelated tutorial.

### D0 — Brief mention
Use for peripheral background, routine implementation details, or content outside the target mastery level.

State what it is and why it appears, then move on. Include a pointer for optional further reading if useful.

## Allocation decision

For each concept or section, assess:
- **Centrality:** Is it essential to the paper's main contribution?
- **Dependency:** Does other important content rely on it?
- **Learning leverage:** Will understanding it unlock later concepts?
- **Target mastery:** What must the reader be able to do?
- **Evidence role:** Does it support a key claim?
- **Complexity:** What explanation is needed to make it accessible?

Choose depth using judgment, not a mechanical score alone.

A concept that is mathematically difficult but peripheral may remain D0/D1. A simple idea that drives the entire method may deserve D3.

## Guardrails against over-explaining

- Teach only the prerequisite slice needed for the paper.
- Explain a concept once in depth, then refer back to it.
- Do not expand every citation into a literature review.
- Do not derive standard results unless the derivation is needed for the target.
- Do not repeat the same explanation in the background, method, and glossary.
- Put optional advanced details in callouts or appendices rather than interrupting the main learning path.

## Guardrails against under-explaining

- Never jump from a new term directly to a complex equation.
- Never say "obviously", "clearly", or "it follows" when a beginner would need the missing step.
- Explain the role of each core module and how data/reasoning flows through it.
- For each central claim, explain what evidence supports it.
- If the paper omits a necessary derivation, identify the gap rather than inventing the authors' reasoning.

## Applying D0–D3 to source code

- D3: trace a central implementation from input to output and connect it to a paper formula, with a focused example and exact function locator.
- D2: explain key function logic and parameter/data flow with paper references.
- D1: state the file/function role and the link to the method, without dumping code.
- D0: identify only the auxiliary purpose; skip routine utilities.

A long file is not inherently more important than a short loss function. Prioritize by contribution, learning leverage and target mastery.
