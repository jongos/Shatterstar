# Research-informed simplification

Use only the lenses relevant to the proposal. This synthesis does not validate Shatterstar or predict benefits for a particular product. Source findings, practitioner guidance and derived checks have different evidentiary weight.

| Source | Supported lens and practical use | Limits |
|---|---|---|
| Juvrud, Myers and Nystrom (2024), [People overlook subtractive changes differently depending on age, culture, and task](https://www.nature.com/articles/s41598-024-51549-y) | Replication/extension with 58 adults in Sweden/USA and 58 Swedish children across Lego, grid and digital tasks. Deliberately include a subtraction option alongside alternatives. | Results differ by task, age and sample. Neither a rule that subtraction wins nor a basis for demographic stereotypes. |
| Thompson, Hamilton and Rust (2005), [Feature Fatigue](https://journals.sagepub.com/doi/10.1509/jmkr.2005.42.4.431) | Three digital-player studies found relatively greater emphasis on capability before use and usability after use. Pair preference requests with realistic task and post-use evaluation. | Young/student samples and particular products do not establish long-term enterprise retention or universal feature-count limits. |
| Pirolli and Card (1999), [Information Foraging](https://www.researchgate.net/publication/229101074_Information_Foraging), author-provided paper | Preserve information scent: labels and context must help people judge where useful information is. Assess interpretation and traversal costs when consolidating destinations. | Theoretical account, not a minimum-click or menu-count prescription. |
| Nielsen (2006), [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) | Keep secondary options behind meaningful, discoverable entry points when this supports the task. Preserve return paths and context. | First-party practitioner guidance, not a controlled effect size. Staging may hinder interdependent decisions; no universal depth threshold. |
| W3C WAI, [Make Important Actions and Information Easy to Find](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o2p04-page-important/) | Protect important actions and warnings even when infrequent. Include cognitive accessibility in the preserved-task check. | Supplemental guidance is not itself a WCAG conformance rule or a complete accessibility audit. |
| Kubernetes, [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) | Operational precedent for inventorying consumers through available warnings, metrics or audit evidence, updating consumers and rehearsing disablement before retirement. | Platform-specific practice, not a universal compatibility commitment. Do not copy commands or assume equivalent telemetry exists. |

## Conditional decision checks

For navigation changes, examine whether retained labels predict their destinations; fewer destinations can increase interpretation costs. For progressive disclosure, ask whether a hidden choice is needed to understand a visible one. For retirement, unknown consumers are an explicit blocker until bounded by evidence or a responsible human decision accepting a stated residual risk. Clearly distinguish UI removal, route retirement and backend/data retirement.

Record the job, cohort, eligible population and observation window if known. Keep frequency and criticality separate. State which evidence could reverse the recommendation, who absorbs displaced work and whether rollback restores data as well as interface state.

## Fictional reasoning stress cases

These invented cases are proposed checks, not executed evaluations or measured product findings.

- **Incident console:** A synthetic statistic says “Revoke all sessions” is used in 0.2 percent of sessions. That denominator may not represent eligible incidents. Preserve an accessible emergency path; test authorized discovery and completion during a simulated incident before changing prominence. Low frequency alone cannot justify removal.
- **Scheduling onboarding:** Service, time and price are coupled decisions. Consider deferring optional profile preferences, but keep price visible before commitment and retain the ability to revise interdependent choices. Compare completion errors and rework against the current flow; do not split every choice into its own step.
- **Export retirement:** A low-click export button may coexist with scheduled exports or API consumers. Removing the button is distinct from removing export capability. Inventory consumers and retention obligations; unknown consumers block a confident backend-retirement recommendation. Propose notice, migration and recovery before a human decides on retirement.
