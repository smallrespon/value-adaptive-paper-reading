#!/usr/bin/env python3
"""Validate the Skill package's metadata, local reference paths, and syntax.

Does not assess factual correctness, output quality, or runtime compatibility.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys

REQUIRED_REFS = (
    "references/value-assessment.md",
    "references/mastery-rubric.md",
    "references/adaptive-depth.md",
    "references/beginner-teaching.md",
    "references/evidence-protocol.md",
    "references/report-blueprint.md",
    "references/paper-types.md",
    "references/multi-paper-workflow.md",
    "references/knowledge-ledger.md",
    "references/code-reading-protocol.md",
    "assets/report-template.md",
)
EXPECTED_SKILL = "value-adaptive-paper-reading"
EXPECTED_PLUGIN = "research-paper-mentor"


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    p = root / "SKILL.md"
    if not p.is_file():
        return ["Missing SKILL.md"]
    content = p.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append("SKILL.md is missing YAML frontmatter")
    else:
        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append("Malformed SKILL.md frontmatter")
        else:
            frontmatter = parts[1]
            name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
            descr_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
            if not name_match or name_match.group(1).strip() != EXPECTED_SKILL:
                errors.append("Unexpected Skill name")
            if not descr_match or not descr_match.group(1).strip():
                errors.append("Empty Skill description")
    for ref in REQUIRED_REFS:
        if not (root / ref).is_file():
            errors.append(f"Missing referenced Skill resource: {ref}")
        if ref not in content:
            errors.append(f"SKILL.md does not reference {ref}")
    agent = root / "agents" / "openai.yaml"
    if not agent.is_file() or "display_name:" not in agent.read_text(encoding="utf-8"):
        errors.append("Missing / invalid agents/openai.yaml")
    plugin_path = root / "mobile-plugin" / "plugin.json"
    try:
        manifest = json.loads(plugin_path.read_text(encoding="utf-8"))
        for key in ("$schema", "name", "version", "description"):
            if not manifest.get(key):
                errors.append(f"Plugin manifest missing {key}")
        if manifest.get("name") != EXPECTED_PLUGIN:
            errors.append("Unexpected plugin name")
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot parse plugin.json: {exc}")
    for py in sorted((root / "scripts").glob("*.py")):
        try:
            ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
        except SyntaxError as exc:
            errors.append(f"Syntax error in {py.name}: {exc}")
    if (root / "mobile-plugin" / "skills").exists():
        errors.append("Duplicated Skill source under mobile-plugin/skills")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    print("PASS: Skill structure, refs, manifest and helper script syntax")
    print("NOTE: This is not a factual paper-reading or plugin install test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
