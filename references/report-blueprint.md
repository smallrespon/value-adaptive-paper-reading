# Report Blueprint and Quality Standard

## Core report architecture

Use this as a flexible order. Rename, merge, or omit sections when the paper genre requires it.

1. **Reading decision card**
   - bibliographic identity and version;
   - field and genre;
   - one-sentence contribution;
   - academic value and beginner learning value;
   - priority P0–P3;
   - overall and component-level mastery targets;
   - high-value sections and skimmable sections;
   - coverage limitations and confidence.

2. **One-page orientation**
   - research question;
   - why it matters;
   - previous approach and gap;
   - proposed idea or central argument;
   - main evidence or result;
   - main limitation.

3. **Research context and prerequisites**
   - field/problem context;
   - relevant history or prior approaches;
   - why the problem remains open;
   - prerequisite concepts in dependency order;
   - plain-language definitions and why each is needed.

4. **Problem and contribution chain**
   - situation → problem → prior limitation → need → proposed response;
   - contribution claims separated from verified evidence.

5. **System / concept map (mandatory for multi-component methods)**
   - distinguish actors/components, reusable programs or policies, actions/events, data artifacts, states, environments, and metrics;
   - include a terminology and role ledger with exact paper term, category, definition, input, output/effect, caller/consumer, execution time, and easily confused concepts;
   - explicitly mark functional teaching decompositions that do not imply separate models or processes;
   - state what the paper does not specify.

6. **Core method, theory, study, or argument**
   - overall structure;
   - inputs and outputs;
   - components and their roles;
   - information/reasoning flow;
   - design rationale;
   - worked example, diagram, pseudocode, or proof outline as appropriate;
   - distinguish reusable rule/program, its version, one invocation, its output action, one execution attempt, one round, and a complete run when the paper distinguishes them.

7. **Step-by-step operational trace (mandatory for D3 methods)**
   - use one consistent running example;
   - show state before, acting component, input, exact operation, output, and state after;
   - explain what the next step can observe;
   - distinguish parallel decision batches from individual tasks/attempts;
   - state the termination condition;
   - for live and replay/simulation modes, show separate traces from the same starting state and explain which model/tool/evaluator calls occur or are skipped.

8. **Key mathematics and formal details**
   - notation table mapping each symbol to its concrete paper referent, mathematical type, domain/dimension/unit, and role;
   - central equations/proofs;
   - stepwise explanations;
   - assumptions and boundary conditions;
   - worked examples where useful;
   - specify exactly what each metric/objective scores.

9. **Code-grounded implementation (when relevant)**
   - official repository and exact inspected commit;
   - central file/function map to paper sections and equations;
   - explanation depth based on concept value and M-level;
   - paper–code differences and static-inspection limitations.

10. **Results and evidence**
    - experiments, proofs, observations, qualitative evidence, dataset analysis, or literature synthesis;
    - what each result tests;
    - what it supports and does not support;
    - robustness, ablations, sensitivity, uncertainty, or alternative explanations where applicable.

11. **Figures and tables**
    - select the figures/tables that carry the argument;
    - explain how to read them;
    - connect each to a claim;
    - do not describe every decorative or redundant visual.

12. **Critical analysis and limitations**
    - author-acknowledged limitations;
    - evidence gaps;
    - assumptions;
    - potential failure cases;
    - independent critique, explicitly labeled.

13. **What a beginner should take away**
    - most reusable ideas;
    - concepts worth remembering;
    - techniques worth revisiting;
    - possible next learning steps;
    - project-specific relevance only if a project was supplied.

14. **Mastery plan and self-test**
    - concept/component → target M-level → observable success criteria;
    - short-answer questions, calculation/derivation tasks, or application prompts;
    - answer key and rubric;
    - mark mastery as unassessed until the reader demonstrates it.

15. **Glossary and evidence index**
    - recurring terminology;
    - important claims with source locations;
    - coverage and access audit.

## Quality standard

A report is successful when an absolute beginner can use it to:
- understand why the paper exists;
- follow the main problem and contribution;
- identify what each central component is, what it receives, what it does, and what it produces;
- distinguish reusable procedures from one-time decisions and executions;
- follow a central method step by step without guessing who acts or how state changes;
- understand the core method or argument at the assigned target level;
- interpret important equations, figures, and evidence;
- where code is relevant and available, trace central paper ideas to actual implementation files and functions;
- distinguish what is known from what is inferred;
- see what is worth learning deeply versus skimming;
- identify what remains unclear and what to study next.

## Length and structure

- Do not target a fixed page count.
- Allocate space according to D0–D3 depth.
- Keep the main narrative coherent; move optional detail to appendices.
- Avoid repeated explanations and generic filler.
- Preserve enough detail to support the assigned mastery targets.
- If output limits require multiple parts, split at complete section boundaries and keep a contents map.
