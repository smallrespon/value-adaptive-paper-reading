# Report Blueprint and Quality Standard

## Core report architecture

Use this as a flexible order. Rename, merge, or omit sections when the paper genre requires it.

1. **Reading decision card:** bibliographic identity, version, field, genre, contribution, academic/learning value, P0–P3 priority, M0–M4 targets, high-value sections, coverage limits.
2. **One-page orientation:** research question, why it matters, previous approach, gap, proposed idea, evidence, limitations.
3. **Research context and prerequisites:** explain necessary background in dependency order.
4. **Problem and contribution chain:** situation → problem → prior limitation → need → proposed response. Separate author claims from evidence.
5. **Purpose-first component map (mandatory for central multi-component methods):**
   - Explain the overall task first.
   - Locate where in the end-to-end workflow the component is needed.
   - Explain the concrete difficulty that appears at that point.
   - Explain what the old process would otherwise have to repeat, lack, or be unable to do.
   - State the component's job in plain language before giving its technical name.
   - Then provide a role/term ledger: exact term, category, definition, input, output/effect, caller, timing, and commonly confused concepts.
   - Mark teaching-only functional decompositions; do not imply separate models/processes.
6. **Core method, theory, study, or argument:** structure, inputs/outputs, roles, information flow, design rationale, examples/pseudocode/proof outline. Distinguish reusable programs, versions, invocations, actions, attempts, rounds, and full runs only when supported by the paper.
7. **Step-by-step operational trace (mandatory for D3 methods):** one consistent example; state before, acting component, input, operation, output, state after, and next-stage visibility. Include the motivation for invoking each major component, not mechanics alone.
8. **Key mathematics:** notation table maps each symbol to its concrete paper referent, mathematical type, dimension/unit, and role. Explain the problem the formula solves before deriving it.
9. **Code-grounded implementation:** official repository, exact commit, file/function map, paper/code differences, static-inspection limits.
10. **Results and evidence:** what each experiment/proof/observation tests and supports; robustness, uncertainty, ablations, alternative explanations.
11. **Figures and tables:** explain how to read key figures and which claim each supports.
12. **Critical analysis:** author limitations, evidence gaps, assumptions, failure cases, independent critique.
13. **Beginner takeaways:** reusable ideas and next learning steps.
14. **Mastery plan and self-test:** M-level targets, observable criteria, questions, answer key/rubric; mark mastery unassessed until demonstrated.
15. **Glossary and evidence index:** terms, source locations, coverage audit.

## Quality standard

A beginner should be able to:
- understand why the paper exists;
- explain why each central component is needed before defining its name;
- describe what problem appears at the component's point in the workflow;
- explain what would happen without it, with evidence/inference clearly distinguished;
- explain what the component actually does, including exact inputs, operations, outputs, callers, and timing;
- trace how its output changes what the next stage can do;
- follow a central method step by step;
- interpret key equations, figures, and evidence;
- distinguish paper facts from examples and inference;
- identify what remains unclear and what to study next.

## Length and structure

- Do not target a fixed page count.
- Allocate space according to D0–D3 depth.
- Keep the main narrative coherent; move optional detail to appendices.
- Avoid repeated explanations and generic filler.
- Preserve enough detail to support mastery targets.
- If output limits require multiple parts, split at complete section boundaries and keep a contents map.
