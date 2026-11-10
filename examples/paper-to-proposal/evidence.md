# Synthetic evidence cards

## ER-SYN-01

- Source: SYN-CACHE-1 v1.0, S2.
- Reported: 20 uncached versus 8 cached units for identical deterministic keys.
- Allowed wording: exact-key caching saves cost in this constructed repeated-key example.
- Unsupported wording: cache memory generally improves agent reasoning.
- Missing: novel-key workload, matched baseline and fixed miss accounting.

## ER-SYN-02

- Source: SYN-CACHE-1 v1.0, Appendix A.
- Reported: four distinct keys cost 24 cached versus 20 uncached units.
- Inference: repeat rate and miss overhead can reverse the cost comparison.
- Contradiction: this is inconsistent with an unconditional efficiency benefit.
- Proposed check: freeze one cost model and vary repeat rate.

## Mechanism comparison

The proposed output-reuse mechanism and the source's S2 exact-key cache share lookup,
stored answer and reuse. Giving the cache an agent-oriented name does not establish
a different mechanism. A distinct routing or approximate-matching policy would need
its own specification and matched control.
