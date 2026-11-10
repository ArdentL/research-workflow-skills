# Proposal v1 — synthetic draft with a deliberate weakness

Status: illustrative draft, no results.

Problem: repeated requests waste compute.
Proposed mechanism: let an agent remember and reuse previous answers.
Proposed claim: this memory mechanism improves general request efficiency.
Evidence: SYN-CACHE-1 S2's 20-versus-8 example.
Planned experiment: compare memory-enabled requests against uncached requests.

Missing in this draft: exact mechanism beyond memoization, the appendix counterexample,
an exact-key cache baseline, a fixed miss cost and independent workload units.
This is intentionally incomplete so the review has a concrete failure to identify.
