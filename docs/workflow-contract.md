# Evidence, model and decision contracts

These contracts describe human-reviewable records, not an automated certification system.

## Evidence identity

A paper record names the source, version, actual local artifact hash and stable page/section/table anchors. Track `obtained`, `assistant_read`, and `user_read` separately; an unknown user reading state stays unknown. Note both PDF page index and printed page labels if they differ.

Keep reported observations separate from interpretations and proposed tests. A paper's unreported ablation is missing evidence, not proof that a component is useless. A proposal's performance target is a planned criterion, not an observed result.

## Model receipts

Record provider, requested model, returned/resolved model when available, endpoint route identifier without secrets, timestamp, input artifact/hash and scope, output artifact, coverage, usage and status. A provider response ID or local execution log anchors an actual call. Unknown usage remains unknown rather than zero.

Two agent names or two calls to the same actual model do not establish model diversity. Different aliases routed to the same model do not qualify. When a gateway cannot resolve identities, record diversity as unverified. A successful request, truncated output or self-report of reading does not establish full coverage.

Allowed statuses: `planned`, `completed`, `partial`, `failed`, `blocked`, and `synthetic-demo`. Only an actual successful reading with documented coverage counts as completed. Synthetic examples never count as completed real calls.

## Cost and capability

Use the user's approved model routes and hard limits. Before external calls, settle any missing authorization, data-sharing constraint or necessary budget. Track calls, available tokens, monetary cost when known, training GPU time and inference GPU time separately. Do not infer free access from installed credentials. Stop at the configured limit; do not retry indefinitely, switch accounts or silently substitute providers.

## Independent review

A fresh reviewer receives the proposal and original source artifacts, plus the task and necessary tool instructions. Exclude earlier reading notes, agent discussions, previous reviews and the desired verdict. A different agent of the same model can provide a fresh-context review, but does not count as a second model for cross-model reading. If fresh context cannot be ensured, label the review non-independent.

Keep original review, verification, responses, revised proposal and unresolved findings. Disagreement is useful information; agreement alone is not experimental evidence. A limited source packet cannot certify field-wide novelty.

## Decision authority

By default the user owns consequential decisions. A project may explicitly delegate a bounded scientific decision to a configured reviewer. That delegation never expands permission to spend, publish, delete, train or modify accounts. Routine implementation follows the existing project scope and does not require repeated scientific review.

## Portable artifact layout

Use the project's existing layout. If there is none, a run directory can contain `sources/`, `readings/`, `evidence.md`, `proposal.md`, `review/`, and `decision.md`. Do not commit real run records or licensed paper content into a public skill repository by default. The worked example in this repository is synthetic and uses only first-party text.
