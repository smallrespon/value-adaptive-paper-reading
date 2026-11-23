# Research Paper Mentor — Value-Adaptive Paper Reading

[简体中文](./README.md) · [Examples](./examples/quick-start.md) · [Architecture](./docs/architecture.md)

**AI reads the paper; you learn from an evidence-grounded, beginner-first Chinese deep-reading report.**

This open-source Skill defaults to a reader with no research background. It separates a paper's academic value from its value to a beginner, sets observable learning targets, allocates explanation depth according to importance, and teaches essential prerequisites before introducing technical material.

## What it does

- **P0–P3 reading priority:** why a paper deserves close reading or a quick orientation.
- **M0–M4 mastery targets:** what a learner should be able to explain, derive, or apply after reading.
- **D0–D3 adaptive depth:** thorough treatment of core ideas, sufficient treatment of supporting concepts, brief treatment of peripheral details.
- **Evidence traceability:** paper sections, equations, figures, tables, and claims are distinguished from independent interpretation.
- **Beginner-first explanations:** motivations, simple examples, mathematical intuition, and step-by-step reasoning.
- **Optional paper-to-code analysis:** inspect accessible relevant source files and connect core functions to methods and formulas without executing untrusted code by default.
- **Multiple genres:** method, theory, experiment, survey, dataset, systems, and qualitative papers.

## Install as a Codex Skill

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME/.agents/skills/value-adaptive-paper-reading"
```

In Codex:

```text
$value-adaptive-paper-reading
Read this paper in full if accessible. Assess its value for a research beginner, set mastery goals, and produce a detailed Chinese teaching report with traceable evidence.
```

## Build the portable ChatGPT plugin ZIP

```bash
python scripts/build_plugin.py
# dist/research-paper-mentor-v1.5.0.zip
```

A portable skill-only plugin package does **not** automatically install itself into ChatGPT or enable web, shell, Git, PDF tools, or mobile capabilities. Installation and runtime tools depend on the hosting product, plan, and workspace. See [mobile plugin packaging](./mobile-plugin/README.md).

## Verify the project

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

These tests verify structure and packaging, not factual correctness of a generated research report.

**License:** MIT ([LICENSE](./LICENSE)). Paper contents, datasets, models, and third-party source repositories retain their own licenses. This is an independent community project, not an official OpenAI offering.
