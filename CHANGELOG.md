# Changelog

All notable changes are listed here. Versions describe repository packaging and documentation, not production validation on every ChatGPT or Codex client.

## [1.5.0] - 2026-11-11

- Add a mandatory purpose-first, causal teaching protocol.
- Require the overall task, workflow stage, concrete problem, limitation of the previous process, and need for a capability to be explained before naming a central component.
- Require separate explanations of why a component exists and how it works.
- Require components to be connected to upstream and downstream stages so the reader sees what becomes possible after their output.
- Strengthen replay teaching: explain the need to reuse previous work first, then inspect exactly what is reused, skipped, executed, or recomputed.
- Distinguish evidence-backed motivation from counterfactual inference; do not claim unverified performance benefits.
- Update beginner teaching rules, concept clarity protocol, report blueprint/template, quick-start prompts, validator, and plugin metadata.

## [1.4.0] - 2026-11-11

- Add concept-clarity protocol for central D2/D3 explanations.
- Distinguish actors, reusable programs/policies, versions, invocations, actions, execution attempts, rounds, complete runs, data artifacts, states, environments, and metrics where supported by the paper.
- Require explicit inputs, operations, outputs/state effects, callers/consumers, and execution timing.
- Require a consistent running example and chronological state trace.
- Separate live execution from replay/simulation.
- Map formula symbols to concrete paper objects.
- Rebuild unclear explanations rather than merely shortening or repeating them.

## [1.3.0] - 2026-11-10

- Consolidate the canonical Skill at repository root and add deterministic portable plugin packaging.
- Add bilingual READMEs, contribution/security guidance, MIT license, examples, architecture documentation, tests, and CI.
- Clarify that a plugin package is not an installed or verified plugin.

## [1.2.0]

- Package a skill-only mobile-plugin source layout.

## [1.1.0]

- Add code-grounded paper reading protocol and repository inventory helper.

## [1.0.0]

- Add value-adaptive deep-reading instructions and report template.
