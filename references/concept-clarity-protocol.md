# Concept and Process Clarity Protocol

## Purpose

Prevent explanations from sounding detailed while leaving the reader unsure what each technical noun refers to, who performs each operation, or how one step changes the system. This protocol is mandatory for every central method taught at D2 or D3 depth, and whenever the user says an explanation is vague, ambiguous, or hard to follow.

The paper's own definitions always take priority. This protocol is a teaching discipline, not permission to impose a generic architecture on the paper.

## 1. Build an entity inventory before explaining the method

Identify the important things in the paper and classify each one. Use only categories that actually apply.

| Category | Question it answers | Typical examples |
|---|---|---|
| Actor / component | Who or what performs work? | model, agent, worker, evaluator, controller, user |
| Program / rule / policy | What reusable procedure determines or performs work? | policy, scheduler, search algorithm, controller code |
| Action / event | What happens on one occasion? | select a node, generate a candidate, evaluate, update |
| Data artifact | What stored object is created or consumed? | tree, graph, trajectory, dataset, replay buffer, checkpoint |
| State / snapshot | What is true or visible at a particular time? | current search state, partial tree, model state |
| Environment | Where does an action execute and receive feedback? | simulator, benchmark, real execution environment |
| Metric / objective | How is quality, cost, or success measured? | reward, loss, score, latency, hypervolume |

Do not force a paper's components into these labels if the paper uses a different structure. If a category is absent, omit it.

## 2. Create a terminology and role ledger

Before a deep explanation, create a compact table for the central concepts:

| Exact paper term | Chinese name | Category | What it means in this paper | Input | Output / effect | Who creates or uses it | Not to be confused with |
|---|---|---|---|---|---|---|---|

Rules:

- Preserve the paper's exact term and explain the paper-specific meaning; do not silently substitute a familiar meaning from another field.
- Distinguish an explicitly named component from a functional decomposition introduced only to help explain the paper.
- If one model or process performs several functions, do not describe those functions as separate agents, models, or services unless the paper establishes that they are separate.
- Label explanatory groupings as “功能视角拆分（不代表独立模型/进程）”.
- If the paper does not specify who creates an object, whether two roles share a model, or when an operation occurs, write “论文未明确说明”; do not fill the gap with a plausible guess.

## 3. Disambiguate overloaded terms every time they matter

Never rely on a bare ambiguous word such as “策略”, “动作”, “状态”, “轨迹”, “搜索”, “回放”, or “Agent” when multiple meanings are in play. Use a qualified name.

For example, only when these distinctions match the paper:

- “探索策略程序（exploration-policy implementation）”: the reusable decision procedure/code/model.
- “策略版本（policy version）”: one particular revision of that procedure.
- “一次策略调用（one policy invocation）”: one occasion on which the procedure is run.
- “一次策略决策（one policy decision）”: the decision produced by that invocation.
- “动作/动作批次（action/action batch）”: the selected operation or set of operations returned by the decision.
- “单次探索尝试（individual exploration attempt）”: one actual execution that attempts to produce or test a candidate.
- “一轮决策（decision round）”: one scheduling step; do not equate it with one worker call unless the paper does.
- “一次完整探索运行（rollout/run/episode）”: the larger process containing one or more decision rounds, if that is how the paper defines it.
- “发现树（discovery tree）”: the stored data structure; it is not the policy and not a path through the tree.
- “探索路径（exploration path）”: one ordered route through nodes; it is not the full tree.
- “历史回放环境（replay environment）”: the mechanism/environment that reuses recorded outcomes; it is not the historical tree itself.

The word “policy” is especially overloaded. When relevant, explicitly distinguish:
1. the abstract mathematical policy/function;
2. its concrete implementation (code, prompt, model, parameters, or other form);
3. a particular version of that implementation;
4. one invocation of that implementation;
5. the action or action batch it outputs.

Do not assume every paper contains all five objects. State only the distinctions supported by that paper.

## 4. Explain every central component with operational fields

For each core component, answer these questions explicitly:

1. **What is it?** Give a one-sentence definition.
2. **What kind of thing is it?** Actor, program, action, artifact, state, environment, or metric?
3. **What is its input?** Name the concrete data or state it receives.
4. **What does it do?** Describe the operation, not just its purpose.
5. **What is its output?** Name the returned value, generated artifact, score, or state change.
6. **Who calls or consumes it?** Identify the upstream and downstream components.
7. **When does it run?** Initialization, each decision round, after execution, offline update, evaluation, etc.
8. **What is it not?** Contrast it with the nearest easily confused concept.

