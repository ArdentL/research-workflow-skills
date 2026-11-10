# Release validation

Release: 0.1.1. Prepared: 2026-11-10.

## Packaging and installation

- Both SKILL.md files passed the system skill-format validator.
- The bundle checker verifies UTF-8, required files, relative references, per-skill MIT notices, provenance metadata and synthetic-example integrity.
- The dry-run path assertion normalizes expected Windows paths, including temporary directories represented with short names. Eight standard-library regression tests cover dry-run side effects, complete standalone copying, conflict preflight preserving existing data, invalid names, source-directory recursion, normal package validity, false completed-example status and modified source hashes.
- Local Windows checks use a writable workspace temporary root. The initial execution sandbox's default temporary directory was not writable.
- Relative-destination preview was separately checked outside filesystem virtualization and resolved correctly. No global skills or user settings were installed or modified.
- CI runs the checker and regression tests on Windows and Linux with Python 3.10 and 3.13. Inspect Actions for current remote results.

## Independent behavioral forward test

A fresh-context subagent, requested as gpt-6.1-sol, received package instructions and realistic tasks without the author's private workflow documents or prior reviews. The served backend identity was not independently resolved; this is not a cross-model reading claim.

The research tasks exercised:
1. A source-anchored proposal with only one reader and no additional model-call budget.
2. A decision packet from a five-task pilot when the configured reviewer is rate-limited and a proposed scale-up lacks authorization.

The subagent produced task outputs that labeled missing cross-model/review stages, kept the scale-up pending, and preserved descriptive pilot arithmetic without a general capability claim.

The test identified ambiguity about native unpaginated sources. The skill was revised to use section/line anchors when no PDF exists and to mark only unavailable required content as incomplete. A focused follow-up reading produced the expected status with no new instruction blocker. It did not rerun a real paper-reading campaign.

## Validation scope

These checks cover packaging and a few observed instruction-following paths. They do not demonstrate real cross-provider full-text comprehension, scientific review quality, field-wide novelty detection, experimental performance or improved long-term research outcomes.

The worked example is first-party synthetic material and records zero actual model calls. Actual user papers and private run outputs do not belong in public release archives by default.
