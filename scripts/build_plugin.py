#!/usr/bin/env python3
"""Build a portable, skill-only plugin ZIP from the canonical root Skill.

No network calls or third-party dependencies. It does not install the plugin.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import zipfile

SKILL_NAME = "value-adaptive-paper-reading"
INCLUDED_ROOT_FILES = ("SKILL.md", "agents/openai.yaml", "assets/report-template.md")
INCLUDED_DIRS = ("references",)
INCLUDED_HELPERS = ("scripts/repo_inventory.py", "scripts/validate_report.py")


def collect_files(root: Path) -> list[tuple[Path, str]]:
    result = []
    for item in INCLUDED_ROOT_FILES + INCLUDED_HELPERS:
        p = root / item
        if not p.is_file():
            raise FileNotFoundError(f"Required Skill file missing: {p}")
        result.append((p, f"skills/{SKILL_NAME}/{item}"))
    for directory in INCLUDED_DIRS:
        base = root / directory
        if not base.is_dir():
            raise FileNotFoundError(f"Required Skill directory missing: {base}")
        for p in sorted(base.rglob("*")):
            if p.is_file() and not p.is_symlink():
                result.append((p, f"skills/{SKILL_NAME}/{p.relative_to(root).as_posix()}"))
    return result


def build_plugin(root: Path, output: Path) -> Path:
    manifest_path = root / "mobile-plugin" / "plugin.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Plugin manifest not found: {manifest_path}")
    manifest_bytes = manifest_path.read_bytes()
    version = json.loads(manifest_bytes)["version"]
    if not version:
        raise ValueError("Plugin manifest has no version")
    entries = [(manifest_bytes, "plugin.json")]
    entries.extend((p.read_bytes(), arcname) for p, arcname in collect_files(root))
    names = [name for _, name in entries]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate ZIP entries")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for data, arcname in sorted(entries, key=lambda x: x[1]):
            info = zipfile.ZipInfo(arcname, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o644 & 0xFFFF) << 16
            zf.writestr(info, data)
    print(f"Built plugin {version}: {output} ({len(entries)} files)")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "mobile-plugin" / "plugin.json").read_text(encoding="utf-8"))
    target = args.output or root / "dist" / f"research-paper-mentor-v{manifest['version']}.zip"
    build_plugin(root, target)


if __name__ == "__main__":
    main()
