"""Stdlib-only checks for the canonical Skill and the portable plugin package."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load_helper(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


validator = load_helper(ROOT / "scripts" / "validate_skill.py", "skill_validator")
builder = load_helper(ROOT / "scripts" / "build_plugin.py", "skill_builder")


class SkillTests(unittest.TestCase):
    def test_structure(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_plugin_bundle_matches_canonical_skill(self):
        manifest = json.loads((ROOT / "mobile-plugin" / "plugin.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            zip_path = Path(tmp) / "plugin.zip"
            builder.build_plugin(ROOT, zip_path)
            with zipfile.ZipFile(zip_path) as zf:
                names = set(zf.namelist())
                self.assertIn("plugin.json", names)
                self.assertEqual(json.loads(zf.read("plugin.json"))["version"], manifest["version"])
                self.assertIn("skills/value-adaptive-paper-reading/SKILL.md", names)
                self.assertFalse(any(n.startswith("/",) or ".." in Path(n).parts for n in names))
                for path, arcname in builder.collect_files(ROOT):
                    self.assertEqual(zf.read(arcname), path.read_bytes(), arcname)
                self.assertFalse(any("tests/" in n for n in names))

    def test_plugin_bundle_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            one = Path(tmp) / "one.zip"
            two = Path(tmp) / "two.zip"
            builder.build_plugin(ROOT, one)
            builder.build_plugin(ROOT, two)
            self.assertEqual(one.read_bytes(), two.read_bytes())


if __name__ == "__main__":
    unittest.main()
