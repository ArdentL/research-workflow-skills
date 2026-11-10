# Repository instructions

- Read and write text as UTF-8. Keep skill references relative and portable.
- Keep each skill independently installable; do not silently invoke sibling skills.
- Preserve evidence strength, negative results, user scope and cost limits.
- Examples must remain explicitly synthetic. Never invent model calls or receipts.
- Do not add credentials, private project material, model weights or research PDFs.
- Before proposing a release, run `python scripts/validate_bundle.py` and `python -m unittest discover -s tests -v`.
