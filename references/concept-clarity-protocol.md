# Concept and Process Clarity Protocol

## Purpose

Prevent explanations from sounding detailed while leaving the reader unsure what each technical noun refers to, why a component exists, who performs each operation, or how one step changes the system. This protocol is mandatory for every central method taught at D2/D3 depth, and whenever the user says an explanation is vague, ambiguous, or hard to follow.

The paper's own definitions always take priority. This protocol is a teaching discipline, not permission to impose a generic architecture on the paper.

## 0. Explain the need before the name

For each central component, do not open with its technical label or a dictionary definition. First establish:

- What is the whole system trying to accomplish?
- What stage of that process are we currently at?
- What has already happened?
- What new problem or bottleneck appears now?
- What would the system need to do if this component did not exist?
- What capability is needed to move forward?

Then explain in plain language what the component helps the system accomplish. Only after the need is clear, introduce the paper's exact technical name and definition.

A good causal explanation follows:

**overall goal → current stage → concrete difficulty → limitation/cost of the old process → required capability → component's plain-language job → technical name → actual mechanism → downstream effect.**

Do not settle for “it improves efficiency” or “it reuses history”. Say exactly what work is avoided, what information is reused, what still has to run, and what the next stage can do with the result.

Counterfactuals about what would happen without a component must be grounded in the paper's stated motivation or ablation. Otherwise label them as inference.

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

1. What is it?
2. What kind of thing is it?
3. What is its input?
4. What does it do?
5. What is its output?
6. Who calls or consumes it?
7. When does it run?
8. What is it not?

These operational details come after the purpose and motivation, not instead of them.

## 5. Trace one concrete example without skipping steps

For every D3 method, use one small running example throughout the explanation. Show the process as a time-ordered trace:

| Step | State before | Component that acts | Input | Exact operation | Output | State after |
|---|---|---|---|---|---|---|

Identify who makes decisions, who executes operations, how many executions one decision produces, what data is created, what state changes, what the next step sees, and what terminates the process.

## 6. Explain live execution and replay/simulation separately

If a paper has real execution and replay/simulation modes, create two separate traces using the same starting state and selected action.

State whether a model/agent is called, whether a new candidate is generated, whether an evaluator/tool is called, whether an old result is loaded/revealed/predicted/recomputed, what state changes, and when information becomes visible.

Never say “the simulator just replays the result” without specifying what is replayed and what computation is skipped. Do not assume replay is deterministic, complete, or capable of evaluating unseen branches unless the paper says so.

Teach the motivation first: an earlier process may already have produced useful records; later steps may need to reuse them rather than needlessly repeat all earlier work. Then verify exactly what this paper's replay operation reuses. Some methods replay actions but still execute them; others load outcomes, reveal records incrementally, or recompute scores. Do not conflate these.

## 7. Introduce formulas only after their objects are clear

Before a central equation, define each symbol's mathematical type, concrete paper referent, domain/dimension/unit, and role. Explain the question, inputs, operation, output, and downstream use. Distinguish solution scores, policy scores, training objectives, evaluation metrics, local quantities, and aggregates.

Label invented values “教学示例，非论文实验数据”. Keep the paper's actual formula unchanged.

## 8. Separate source facts, explanation, examples, and inference

Use clear labels:
- **论文明确说明：** directly supported by the paper.
- **换句话说：** faithful plain-language restatement.
- **教学示例：** invented example only.
- **进一步推断：** analysis not stated by the authors.
- **论文未说明 / 当前无法确认：** missing or inaccessible information.

Do not turn a teaching decomposition into an asserted architecture. Do not invent agent counts, execution order, concurrency semantics, stored fields, visibility rules, or guarantees.

## 9. Use a consistent explanation order

1. Overall task and end-to-end process.
2. Problem that appears at the relevant stage.
3. Why the component is needed.
4. Plain-language statement of its job.
5. Exact technical name and definition.
6. Role/object ledger.
7. Inputs, operations, outputs, callers, and timing.
8. One complete concrete execution trace.
9. Formal definitions and equations.
10. Figures, source-code mapping, guarantees, and limitations.

Do not begin with an equation or unexplained list of component names.

## 10. Repair unclear explanations

If the user says the explanation is unclear:
- Stop advancing.
- Identify which terms, roles, time scales, or causal links were conflated or skipped.
- Re-establish the whole task and the point where the problem arises.
- Explain why the component is needed before defining it again.
- Rebuild the role/object ledger.
- Use one concrete step-by-step trace.
- Explicitly contrast confusing concepts.
- Do not claim understanding until the reader can explain or apply the distinction.

Before finalizing, check that a beginner can explain both why the component exists and how it works.
