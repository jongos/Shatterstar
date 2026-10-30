# Storage lifecycle for development and testing

Apply proportionately alongside the existing resource review. This is assessment guidance, not deletion authority. Prefer preventing generation over adding a cleanup system.

## Before generating

Verify the canonical checkout, branch, user changes, active consumers and any migration in progress. An older directory is not redundant until migration coverage, source preservation and recovery needs are verified. Unknown migration state blocks a redundancy recommendation.

Choose a dedicated task-specific artifact root outside source and preferably outside cloud synchronization. Resolve paths, check permissions and links/junctions, and isolate concurrent tasks. Put temporary screenshots, extraction, logs and databases there. Promote only reviewed deliverables and required evidence into source control. A temporary path is not permission to discard its contents.

Use a small register, not a new service or database. For each generated file record exact path, purpose, task/run, producer command and version, input identity, regeneration prerequisites, size, category, retention condition and disposition. Record interrupted outputs and unknown provenance. Reference existing preview manifests rather than duplicating them. Bound the register itself and omit secrets/content bodies.

Categories: disposable intermediates (candidate only after use), review evidence (hold through review/investigation), deliverables (preserve at agreed destination), immutable sources (preserve original/provenance), recovery backups (hold until owner-approved recovery requirements expire). Unknown category means retain for clarification.

## While working

Measure baseline, planned expansion, post-run and completion storage. Separate peak from retained, logical from allocated, and estimates from observations. Include cumulative reruns and known external caches; disclose excluded scopes. Agree task-specific budgets and stop before additional generation would exceed them. Unexpected growth or a full retention allowance triggers a decision, never silent deletion or automatic budget expansion.

Reuse unchanged inputs and fixtures only when input hashes, producer/configuration and relevant environment still match. Separate immutable fixtures from mutable test copies. Select likely duplicate candidates before reading/hashing; hash equality is evidence of matching bytes, not equivalent ownership or deletion authority. Normalized text hashes are not byte-identity hashes.

Preserve final validation results and representative unresolved failures. Generate screenshots only when needed, cap logs and evidence bytes, and avoid a full tree copy for every small assertion. A successful test does not invalidate historical failure or recovery evidence. If a prior task directory exists, review/reuse its verified results where appropriate or seek a new bounded run; do not create endless unique directories to avoid the limit.

Prefer deterministic small synthetic database fixtures. Record schema/seed, required cases, processes, connections, database and associated sidecars. Close owned connections on success, error and cancellation. Before any separately authorized removal, verify the database is inactive and preserve required journal/WAL/recovery state; never treat a sidecar as independently disposable. Use large fixtures only for demonstrated scale needs.

For cloud-backed files, inspect metadata first. Distinguish logical bytes, allocated bytes, placeholders and hydrated content. Do not download placeholders just to inventory or hash them. Unknown allocation remains unknown. Reparse points and external consumers require explicit scope review.

## Completion review and authorized cleanup

Produce an exact-file candidate list with sizes, purpose, retention reason, regeneration method, reference/dependency findings, preservation evidence and unresolved questions. Check code, docs, configuration, CI, installations, open processes, symlinks and known external consumers. No search result proves universal absence of consumers. Preserve user edits, immutable sources, required evidence and recovery history. File age, name, hashes and passing tests never authorize deletion.

Keep review separate from execution. Any deletion must match explicit user authorization and revalidated exact paths/identities, containment and preservation. If a cleanup tool is separately authorized, require a receipt linking approval to attempted/completed removals, failures, preserved evidence and before/after measurements. Report logical removed bytes separately from observed allocated/free-space changes, including new receipts and concurrent activity. No deletion means no removal receipt or reclaimed-space claim. Partial failures do not authorize retry or expansion.

## Acceptance scenarios

- Repeated unchanged runs: no hidden accumulation; reuse is justified or the budget/retention gate stops generation.
- Interrupted run: partial artifacts and results are discoverable; no automatic purge.
- Budget breach: no further bulk creation, no silent limit increase.
- User-modified evidence: preserve it and flag the change rather than overwrite it.
- Incomplete migration or unknown references: retain and report uncertainty.
- Cloud placeholder: metadata-only review does not hydrate it.
- Database failure: owned connections close and database/sidecar evidence is accounted for.
- Completion: every retained generated file has a category and reason; cleanup remains a proposal until authorized.

These are evaluation criteria, not claims that all scenarios have been implemented or tested in Shatterstar.
