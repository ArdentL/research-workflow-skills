# Original review — synthetic demonstration, not an actual reviewer call

Example packet: proposal-v1.md and source-paper.md only, plus a neutral review task.
Reader notes and earlier discussion are excluded from that example packet.

## F1 — major: mechanism overlaps with the supplied source

Source S2 already stores and reuses outputs by exact key. The proposal does not specify
a different policy. Its current test cannot attribute a benefit to a new mechanism.
Repair: include exact-key caching as a baseline, or reframe as a workload-boundary study.

## F2 — major: claim conflicts with the appendix workload

Appendix A reports 24 cached units versus 20 uncached. The general efficiency claim
is too strong. Repair: fix miss accounting and test repeated and novel keys.

## F3 — moderate: sample unit and cost accounting are unspecified

Four requests in one workload are not automatically four independent workload replications.
Repair: use independently generated sequences as paired units and record all hit/miss overhead.

Disposition: revise the question before implementation. No field-wide novelty conclusion
is possible from this single synthetic source.
