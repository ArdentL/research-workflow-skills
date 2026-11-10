#!/usr/bin/env python3
"""Validate package integrity, references and synthetic-example labeling."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("paper-to-proposal", "research-decision-review")
REQUIRED = (
    "LICENSE", "README.md", "README.en.md", "PROVENANCE.md", "CONTRIBUTING.md",
    "SECURITY.md", "CHANGELOG.md", "docs/installation.md",
    "docs/workflow-contract.md", "docs/release-provenance.json",
    "examples/paper-to-proposal/README.md",
)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    for name in SKILLS:
        directory = root / "skills" / name
        path = directory / "SKILL.md"
        if not path.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Invalid UTF-8: {path.relative_to(root)}")
            continue
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"Missing frontmatter: {name}")
        else:
            header = match.group(1)
            if not re.search(rf"^name: {re.escape(name)}$", header, re.M):
                errors.append(f"Skill name mismatch: {name}")
            if not re.search(r"^description: .+\S$", header, re.M):
                errors.append(f"Missing description: {name}")
            if not re.search(r"^license: MIT$", header, re.M):
                errors.append(f"Missing MIT metadata: {name}")
        if not (directory / "LICENSE").is_file():
            errors.append(f"Missing independently installable license: {name}")
    for path in sorted(root.rglob("*")):
        if any(part in {".git", ".scratch", "__pycache__", "dist"} for part in path.relative_to(root).parts):
            continue
        if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".yml", ".yaml", ".cff"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Invalid UTF-8: {path.relative_to(root)}")
            continue
        if "\ufffd" in text:
            errors.append(f"Replacement character: {path.relative_to(root)}")
        if re.search(r"[A-Za-z]:[\\/]Users[\\/]", text, re.I):
            errors.append(f"Personal machine path: {path.relative_to(root)}")
        if path.suffix == ".md":
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                link = link.split("#", 1)[0]
                if not link or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                    continue
                resolved = (path.parent / link).resolve()
                if not resolved.is_relative_to(root) or not resolved.exists():
                    errors.append(f"Broken/outside link in {path.relative_to(root)}: {link}")
    record = root / "examples/paper-to-proposal/receipts.json"
    if not record.is_file():
        errors.append("Missing synthetic receipts")
    else:
        try:
            receipts = json.loads(record.read_text(encoding="utf-8"))
            if receipts.get("synthetic_demo") is not True:
                errors.append("Example must be marked synthetic_demo")
            if receipts.get("actual_model_calls") != 0:
                errors.append("Synthetic example must not claim actual model calls")
            readings = receipts.get("readings")
            if not isinstance(readings, list) or not readings:
                errors.append("Missing synthetic reading records")
            else:
                for reading in readings:
                    if reading.get("status") != "synthetic-demo":
                        errors.append("Example reading must have synthetic-demo status")
                    rel = reading.get("source_file", "")
                    source = (record.parent / rel).resolve()
                    if not rel or not source.is_relative_to(record.parent.resolve()) or not source.is_file():
                        errors.append("Invalid example source path")
                    elif hashlib.sha256(source.read_bytes()).hexdigest() != reading.get("input_sha256"):
                        errors.append("Example source hash mismatch")
        except (ValueError, TypeError, AttributeError):
            errors.append("Invalid synthetic receipts JSON/schema")
    provenance = root / "docs/release-provenance.json"
    if provenance.is_file():
        try:
            record = json.loads(provenance.read_text(encoding="utf-8"))
            if record["project"] != "research-workflow-skills" or set(record["included_skills"]) != set(SKILLS):
                errors.append("Project/skill provenance mismatch")
            if record["third_party_skill_text_bundled"] is not False:
                errors.append("Unexpected third-party bundle declaration")
            for source in record["workflow_sources"]:
                if source["first_party"] is not True or not re.fullmatch(r"[0-9a-f]{64}", source["source_sha256"]):
                    errors.append("Invalid workflow source provenance")
        except (ValueError, KeyError, TypeError):
            errors.append("Invalid release provenance")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("OK: 2 skills, UTF-8, links, licenses, provenance and synthetic-example integrity.")
    print("This is a packaging check, not evidence of scientific or model performance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
