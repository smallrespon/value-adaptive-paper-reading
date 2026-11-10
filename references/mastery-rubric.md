# Mastery Rubric: M0–M4

## Principle

Set mastery targets for each important concept, method component, proof, experiment, or research skill. Do not assign one level to every part of a paper. The reader starts from a zero-background baseline; the report must teach prerequisites rather than assume them.

A target is a desired learning outcome, not proof that the reader already achieved it.

## Levels

### M0 — Orientation
The reader can identify:
- the topic and problem;
- the paper's main proposal, argument, or finding;
- the headline result or conclusion;
- the role the paper plays in the field.

### M1 — Conceptual explanation
The reader can explain in their own words:
- the context and motivation;
- what earlier approaches do and where they fall short;
- the central idea;
- the overall structure of the method, theory, study, or argument;
- the main contribution and its boundaries.

### M2 — Technical understanding
The reader can:
- explain the important components and how they interact;
- interpret core equations, assumptions, variables, and diagrams;
- trace the main algorithm, proof idea, experimental design, or analytical argument;
- explain why key design choices are made;
- connect the evidence to the claims it supports.

### M3 — Operational application
The reader can:
- reconstruct the central workflow or reasoning chain;
- work through a representative example or calculation;
- identify necessary implementation, data, measurement, or proof details;
- adapt the central idea to a related problem;
- outline what would be needed to reproduce or apply the work.

Do not require full reproduction if the paper omits essential details or reproduction is outside the task.

### M4 — Critical and generative understanding
The reader can:
- identify assumptions and scope conditions;
- evaluate whether evidence is sufficient;
- identify plausible failure cases and alternative explanations;
- propose a defensible extension, test, or improvement;
- formulate a research question motivated by the paper.

M4 is advanced and should not be the default expectation for a novice.

## Default targets by priority

These are starting heuristics, not rigid rules:

| Priority | Overall target | Core contribution | Peripheral details |
|---|---|---|---|
| P0 | M2, with selected M3 | M2–M3 | M0–M1 |
| P1 | M1–M2 | M2 | M0–M1 |
| P2 | M0–M1 | M1 | M0 |
| P3 | M0 | M0–M1 | Usually omit |

Adjust for paper genre. For example:
- A theory paper may need M2 on assumptions and proof structure.
- A methods paper may need M3 on the central algorithm if implementation is a stated goal.
- A survey may need M2 on the taxonomy and relationships, not M3 on every cited method.
- A dataset paper may need M2 on collection, annotation, leakage risks, and benchmark design.

## Target table

For each major component, provide:

| Component | Why it matters | Target | Observable success criterion |
|---|---|---|---|
| Core concept | ... | M1/M2/etc. | Can explain ... |
| Main equation/proof | ... | M2/M3 | Can interpret/derive ... |
| Main method | ... | M2/M3 | Can trace/reconstruct ... |
| Evidence | ... | M1/M2 | Can judge ... |
| Limitations | ... | M1/M2/M4 | Can identify ... |

## Assessment integrity

Use these distinctions:
- **Taught:** the report explained it.
- **Practiced:** the report included an example or exercise.
- **Demonstrated:** the reader successfully answered, derived, explained, or applied it.
- **Not yet assessed:** no evidence of mastery.

Never upgrade a concept to `Demonstrated` because it appeared in the report. If the user has not completed a test, say that mastery remains unverified.

## Code-related observable success criteria (when relevant)

- M0: identify whether the paper provides code and which artifact implements the main method.
- M1: explain in ordinary language what the main code modules do and how they fit together.
- M2: map the core equation or algorithm to specific functions and trace important inputs/outputs.
- M3: work through a toy call/data-flow example and identify implementation and reproducibility requirements.
- M4: identify source-vs-paper discrepancies, important design tradeoffs, and defensible modifications.

Never infer actual execution or reproduction from static source inspection.
