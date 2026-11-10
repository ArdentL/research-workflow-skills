"""Meaningful failure checks for installation and evidence-example integrity."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load("install")
validator = load("validate_bundle")


class InstallerTests(unittest.TestCase):
    def test_dry_run_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "not-created"
            result = installer.install(["paper-to-proposal"], dest, dry_run=True)
            self.assertEqual(result, [dest / "paper-to-proposal"])
            self.assertFalse(dest.exists())

    def test_full_independent_skill_is_copied(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "skills"
            installer.install(["paper-to-proposal"], dest)
            for rel in ["SKILL.md", "LICENSE", "references/protocol.md", "references/templates.md"]:
                self.assertEqual((dest / "paper-to-proposal" / rel).read_bytes(),
                                 (ROOT / "skills/paper-to-proposal" / rel).read_bytes())

    def test_conflict_preflight_preserves_existing_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            existing = dest / "research-decision-review"
            existing.mkdir()
            marker = existing / "private-customization.md"
            marker.write_text("retain me", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install(["paper-to-proposal", "research-decision-review"], dest)
            self.assertEqual(marker.read_text(encoding="utf-8"), "retain me")
            self.assertFalse((dest / "paper-to-proposal").exists())

    def test_unsafe_name_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                installer.install(["../outside"], Path(tmp))

    def test_recursion_into_source_is_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(["paper-to-proposal"], ROOT / "skills/paper-to-proposal/nested", dry_run=True)


class BundleTests(unittest.TestCase):
    def copy_bundle(self, dest: Path):
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))

    def test_real_bundle_is_valid(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_false_completed_reading_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "bundle"
            self.copy_bundle(dest)
            receipt = dest / "examples/paper-to-proposal/receipts.json"
            receipt.write_text(receipt.read_text(encoding="utf-8").replace(
                '"status": "synthetic-demo"', '"status": "completed"', 1), encoding="utf-8")
            self.assertIn("Example reading must have synthetic-demo status", validator.validate(dest))

    def test_changed_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "bundle"
            self.copy_bundle(dest)
            paper = dest / "examples/paper-to-proposal/source-paper.md"
            paper.write_text(paper.read_text(encoding="utf-8") + "\nChanged data.\n", encoding="utf-8")
            self.assertIn("Example source hash mismatch", validator.validate(dest))


if __name__ == "__main__":
    unittest.main()
