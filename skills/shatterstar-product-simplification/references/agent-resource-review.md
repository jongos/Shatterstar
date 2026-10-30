# Agent resource review: illustrative decisions

These invented cases calibrate recommendations; they are not executed benchmarks.

## Batch document extraction

An agent proposes copying an entire collection, loading every document into RAM and retaining all intermediate renderings. The required outcome is searchable extracted text with source traceability.

Compare reading originals in place with bounded batches and retaining only needed outputs. Check source immutability, parser isolation, restartability and whether rendering is required. Estimate peak disk including expanded files and temporary output, and peak RAM including concurrent parser processes. Do not assume file size equals in-memory size. A bounded representative probe should measure both before scaling. Keep an isolated copy when the parser mutates inputs or recovery requires it; explain that cost.

## Cache with a real latency requirement

An agent proposes eliminating a large cache to save disk. The product has an explicit response-time target and expensive repeated computations.

Compare no cache, a size-limited cache with eviction, and the current cache under representative access patterns. Preserve correctness and account for recomputation, network traffic and cache misses. Retaining bounded storage may be the better choice. The recommendation must identify invalidation, ownership and retention rules, not just report bytes removed.

## One-off report versus a new platform

An agent proposes a database, vector index, container stack and always-running worker for a one-time report.

Check whether existing local queries or a small script meet retrieval, reproducibility and delivery requirements. Reject new infrastructure whose benefits are only speculative. Retain a database or isolated environment if actual data volume, query needs or dependency conflicts justify it. Make installation footprint, idle memory and ongoing maintenance visible.

## Compact decision record

| Question | Required answer |
|---|---|
| Goal and constraints | Observable completion and must-preserve properties |
| Alternatives | Proposed design, reuse and smaller viable option |
| Resource envelope | Peak/retained disk, peak/idle RAM and material compute/network cost; measured, estimated or unknown |
| Justification | Why each material addition is worth its cost; who bears it |
| Lifecycle | Artifact destination, owner, retention and authorized cleanup conditions |
| Validation | Representative workload, baseline, measurements and failure/cancellation checks |
| Decision | Chosen option, rejected alternative, uncertainty and stop/owner-decision conditions |

## Review checks

- No measurements supplied: report unknowns or labeled estimates, never invented savings.
- Low memory but high disk: identify spill/temp growth rather than calling the design unconditionally efficient.
- Critical recovery copy: preserve it until equivalent recovery is demonstrated.
- Budget exceeded: stop or escalate the decision; do not silently enlarge the budget.
- Existing user cache: recommend a retention policy without treating review as deletion permission.
- Tiny task: a concise comparison is enough; avoid speculative frameworks and elaborate profiling.
