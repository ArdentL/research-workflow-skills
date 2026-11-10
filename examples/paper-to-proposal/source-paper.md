# Synthetic paper: exact-key response caching

**First-party synthetic teaching material. No real experiment or external paper is represented.**
Source ID: SYN-CACHE-1. Version: 1.0. Format: Markdown, no PDF pages.

## S1. Problem

Repeated identical requests may waste compute. Consider four requests to a deterministic
function, all with the exact same key. A fresh evaluation costs 5 synthetic time units.

## S2. Method

An exact-key cache stores the output of the first evaluation. A hit costs 1 unit.
For four identical requests, the uncached cost is 4 × 5 = 20 units. Cached cost is
5 + 3 × 1 = 8 units. The synthetic example speedup is 20 / 8 = 2.5.

## S3. Comparison

The only comparison is uncached evaluation. All four keys are identical and all outputs
are deterministic. No measurement across mixed or novel keys is reported.

## S4. Limitation

This example does not report memory cost, cache invalidation or nondeterministic outputs.

## Appendix A. Counterexample workload

For four different keys, every request misses. If a miss adds 1 unit of bookkeeping,
cached cost becomes 4 × (5 + 1) = 24 units, versus 20 without caching.
No approximate-key matcher, learned policy or second method was tested.
