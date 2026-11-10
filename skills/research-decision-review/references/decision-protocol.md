# Decision protocol

## Configurable roles

| Role | Responsibility | Required output |
| --- | --- | --- |
| Investigator | Explore, implement, run authorized experiments and verify facts | Concrete recommendation, evidence, costs and reproducible artifacts |
| Optional ideation assistant | Supply candidate hypotheses, alternatives or drafts | Clearly labeled candidates whose facts remain to be checked |
| Reviewer | Challenge consequential arguments and choices | Explicit disposition, conditions, reasons and source anchors |
| Decision owner | Accept a bounded scientific choice | Recorded decision and authority scope |

A user may combine or delegate roles. Distinguish an actual independent review from an investigator reviewing their own text. No role's opinion replaces experimental evidence.

## Review-worthy changes

Examples: selecting or abandoning a main direction; fixing the core novelty boundary; promoting an observation into a primary causal or general claim; changing a protocol in ways that affect validity; committing to a substantially larger validation; finalizing a paper's main contribution or conclusion.

Routine code, source retrieval, fixed-protocol pilot execution, arithmetic checking and layout normally do not require this review. Existing project rules still apply.

## Minimum evidence packet

A packet should expose the decision trigger, alternatives, investigator recommendation, supporting and contradictory evidence, nearest-neighbor mechanism when relevant, exact metric and statistical unit, compute/call budget, stop conditions and open questions. Link to raw artifacts rather than copying an entire project or discussion.

Scientific validity and product completion are separate. A process exit, a successful model call or a completed checklist does not establish an experimental outcome.

## Usage and retry discipline

Record actual calls and known usage. Monetary cost, tokens and GPU hours are separate fields. Stop at hard limits. Authentication errors, exhausted capacity or rate limits are failures, not completed review. Do not change providers, models, accounts or data routes unless the user has already authorized that choice.

If review is pending, preserve the packet and continue independent work. Do not upgrade pending to approved because a deadline or budget is approaching.

## Reuse and correction

Record which artifact versions and assumptions a verdict covers. Changed filenames alone are not new evidence. A material mismatch in source facts, metric definitions, comparison units, compute budgets or protocol does justify correction or renewed review.

Save original review, factual verification, corrected review if any, decision and execution evidence as separate records. Never relabel an investigator's historical opinion as a reviewer's decision.
