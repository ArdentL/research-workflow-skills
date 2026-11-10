# Proposal v2 — synthetic falsifiable pilot plan

Status: planned; no measured result, actual model reading, independent review call or approval.

## Question and mechanism

Under a fixed cost model, at what repeated-key rates does an existing exact-key cache
reduce total cost? This is a boundary study of memoization, not a new agent memory method.

## Evidence and nearest alternative

SYN-CACHE-1 S2 gives a favorable repeated-key example; Appendix A gives an unfavorable
novel-key example under different miss accounting. The pilot must not mix those cost models.

## Minimal planned comparison

Use 20 independently generated length-100 key sequences at each planned repeat-rate level
0, 0.25, 0.5, 0.75 and 1. Pair cached and uncached execution on the same sequence.
These counts are illustrative pilot choices, not a power-analysis result.

Uncached: 5 units per request.
Cached: 1 lookup unit on every request; add 5 compute units on a miss.
Use an empty cache per sequence; freeze exact-key equality and deterministic outputs.

Primary metric: paired difference in total cost, cached minus uncached; lower is better.
Report per-rate differences and uncertainty across sequences. Do not treat 100 requests
within one sequence as independent replications. Compare only the predeclared workload levels.

## Resource and stop conditions

Budget: at most 100 synthetic sequence pairs, no API or GPU calls.
Stop after the declared pairs, or on any output mismatch or cost-accounting inconsistency.
The first check is whether implementation reproduces uncached cost and hit/miss accounting
under this newly fixed model. Do not claim a measured break-even rate until execution.

## Interpretation

A favorable result would describe these workloads and this cost model. A negative result
would narrow or reject the cost-saving hypothesis here. Neither result establishes a
novel memory mechanism or general agent reasoning improvement.
