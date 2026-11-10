# Research Paper Mentor — Mobile Plugin

This directory contains a portable, **skill-only** plugin package for ChatGPT. It contains no local MCP server so it does not depend on a computer running a local tool.

Install via ChatGPT **Plugin Creator**: point it at this directory or upload the downloadable plugin ZIP, and ask it to create a private personal plugin for mobile usage.

The canonical Codex skill remains at the GitHub repository root. The bundled skill under `skills/value-adaptive-paper-reading/` is a package snapshot; keep it in sync when updating the root skill.

**Limitations:** The skill does not independently provide Git cloning, shell execution, PDF parsing or access to private GitHub repositories. Those need capabilities in the runtime or authorized app connections. An installed personal plugin is not automatically synced from GitHub without a supported sync arrangement.
