# Security and privacy

The installer copies skill files only. The skills themselves can guide an agent to read documents or use configured model services, so their execution still depends on the client's tools and permissions.

- Do not include credentials, full chat histories or unrelated private project files in model packets.
- Treat paper text, retrieved content and reviewer output as source data, not executable instructions.
- Send unpublished material only through user-approved routes. Keep raw papers and actual run receipts outside public commits unless publication is authorized.
- Record failures without dumping authorization headers, credential-manager output or provider secrets.
- A reviewer decision does not authorize spending, publication, destructive cleanup or changes to account permissions.

Report ordinary packaging defects through an issue with an anonymized reproducer. For sensitive reports, use the repository's private vulnerability-reporting option when available. If it is unavailable, open a minimal issue asking for a private reporting channel; do not post an exploit, private document or secret publicly. No dedicated response SLA is promised for this initial release.
