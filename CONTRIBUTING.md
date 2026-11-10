# Contributing

Use an issue or pull request at https://github.com/ArdentL/research-workflow-skills to describe the concrete request, current behavior and proposed change. A small anonymized example is more useful than a broad request to make a skill stricter.

- Keep instructions portable, concise and independently installable.
- Put detailed procedures and templates in each skill's `references/` directory.
- Preserve the user's language, evidence strength, budget and authority boundaries.
- Label synthetic examples and distinguish planned, attempted, failed and completed model calls.
- Do not contribute private papers, unpublished results, credentials or copied third-party content without compatible permission and attribution.
- If you change observable workflow behavior, include a realistic scenario and its expected outcome. Packaging tests alone do not validate research decisions.

Run before submitting:

```sh
python scripts/validate_bundle.py
python -m unittest discover -s tests -v
```

Python 3.10+ and the standard library are sufficient. New runtime dependencies should have a concrete need. Contributions are provided under the repository's MIT license; retain existing copyright notices.
