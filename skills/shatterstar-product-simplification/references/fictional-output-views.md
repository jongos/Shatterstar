# Fictional worked example: overlapping output views

All artifacts, tasks and proposals below are invented. No users, telemetry or application were evaluated.

## Synthetic source A: interface inventory

An imaginary report tool has Results, Recent Outputs and Saved Outputs destinations. Each links to the same underlying output IDs. Results shows the latest run; Recent Outputs lists twenty runs; Saved Outputs lists pinned runs. Results provides export. Recent Outputs provides comparison and failed-run retry. Saved Outputs supports retrieval by label. Keyboard navigation and permission enforcement are specified requirements, but current compliance is unknown.

## Synthetic source B: task brief

Required tasks are finding the newest output, retrieving an older pinned output, comparing two runs, exporting an authorized output and recovering from a failed run. No usage analytics or research findings are available.

## Ranked proposals

1. **Combine navigation into one Outputs destination, retaining Latest, Recent and Pinned filters.** Evidence: shared output IDs and overlapping lists in [A](#synthetic-source-a-interface-inventory). Hypothesis: fewer destination choices may reduce wrong turns. Preserve comparison, export and retry actions with their original permissions. Cost: migration of links, filter state and keyboard navigation; users may lose familiar entry points. Confidence: moderate for overlap, low for benefit. Counterexample: frequent comparisons across independently open views become slower. Conservative alternative: group the three existing links under Outputs without changing routes.
2. **Defer removal of the old destinations until coverage is verified.** Keep compatibility routes into equivalent filters and preserve bookmarks. This adds temporary maintenance cost but limits retrieval regressions. Remove redundant navigation only after the first proposal meets its criteria; retain routes while external dependencies remain unknown.

Do not remove retry or comparison merely to make the new destination visually smaller. Their distinct jobs are explicitly required by [B](#synthetic-source-b-task-brief).

## Preserved-task and dependency checks

| Task/dependency | Proposed path | Constraint / verification status |
|---|---|---|
| Find newest | Outputs, Latest filter | Sorting and stale-state indication required; untested |
| Retrieve older pinned item | Outputs, Pinned filter plus label search | Preserve IDs and pins; untested |
| Compare two runs | Select two eligible outputs, Compare | Keyboard selection and accessible labels required; untested |
| Export | Output detail, Export | Preserve authorization and format choices; untested |
| Recover failed run | Failed output, Retry | Preserve original retry safety rules and feedback; unknown implementation |
| Existing links | Compatible route to matching filter/detail | Inventory deep links and integrations before removal; unknown |

## Proposed experiment and rollback

Product owner decides whether to prototype consolidation. First collect baseline task completion, wrong-destination visits and step counts on the existing design; do not invent values. Use matched task conditions, including keyboard-only and relevant assistive-technology paths, for a prototype comparison. UX and engineering owners jointly check task coverage and dependency inventory. No live rollout is implied.

Proposed acceptance: every required task remains reachable with appropriate permissions and no lost data; no new keyboard trap or unlabeled action; comparison/export/retry remain available; fewer wrong-destination visits without worse completion for any critical task. These are hypotheses to test, not measured outcomes. Agree participant coverage and meaningful thresholds before collecting comparative data; an inconclusive result does not justify removal.

Stop evaluation on any lost critical path or authorization regression. If later authorized for deployment, retain original routes, data schema and navigation configuration so the release owner can restore navigation without data conversion. Roll back on a critical-path failure. Human decisions remain: acceptable navigation costs, evaluation sample, observation window and compatibility-route retirement.
