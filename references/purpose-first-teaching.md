# Purpose-First, Causal Teaching Protocol

## Core principle

Never introduce a central component by naming its technical mechanism first and expecting a beginner to infer why it exists.

Teach the need before the name:

**overall goal → where the difficulty appears → what goes wrong or becomes expensive without help → why a new capability is needed → what this component is meant to accomplish → the technical name → how it actually works → how its output helps the next stage.**

The learner should understand why the component belongs in the system before being asked to memorize its name.

This protocol is mandatory for central D2/D3 concepts, every major algorithm component, and any term the user says they do not understand.

## 1. Start with the whole task, not the component name

Before explaining a component, answer in ordinary language:

1. What is the whole system/paper trying to accomplish?
2. What does a normal end-to-end run look like?
3. At which stage does the problem addressed by this component appear?
4. What has already happened before this component is used?
5. What needs to happen after it?

Do not begin a section with an unexplained label such as "replay mechanism", "scheduler", "critic", "memory module", or "policy network". First establish the situation in which the component becomes necessary.

## 2. Explain the problem that creates the need

Describe the difficulty as a concrete cause-and-effect story:

- What work is being done repeatedly?
- What information is missing or difficult to access?
- What operation is costly, slow, unreliable, or impossible in the previous workflow?
- What would the system have to do if this capability did not exist?
- Why is the existing component or baseline approach insufficient?

Use only problems supported by the paper. If the paper does not explicitly state the motivation, distinguish a reasonable interpretation from the authors' stated rationale.

## 3. State the component's job in plain language before giving its technical name

Use one plain sentence that a beginner can understand without knowing the jargon.

A useful teaching pattern is:

"At this point in the process, the system has already done X. But when it needs to do Y again, doing Z from scratch would cause problem P. This component is introduced to help the system accomplish Q, so that the next stage can do R."

Then introduce the paper's exact technical term and explain how the paper defines it.

Do not use the pattern mechanically when it does not fit the paper. The purpose is causal clarity, not a fixed phrase.

## 4. Explain both why it exists and how it works

These are separate questions. Answer both.

### Why it exists

- What specific problem or bottleneck motivates it?
- At what stage is it needed?
- What capability does it add to the overall workflow?
- What does it save, avoid, coordinate, preserve, expose, or make possible?
- What would become harder or different if it were absent?

### How it works

- What kind of object is it: actor, program, action, data artifact, state, environment, or metric?
- What input does it receive?
- What operation does it perform?
- What output or state change does it produce?
- Which component uses that output next?
- When and how often does it run?

Never let a purpose statement substitute for an operational explanation. "It avoids repeated work" is not enough; identify exactly which work is not repeated and what is reused.

## 5. Place every component in the end-to-end causal chain

For each major component, explain:

- **Before it:** what has happened and what problem remains?
- **At it:** what does this component receive and do?
- **After it:** what new information, result, or capability becomes available?
- **Connection:** which upstream component provides its input, and which downstream component consumes its output?

Use a compact map when useful:

| Stage | Situation/problem before the component | Component's job in plain language | Actual input and operation | Output/effect | What the next stage can now do |
|---|---|---|---|---|---|

A component is not adequately explained merely because its definition and input/output have been listed. Its role in the whole process must be clear.

## 6. Special care with mechanisms that reuse previous work (for example, replay)

Do not begin with "the replay mechanism replays historical trajectories". A beginner does not yet know why history is being replayed or what work this avoids.

If, and only if, the paper's actual replay mechanism supports this interpretation, build the explanation from the workflow:

1. An earlier exploration has already generated some data, actions, states, or results.
2. Later, the system needs to use or revisit some of that earlier exploration information.
3. Repeating the entire earlier process from scratch may waste work.
4. The paper introduces a replay-related capability to reuse or reveal previously recorded information.
5. Explain exactly what is reused: action sequence, state, transition, observation, reward, evaluation result, trajectory, or another record.
6. Explain exactly what is skipped and what still runs: model generation, environment execution, tool call, evaluation, scoring, state update, etc.
7. Explain what the replayed information changes in the current process and what the next component can do with it.

**Critical accuracy rule:** "Replay" does not automatically mean that the entire exploration is skipped or that all results are reused. Some methods replay an action sequence but still execute it; some load recorded outcomes; some reveal historical data incrementally; some recompute a score. Inspect the paper and state the exact behavior. If the paper does not specify it, say so.

The beginner-facing explanation should first communicate the motivation in ordinary language (for example, avoiding unnecessary repetition of already completed work), then introduce the technical term, then distinguish the precise implementation.

## 7. Use counterfactuals carefully

A useful explanation may say what would happen without a component, but this is often an inference.

- If the paper includes an ablation or explicitly states the baseline limitation, cite that evidence.
- If the paper does not test component removal, label the statement "进一步推断：如果移除该部件，可能会……".
- Never present an untested counterfactual as an experimental finding.
- Do not claim a component improves speed, cost, accuracy, or exploration quality unless the paper's evidence supports that claim.

## 8. A worked example must reveal the purpose, not just the mechanics

For a central D3 component, use one example to show:

1. The overall task and starting situation.
2. The problem that appears before this component is used.
3. What the system would otherwise need to do.
4. Why the component is invoked at this exact point.
5. What input it receives and what it actually does.
6. What output or state change results.
7. How the next component uses that result.
8. What is not done, not reused, or not guaranteed.

Label invented details and numbers as teaching examples, not paper results.

## 9. A reusable explanation skeleton

For each major component, adapt this sequence:

1. **先看整体任务：** 这篇论文/这个系统最终想完成什么？
2. **问题出现在哪里：** 流程走到哪一步时，原有做法遇到了什么麻烦？
3. **为什么需要新部件：** 如果没有它，系统必须重复什么、缺少什么或无法完成什么？
4. **先用白话说它的工作：** 它在整个流程里帮忙解决什么问题？
5. **再介绍论文术语：** 作者把这个部件称为什么，严格定义是什么？
6. **说明具体工作方式：** 输入、操作、输出、调用者和时机。
7. **放回整体流程：** 它接收前面什么结果，又把什么交给后面？
8. **跑一个具体例子：** 展示使用前后有什么变化。
9. **说明边界：** 它不负责什么，论文没有证明什么，哪些细节尚不明确。

Do not skip steps 1–4 for a core component. Do not force all nine steps onto minor details.

## 10. Final audit

Before delivering a central component explanation, check:

- Does the first explanation tell the reader why this component is needed before naming the mechanism?
- Is the overall task clear?
- Is the specific problem/bottleneck concrete rather than a vague phrase such as "improve efficiency"?
- Is the component's purpose connected to a stage in the full workflow?
- Have I explained what it actually does, not just what it is intended to achieve?
- Have I stated exactly what work/data is reused, skipped, recomputed, or newly generated?
- Are paper statements, teaching examples, and my inferences clearly separated?
- Could a beginner explain both "why this part exists" and "how this part works"?

If not, revise before moving on.
