# Detailed protocol

## Intake

Use provided sources or a library connection only within the requested scope. Deduplicate by DOI/arXiv version or another canonical identifier; a different title string is not necessarily a different paper. Keep source metadata, annotations and user reading states. An unavailable library connection is not evidence that the library is empty.

Confirm the budget before calls whose cost or data sharing is not already authorized. Separate training GPU time, inference GPU time, API calls, available token usage and monetary cost. An unknown cost is not zero. Stop at a hard limit or exhausted/rate-limited route; do not silently change accounts or retry indefinitely.

## Source and reading records

Use one inventory entry per exact source version. Hash the artifact actually sent or extracted, and record any relation to the original PDF. A text extraction hash alone does not prove completeness. Page anchors should distinguish PDF page index from printed labels when necessary.

Before synthesis, inspect each reading's coverage against the obtained source:
- Are the appendix, footnotes and figure/table captions included?
- Did truncation, unreadable equations or missing image pages prevent a full read?
- Does the claim cite a matching original passage or figure?
- Are an author's explanation and a reader's inferred explanation separated?

Keep a route's configured name and its returned/resolved identity distinct. If the provider cannot resolve an alias, model diversity remains unverified. Preserve actual outputs and transport receipts. Do not publish provider responses or papers automatically.

## Mechanism comparison

Build a row for each proposed difference: nearest method, source anchor, what is shared, what changes, alternative explanation, missing control, and test that separates them. Extra agents, a new trigger, a renamed component or a different dataset may leave the underlying mechanism unchanged. Decide from the actual mechanism, not terminology.

Missing evidence should narrow a claim or become a test. Preserve specific contradictions and negative results. Do not turn every paper into a new research direction to fill a template.

## Proposal and minimum experiment

Freeze the sample unit, comparison, metric and budget before execution. Include the simplest competitive replacement and resource-matched control when claiming benefits from cooperation, memory, search or added inference. Specify whether measured cost includes all model calls and retries.

A plan may be useful before all stages are complete. Label it as a draft with missing evidence rather than pretending it is accepted. A pilot's thresholds are design choices with a stated rationale, not observations or guarantees.

## Review packet

Create a separate packet containing:
- the current proposal;
- original papers or faithful page-anchored representations, with image pages when needed;
- a neutral task covering feasibility, overlap, related work in scope and failure points;
- necessary access/tool instructions.

Exclude reading notes, conversation history, previous reviews, hoped-for verdicts and role labels that communicate which option the investigator prefers. If the proposal itself contains a recommendation, the reviewer still receives it as the object under review, not as a verdict to endorse.

Ask the reviewer to distinguish source-supported findings from speculation or out-of-packet knowledge. Preserve the returned text unchanged. The investigator verifies citations and responds separately. A new context reduces history contamination; it does not guarantee independence from shared model biases.

## Deliverable naming

Reuse the project layout. A minimal standalone run can contain:
- source-inventory.md;
- readings/reader-a.md and reader-b.md;
- receipts.json;
- evidence.md;
- proposal-v1.md;
- review/original.md and response.md;
- proposal-v2.md;
- status.md.

These names are examples, not mandatory migrations. Retain old versions. Never package real private run records into a public release without explicit authorization.
