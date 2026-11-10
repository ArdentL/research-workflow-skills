# Installation and removal

The repository is a skill bundle. Install individual directories under your client's skill directory; do not copy this repository's root `AGENTS.md` into your own project.

## Bundled installer

Use Python 3.10+ from the cloned repository:

```sh
python scripts/install.py --client codex --skill paper-to-proposal --dry-run
python scripts/install.py --client codex --skill paper-to-proposal
python scripts/install.py --client claude --all
```

Targets:

- `--client codex`: `$CODEX_HOME/skills` when `CODEX_HOME` is set, otherwise `~/.codex/skills`.
- `--client claude`: `~/.claude/skills`.
- `--dest PATH`: a caller-selected skill root, useful for project-scoped or other compatible clients. It cannot be combined with `--client`.

`--skill` can be repeated. Choose either named skills or `--all`. Preview with `--dry-run`; it creates no directories. Existing targets, including symbolic links, are rejected before copying starts. There is no force-overwrite option. Select a different destination or review and remove the old copy yourself before upgrading.

The script copies each selected skill's full directory, including references, UI metadata and license. It does not install models, execute downloaded code, edit client configuration or enable an always-running process. Restart or refresh the client's skill discovery if required by your client.

## Manual installation

Copy one complete directory from `skills/` to the appropriate client skill root. Keep its name and its `SKILL.md`, `references/`, `agents/` and `LICENSE` together. Do not install the whole repository as one skill.

Invoke explicitly by skill name where supported, or ask your client to load the corresponding `SKILL.md`. Automatic discovery and invocation syntax are client features; they may differ between versions. Each skill also works as instructions loaded manually.

## Research tools and model routes

The repository does not supply PDF extraction, provider SDKs, API keys or a cross-provider runner. Before a research run, identify available tools, actual model identities, approved data routes and a hard budget. If a capability is missing, use the documented incomplete state. Do not create imaginary coverage or substitute another route without authorization.

## Removal and upgrades

Remove only the installed skill directories you selected. No account settings, papers, models or project data are installed by this package. Upgrades are explicit: inspect local customizations, archive the old copy if needed, then install the new version into a clear destination. Do not delete a shared client skill root.
