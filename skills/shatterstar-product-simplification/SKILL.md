---
name: shatterstar-product-simplification
description: Assess evidence-backed removal, consolidation, hiding or deferral of product features and interface controls while preserving important tasks, accessibility and rare critical actions. Use for deliberate simplification proposals, not generic UI criticism or automatic redesign.
---

# Shatterstar product simplification

Make subtraction accountable to task coverage and evidence. Invoking this skill does not authorize deleting or editing implementation, changing configuration or running a live experiment.

## Ground the assessment

Define the product area, intended audience, important jobs and constraints. Inventory candidate controls/features and dependencies: navigation, data, permissions, exports, integrations, accessibility, support and recovery. Link claims to supplied artifacts using specific locators. Mark facts, inferences, assumptions and missing evidence separately. Do not invent analytics, participants or measured benefits.

Map each candidate to the tasks it enables and the people or contexts relying on it. Preserve rare but critical tasks, including recovery and accessibility paths, even if frequency is low or unknown. Low usage alone does not establish low value; examine discoverability, eligibility, seasonality and consequences of losing the action.

## Propose subtraction

Consider removing, combining, hiding or deferring candidates when evidence suggests redundant destinations, unnecessary choices or avoidable task steps. Trace both direct and indirect dependencies before recommending a change. Keep essential state, permissions and user data intact in the proposal. When coverage cannot be established, prefer retaining the feature or a smaller reversible alternative.

For each proposal specify the exact subtraction, remaining entry point, task coverage, evidence, expected benefit hypothesis, costs and affected users. Include a counterexample that could make the proposal harmful and a conservative alternative such as relabeling, grouping or reducing prominence. Hiding can impose discoverability costs; consolidation can add navigation or remove useful side-by-side context. Do not present reduced control count as proof of improved usability.

Rank proposals by evidence strength, plausible task benefit, regression severity, dependency cost and reversibility. Use qualitative judgments with reasons when data is insufficient; avoid fabricated precision. Explain why retaining a candidate may outrank removing it.

## Make the decision testable

Specify a reversible experiment or prototype evaluation, who must decide, an owner role, baseline to collect, observable success and failure criteria, accessibility checks, duration or stopping condition, and a rollback path. Label invented thresholds as proposed. If no analytics exist, suggest task walkthroughs or observation and describe evidence still needed, without claiming they happened.

Separate demonstrated findings from simplification hypotheses. A prototype passing task checks does not establish production benefit or general human efficacy. Stop at recommendations unless the user separately requests implementation or experiment execution.

## Deliver

- A source register, scope and evidence gaps.
- Ranked subtraction proposals with retained destination, rationale, tradeoffs, counterexamples, conservative alternatives and confidence.
- A preserved-task matrix mapping every important task and dependency to its proposed path, permission/accessibility constraints and verification status. Missing coverage blocks a removal recommendation.
- Experiment and rollback plans with falsifiable acceptance criteria, uncertainty and explicit human decisions.

Read the [fictional output-view example](references/fictional-output-views.md) for a compact proposal and coverage matrix. Longshot's rendered-interface testing and Dazzler's creation work are separate capabilities, not required dependencies.