Avoid explanations such as “the policy controls exploration” unless the next sentence says exactly what information it reads, what decision it returns, and what component executes that decision.

## 5. Trace one concrete example without skipping steps

For every D3 method, use one small running example throughout the explanation. Do not switch examples halfway through unless the change is explicitly signposted.

Show the process as a time-ordered trace:

| Step | State before | Component that acts | Input | Exact operation | Output | State after |
|---|---|---|---|---|---|---|

At minimum, identify:

- who makes the decision;
- who executes the selected operation;
- whether one decision produces one or several executions;
- what new data/artifact is created;
- how the system state changes;
- what information becomes visible to the next decision;
- what condition ends the process.

For parallel systems, distinguish a decision batch, individual tasks, workers, and completed attempts. A batch of three tasks is not automatically one attempt.

For iterative systems, distinguish a single step/round from the complete run/episode. Explain the termination condition.

For tree or graph methods, show the parent, child, edge, root, leaf/frontier, and legal-choice set only where the paper defines them. Explain whether the structure represents all historical data or only the currently visible/active portion.

## 6. Explain live execution and replay/simulation separately

If a paper has real execution and replay/simulation modes, create two separate traces using the same starting state and selected action.

For each mode, state explicitly:

- whether a model/agent is called;
- whether a new candidate is generated;
- whether an evaluator or external tool is called;
- whether an old result is loaded, revealed, predicted, or recomputed;
- what is appended to or changed in the current state;
- whether the full historical data is visible at once or revealed incrementally.

Never say “the simulator just replays the result” without specifying what is replayed and what computation is skipped. Do not assume replay is deterministic, complete, or capable of evaluating unseen branches unless the paper says so.

## 7. Introduce formulas only after their objects are clear

Before presenting a central equation, define every symbol in a notation table:

| Symbol | Mathematical type | Concrete object in the paper | Domain / dimension / unit | Role in the equation |
|---|---|---|---|---|

Then explain:

1. what question the equation answers;
2. what its inputs are;
3. what operation is performed;
4. what output it produces;
5. how that output is used by the algorithm or argument.

Distinguish a score for a candidate solution from a score for a policy, a training objective from an evaluation metric, and a local quantity from an average over tasks or histories. Do not use the same informal label for different quantities.

For a worked numerical example, label all invented numbers as “教学示例，非论文实验数据”. Keep the paper's actual formula unchanged; do not silently simplify or replace it with a more familiar formula.

## 8. Separate source facts, explanation, examples, and inference

Use clear labels where confusion is possible:

- **论文明确说明：** directly supported by the paper.
- **换句话说：** a faithful plain-language restatement.
- **教学示例：** invented example used only to explain the mechanism.
- **进一步推断：** analysis that follows from the paper but is not stated as an author claim.
- **论文未说明 / 当前无法确认：** missing or inaccessible information.

Do not turn a teaching decomposition into an asserted architecture. Do not invent agent counts, execution order, concurrency semantics, stored fields, visibility rules, or guarantees.

## 9. Use a consistent explanation order

For a central method, prefer this sequence:

1. One-sentence goal.
2. System map: actors, programs, data structures, environment, metrics.
3. Terminology/role ledger.
4. Inputs and outputs of each central component.
5. One complete concrete execution trace.
6. The paper's actual algorithm and formal definitions.
7. Important equations and hand calculation.
8. Mapping to figures and source code, if available.
9. What the method guarantees and what it does not guarantee.

Do not begin with an equation or a list of unexplained component names.

## 10. Repair unclear explanations when the reader gives feedback

If the user says the explanation is unclear, too vague, or mixes concepts:

- Treat that as a teaching-quality failure, not as a request for a shorter paraphrase.
- Stop advancing to new material.
- Identify which nouns, roles, time scales, or data-flow transitions were conflated.
- Rebuild the explanation from the terminology/role ledger.
- Use one concrete running example and a step-by-step state trace.
- Explicitly contrast the confusing pairs.
- Do not claim the reader understands until they can explain or apply the distinction.

Before finalizing any D2/D3 explanation, audit it with these questions:

- Is every central noun a clearly identified object?
- Is every action assigned to a specific actor/component?
- Are inputs and outputs named?
- Are one-time events distinguished from reusable programs and repeated processes?
- Are artifacts distinguished from paths through those artifacts?
- Are current/visible state and complete historical data distinguished?
- Are paper facts separated from teaching examples and inference?
- Could a beginner answer “who does what, to which input, producing what output, at what time” for every major step?

If any answer is no, revise before delivering.
