---
name: shatterstar-product-simplification
description: Assess evidence-backed removal, consolidation, hiding or deferral of product features and interface controls while preserving important tasks, accessibility and rare critical actions. Also challenge agent implementation plans for unnecessary complexity, storage, memory and compute costs. Use for deliberate simplification and resource reviews, not automatic redesign or cleanup.
---

# Shatterstar product simplification

Make subtraction accountable to task coverage and evidence. Invoking this skill does not authorize deleting or editing implementation, changing configuration or running a live experiment.

Apply this to navigation and dashboards, settings and advanced controls, onboarding and forms, administrative workflows or feature retirement. Preserve the job, not necessarily its existing surface. Compare remove, merge, hide and defer against a credible keep/clarify baseline; there is no reduction quota.

## Ground the assessment

Define the product area, intended audience, important jobs and constraints. Inventory candidate controls/features and dependencies: navigation, data, permissions, exports, integrations, accessibility, support and recovery. Link claims to supplied artifacts using specific locators. Mark facts, inferences, assumptions and missing evidence separately. Do not invent analytics, participants or measured benefits.

Map each candidate to the tasks it enables and the people or contexts relying on it. Preserve rare but critical tasks, including recovery and accessibility paths, even if frequency is low or unknown. Low usage alone does not establish low value; examine discoverability, eligibility, seasonality and consequences of losing the action.

For each job, record affected cohorts, observation window and eligible-user denominator when supplied, frequency separately from criticality, friction, dependencies, uncertainty and evidence that would change the recommendation. Track burden removed and burden displaced to navigation, memory, support, migration or expert work; name who benefits and who pays.

## Propose subtraction

Consider removing, combining, hiding or deferring candidates when evidence suggests redundant destinations, unnecessary choices or avoidable task steps. Trace both direct and indirect dependencies before recommending a change. Keep essential state, permissions and user data intact in the proposal. When coverage cannot be established, prefer retaining the feature or a smaller reversible alternative.

For each proposal specify the exact subtraction, remaining entry point, task coverage, evidence, expected benefit hypothesis, costs and affected users. Include a counterexample that could make the proposal harmful and a conservative alternative such as relabeling, grouping or reducing prominence. Hiding can impose discoverability costs; consolidation can add navigation or remove useful side-by-side context. Do not present reduced control count as proof of improved usability.

Rank proposals by evidence strength, plausible task benefit, regression severity, dependency cost and reversibility. Use qualitative judgments with reasons when data is insufficient; avoid fabricated precision. Explain why retaining a candidate may outrank removing it.

Hidden controls need recognizable labels, accessible entry points and return paths. Search or command palettes do not automatically replace recognizable navigation. Separate interface changes from capability retirement: inventory known and unknown consumers, APIs, integrations, saved data, deep links and permissions. Require replacement coverage, migration/notice/support plans, ownership, rollback feasibility and explicit blockers before recommending retirement. A hidden button is not a retired feature; a feature flag cannot undo incompatible data changes.

## Challenge agent implementation plans

Apply this review before substantial implementation, dependency installation, bulk downloads, replication or persistent infrastructure, and again when the plan materially expands. For a small change, use a short comparison; do not create an audit system larger than the work. Invoking this skill alone remains review-only.

Define the required outcome, correctness, reliability, security, recovery and performance constraints first. Compare the proposed approach with reuse of existing capabilities and a smaller viable implementation. Explain why each new service, dependency, data copy, index, cache, environment or abstraction is necessary. Prefer the simplest approach that meets the constraints, not the shortest code or lowest byte count at any cost. Do not claim a globally optimal design without evidence.

Account for peak and retained disk usage separately, including inputs, expanded downloads, intermediate files, outputs, logs, backups, build artifacts and duplicate environments. Account for peak and idle RAM, concurrent workers and per-worker buffers; consider CPU/GPU time, network transfer and model calls when material. Available capacity is not a reason to consume it. Distinguish measured values, estimates with assumptions, and unknowns; never invent savings or hide costs on another machine or service.

Challenge whole-dataset loading when bounded streaming or batches would work, unbounded parallelism, repeated full copies, redundant dependencies, unlimited caches/logs, persistent processes for one-off jobs, and speculative infrastructure. These are candidates to investigate, not automatic prohibitions: measure the relevant tradeoff and preserve required isolation, reproducibility, latency and recovery.

Before proceeding under implementation authorization, show the user the chosen approach, smaller alternative, expected resource envelope, unavoidable costs and reasons for rejecting the alternative. Use explicit user limits when supplied; otherwise propose proportionate limits with assumptions. If a material cost cannot be bounded, resolve it with a bounded probe or surface the decision before costly execution. Pause at an agreed budget breach or unexpected growth rather than silently increasing scope.

For generated artifacts, define ownership, destination, lifetime, reuse and cleanup conditions. Do not delete existing user files, caches, backups or recovery material as an optimization without the necessary authorization and preservation checks. Prefer avoiding needless creation over creating bulk artifacts and promising cleanup later.

Validate the chosen design against representative workloads and a credible baseline: task correctness, latency, peak memory, peak disk and retained disk where relevant. Include growth with input size and concurrency, failure recovery and cancellation. Measure the whole process tree when workers materially contribute. Keep profiling bounded. Label synthetic checks as synthetic; a smaller footprint is not proof of better performance.

Deliver a compact resource decision alongside the task matrix: alternative comparison, justified additions, resource estimates or measurements, retention plan, limits/stopping conditions, unresolved uncertainty and owner decisions. Explain costs in plain language so the human can challenge them. Read the [agent resource examples](references/agent-resource-review.md) for calibration.

For development and testing artifacts, apply the [storage lifecycle workflow](references/storage-lifecycle.md): task-scoped output locations, a lightweight artifact register, bounded generation and retention, and an exact-file completion review. Extend existing provenance records; do not build duplicate infrastructure.

## Make the decision testable

Specify a reversible experiment or prototype evaluation, who must decide, an owner role, baseline to collect, observable success and failure criteria, accessibility checks, duration or stopping condition, and a rollback path. Label invented thresholds as proposed. If no analytics exist, suggest task walkthroughs or observation and describe evidence still needed, without claiming they happened.

Separate demonstrated findings from simplification hypotheses. A prototype passing task checks does not establish production benefit or general human efficacy. Stop at recommendations unless the user separately requests implementation or experiment execution.

Match validation to the claim: destination finding and wrong turns for navigation; completion, errors and rework for workflows; actual consumer coverage for retirement. Exercise rare critical scenarios explicitly rather than assuming ordinary A/B traffic will cover them.

## Deliver

- A source register, scope and evidence gaps.
- Ranked subtraction proposals with retained destination, rationale, tradeoffs, counterexamples, conservative alternatives and confidence.
- A preserved-task matrix mapping every important task and dependency to its proposed path, permission/accessibility constraints and verification status. Missing coverage blocks a removal recommendation.
- Experiment and rollback plans with falsifiable acceptance criteria, uncertainty and explicit human decisions.

Read the [fictional output-view example](references/fictional-output-views.md) for a compact proposal and coverage matrix. Longshot's rendered-interface testing and Dazzler's creation work are separate capabilities, not required dependencies.

Consult [research and conditional checks](references/research.md) when choosing evaluation methods, progressive disclosure or retirement safeguards. These are research-informed heuristics, not a validated scoring instrument.
