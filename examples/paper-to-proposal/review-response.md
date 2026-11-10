# Response — synthetic demonstration

- F1 accepted. v2 drops the new-memory-mechanism claim and asks when an existing exact-key cache pays off.
- F2 accepted. v2 uses one cost model across all workloads: fresh computation = 5,
  lookup bookkeeping = 1 per request, no bookkeeping for the uncached baseline.
  This is a new planned model, not a reinterpretation of S2's 8-unit observation.
- F3 accepted. Independent generated sequences, not individual requests, are paired units.
- Remaining: actual runtime measurement, memory/invalidation cost and nondeterministic outputs are outside this pilot.
- No original review text was edited, and no experiment was run.
