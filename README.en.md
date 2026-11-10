# Research Workflow Skills

[中文](README.md) · [Installation](docs/installation.md) · [Worked example](examples/paper-to-proposal/README.md) · [MIT](LICENSE)

**AI agent skills for full-text paper reading, research proposals, independent review, and evidence-based research decisions.**

Designed for Codex, Claude Code and compatible skill-aware agents. These workflows turn source papers into a traceable proposal and concentrate review on consequential scientific choices. Install either skill or both; no full research workbench is required.

| Skill | Use it for | Output |
| --- | --- | --- |
| [paper-to-proposal](skills/paper-to-proposal/SKILL.md) | Full-text reading, nearest-neighbor mechanism comparison, falsifiable proposals and clean-context meta-review | Coverage matrix, model receipts, source evidence, proposal, original review and response |
| [research-decision-review](skills/research-decision-review/SKILL.md) | Novelty boundaries, major scientific claims, protocol changes, scale-up and direction choices | Decision packet, original review, factual verification and recorded disposition |

This repository supplies instructions, templates, a synthetic example and installation tools. Your client supplies PDF access, approved model routes and subagent capability. No model runner, private path or fixed vendor/model version is required.

## Install

Python 3.10+ is required. Clone with Git or download a source ZIP from Releases. Installer and repository checks use only the Python standard library.

```sh
git clone https://github.com/ArdentL/research-workflow-skills.git
cd research-workflow-skills
python scripts/validate_bundle.py
python scripts/install.py --client codex --all --dry-run
python scripts/install.py --client codex --all
```

Use `--client claude` for Claude Code, `--skill paper-to-proposal` for one skill, or `--dest PATH` for a custom skill root. Existing installations are never overwritten. The installer does not edit global instructions, change model settings or call models. See [installation and removal](docs/installation.md).

## Usage

In a Codex client that supports explicit skill invocation:

```text
Use $paper-to-proposal on the supplied papers.
Use the approved model routes and budget. Save actual reading coverage and receipts,
compare the nearest mechanisms, propose the smallest falsifiable experiment,
and obtain a fresh-context review with only the proposal and original sources.

Use $research-decision-review before scaling this experiment.
Verify existing results first, then prepare a compact decision packet.
Keep the project's reviewer, spending limit and existing authority.
```

Other compatible clients can load the matching `SKILL.md` explicitly. Both skills work independently.

## What the workflows preserve

- Full-text coverage of body, appendices, captions and obtained supplements; downloading a paper does not mean reading it.
- Actual model identities, routes, input scope, outputs and call receipts; same-model agents do not establish model diversity.
- Mechanism-level differences, alternative explanations and controls instead of novelty inferred from task names.
- Falsifiable proposals with strong baselines, simple substitutes, statistical units, cost estimates and stopping rules.
- Clean-context review, original findings, verified responses and unresolved issues.
- Distinct recommendations, review opinions, authorized decisions and observed execution.

Unavailable models or reviewers remain pending. A clearly labeled single-reader draft is allowed. Reading and review never create new authorization to train, spend, publish or delete data.

## Worked example and status

The [synthetic example](examples/paper-to-proposal/README.md) follows a deliberately weak proposal through a critical review and revision into a bounded pilot. All demo readings and reviews are labeled synthetic; none are claimed as actual model calls or experimental results.

v0.1.0 is an initial workflow release. Automated checks cover UTF-8, relative references, installation behavior and example source hashes. A fresh-context behavioral check exercised constrained user requests. These are not measurements of improved scientific output. See [validation](docs/validation.md).

## Documentation and license

[Workflow contracts](docs/workflow-contract.md) · [Provenance](PROVENANCE.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md) · [Citation metadata](CITATION.cff).

Code, skills, templates and synthetic examples are [MIT licensed](LICENSE). No third-party skill text, research PDFs, model weights, private run records or credentials are bundled.
