#!/usr/bin/env python3
"""Copy selected skills without overwriting existing installations."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = ("paper-to-proposal", "research-decision-review")


def destination(client: str | None, explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    if client == "codex":
        return (Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills").expanduser().resolve()
    if client == "claude":
        return (Path.home() / ".claude" / "skills").resolve()
    raise ValueError("Choose --client or --dest.")


def install(names: list[str], dest: Path, *, dry_run: bool = False) -> list[Path]:
    """Preflight every selected target; never merge with an existing directory."""
    selected = list(dict.fromkeys(names))
    if not selected or any(name not in SKILL_NAMES for name in selected):
        raise ValueError("Select at least one known skill.")
    dest = dest.expanduser().resolve()
    targets = [dest / name for name in selected]
    for name, target in zip(selected, targets):
        source = ROOT / "skills" / name
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing source skill: {name}")
        if dest.is_relative_to(source.resolve()):
            raise ValueError("Destination cannot be inside a source skill.")
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if dry_run:
        return targets
    dest.mkdir(parents=True, exist_ok=True)
    for name, target in zip(selected, targets):
        shutil.copytree(ROOT / "skills" / name, target)
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--client", choices=("codex", "claude"))
    target.add_argument("--dest", help="Explicit client skill root.")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--skill", action="append", choices=SKILL_NAMES)
    selection.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        paths = install(list(SKILL_NAMES) if args.all else args.skill,
                        destination(args.client, args.dest), dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        print("No existing installation was overwritten. Check for partial new copies after an I/O failure.", file=sys.stderr)
        return 1
    verb = "Would install" if args.dry_run else "Installed"
    for path in paths:
        print(f"{verb}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
