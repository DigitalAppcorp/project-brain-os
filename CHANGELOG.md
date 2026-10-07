# Changelog

## 1.3.0 — 2026-10-07

### Added
- **Scope Closure Reconciliation** before marking a module/phase completed.
- Explicit distinction between implementation/build evidence and visual/product acceptance evidence.
- Closure checklist that reconciles approved scope, architecture, DoD, migrations, runtime behavior, experiments and visual assets.
- Recovery rule to inspect active branches and open PRs when `main` may lag current in-progress work.
- Stronger active-handoff requirements: current defect, exact next verification, active PR/head, backend state and Product Owner approvals.

### Clarified
- A working core does not imply the whole approved phase is complete.
- Agreed fake doors, visual assets, models, instrumentation and UX elements are deliverables when they were part of approved scope.
- Product Owner approval applies only to what was actually shown/tested; unseen scope cannot be inferred as approved.
- Premature closure must be reopened and corrected forward rather than rewriting history.


## 1.2.0 — 2026-10-06

### Added
- Explicit **Idea Bank + Conceptual Audit** before committing to experiment/specification.
- **Minimum Useful Real Core** strategy for MVP-critical modules.
- Contextual validation of advanced/optional capabilities inside a real usable module.
- Canonical GitHub source-of-truth policy with Library as mirror.
- Generalization filter: project-specific decisions stay in the project; reusable lessons go into Project Brain OS.

### Clarified
- Fake doors are a validation tool, not a mandatory pattern.
- A usable MVP should not become a collection of placeholders when that would invalidate the product experience.

## 1.1.0

- AI Project Brain owns architecture, implementation, backend, security, tests, Git/PR and durable documentation.
- Antigravity/local environment is execution/visualization only.
- No routine delegation to other AI assistants.
