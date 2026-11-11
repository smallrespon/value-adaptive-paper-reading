# Changelog

All notable changes are listed here. Versions describe repository packaging and documentation, not production validation on every ChatGPT or Codex client.

## [1.4.0] - 2026-11-11

- Add a mandatory concept-clarity protocol for central D2/D3 explanations.
- Distinguish actors, reusable programs/policies, versions, invocations, actions, execution attempts, rounds, complete runs, data artifacts, states, environments, and metrics where supported by the paper.
- Require explicit inputs, operations, outputs/state effects, callers/consumers, and execution timing for central components.
- Require one consistent running example and a chronological state trace for central methods.
- Separate live execution from replay/simulation, including exactly which model, evaluator, or external calls occur or are skipped.
- Map formula symbols to concrete paper objects and distinguish solution scores from policy scores and objectives from evaluation metrics.
- When a reader says an explanation is unclear, stop advancing and rebuild the explanation instead of merely shortening or repeating it.
- Update report template, quick-start prompts, architecture notes, and package metadata.

## [Unreleased]

- Prepare the repository for community feedback and initial publication.

## [1.3.0] - 2026-11-10

- Consolidate the canonical Skill at repository root; remove duplicated skill source under mobile-plugin/skills.
- Add deterministic build of a portable, skill-only plugin ZIP from the root Skill.
- Add bilingual READMEs, contributor and security guidance, MIT license, examples, architecture documentation, release checklist, tests, and CI workflow.
- Clarify the difference between a packaged plugin and an installed/verified ChatGPT plugin.
- Preserve existing paper value assessment, mastery targets, adaptive teaching, source grounding, and optional code-reading instructions.

## [1.2.0]

- Package a skill-only mobile-plugin source layout for ChatGPT experimentation.

## [1.1.0]

- Add the code-grounded paper reading protocol and repository inventory helper.

## [1.0.0]

- Add value-adaptive deep-reading instructions, report template, and structural report validator.
