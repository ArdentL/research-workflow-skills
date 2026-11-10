# Reader A — synthetic demonstration

Status: synthetic-demo. Model/provider/response ID: none; no actual call.

Source: SYN-CACHE-1 v1.0, source-paper.md. Coverage: S1–S4 and Appendix A.
No PDF pages or supplementary files exist for this source.

- S2 reports exact-key memoization: 20 uncached units and 8 cached units for four identical keys.
- Appendix A reports 24 cached units for four distinct keys, including miss bookkeeping.
- S3 has no mixed-key workload, so a general speedup claim is unsupported.
- Inference: workload repeat rate could determine whether caching pays off.
- Missing: memory/invalidation costs and any comparison against a cache-aware baseline.
