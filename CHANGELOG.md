# Changelog

## Unreleased — 2026-10-28

### Video Production OS v0.1.0 — habilidad nueva
- Añade módulo reutilizable de dirección creativa y producción audiovisual con cuatro rutas (comercial cotidiano, animación 3D, mascotas reales y demostración auténtica).
- Aísla validación técnica de video, juicio de calidad, autorización visual, derechos comerciales, publicación y medición real.
- Incorpora pipeline FFmpeg sin coste de créditos con pruebas de decodificación/metadata y plantillas de brief, toma y scorecard; Blender sigue pendiente de validación real.
- Integra Marketing Brain OS y Design Intelligence OS sin imponer estética, suscripciones ni gastos a productos.

## Unreleased — 2026-10-23

### Marketing Intelligence & Growth knowledge module
- Add an independent, reusable `knowledge/marketing/` domain with strategy, paid ads, creative/CRO, SEO/AI search, analytics, retention and compliance guidance, verified primary sources and experiment templates.
- Introduce a monthly/event-triggered maintenance protocol with dated evidence and PR review; no automatic ad spend or changes to product-specific repositories.
- Keep core Brain OS at v1.4.1; marketing module starts at v0.1.0 and complements existing gates and authorization rules.

## Unreleased — 2026-10-19

### Preview budget and payment-gateway continuity
- Preserve remaining deployment attempts by treating connected Git pushes as potential preview deployments; require a provider/PO-verified Preview OFF control and distinguish provider readback from a CI PASS.
- For financial gates, distinguish code-only provisioning, hosted metadata, existing role grants, scoped secret access and actual Live settlement. Record migration versions from the provider and never silently bypass a blocked credential-revealing RPC.
- Keep reusable rules in Project Brain OS; sensitive resources, product decisions, exact pending gates and fixture counts in the product repository.


## Unreleased — 2026-10-18

### Improved cross-chat continuity
- A Product Owner's rejected screenshot must be kept separate from a newer, already-committed UI iteration; require latest branch/CI verification and an actual screenshot of the new iteration before treating the rejection as current.
- Preserve discoverable approved-reference and rejected-runtime image paths from an accessible file library or project repo; resume from the comparison gate without asking users to repeat design choices.
- A design mock's business charts and numbers are not production data: preserve visual hierarchy with verified sources, label unavailable histories and metrics honestly.
- When an active handoff becomes huge, archive it before writing one concise, authoritative current snapshot. Project facts stay in the product repo; generalized recovery rules live in `patterns/VERIFIABLE_HANDOFF.md`.

## Unreleased — 2026-10-14

### Clarified
- During cross-chat transfers, a failed CI job must be diagnosed at its actual first actionable step, including strict shell optional-variable checks. Fix the narrow cause, rerun on the corrected HEAD and report failed-vs-passing run IDs distinctly; never imply generic CI PASS supersedes a separate failing database job.


## Unreleased — 2026-10-13

### Clarified
- After an interrupted tool batch or chat, verify remote HEAD/CI/files before replaying operations. An exception in a multi-action run does not prove that prior steps were rolled back, and another executor may have finished the work; a cross-chat handoff should resume only truly pending gates.
- Visual implementation handoffs distinguish a Product Owner's selected design concept from coded behavior, passing CI and actual browser/product acceptance. Record exact layout and preserved action contracts, current HEAD (not earlier failed CI), safe local preview steps and the sole remaining acceptance gate; do not ask the user to select the option again.

## Unreleased — 2026-10-12

### Clarified
- For cross-chat handoffs involving source-to-Figma (or other design editor) replication, require **real runtime evidence + visual fidelity + editable semantic layers**; generic editable sketches are not valid replicas.
- Reject and explicitly segregate inaccurate design drafts, inspect the precise live runtime/revision, and validate one real screen with the Product Owner before mass production. Keep product-specific Preview URLs and Figma files only in their own repos.

## Unreleased — 2026-10-11

### Clarified
- Cross-chat transfers after parallel agent activity must rebase their knowledge on the latest remote branch and live provider snapshot, preserve newer checkpoints and avoid duplicate commits/tests when a handoff is already accurate.
- An authorized irreversible step may remain operationally BLOCKED; carry forward exact authorization scope, operator access, rollback and evidence without suggesting it executed.

## Unreleased — 2026-10-10

### Clarified
- A paused external/local executor keeps ownership of its explicitly delegated task; quota interruption is neither PASS nor failure. Keep the exact resumable checkpoint, prevent duplicate test identities and continue only independent work.
- A new chat must not assume external execution resumes automatically or interpret prepared scripts/green CI as end-to-end deletion evidence.
- Git history can preserve a superseded handoff while the live file becomes a short authoritative snapshot; branch pushes may trigger automatic preview integrations even without manual deployment.

## Unreleased — 2026-10-09

### Clarified
- Cross-chat recovery must prioritize **one concise, verified live snapshot** over a chronological accumulation of superseded checkpoints.
- When a decision is closed but its implementation/Definition of Done is pending, label both states explicitly rather than reporting a false completed phase.
- Distinguish last verified CI from subsequent commits, and mark local changes or privileged external actors **unknown** when not independently inspected.
- Preserve historical evidence by archiving; keep product-specific details in the product's own repository. No change to version 1.4.1 semantics or deployment authority.

## 1.4.1 — 2026-10-08

### Added
- `patterns/VERIFIABLE_HANDOFF.md`: compact, auditable cross-chat recovery without reconstructing product state from a long conversation.
- An explicit distinction among code present, CI build, live backend, user-driven visual QA, and an unexecuted test.
- Mandatory recording of the **latest** branch/PR HEAD, local-only uncertainty, external migration/deploy state, exact user action pending, and authorization boundaries.
- Archive-over-append strategy when ACTIVE_HANDOFF grows too large; preserve history separately, keep current snapshot short.

### Fixed
- Aligned SKILL frontmatter and README version markers with the canonical VERSION.
- Clarified that an approved technical workflow does not automatically authorize production release, paid resources, irreversible deletion, or bypass of visual acceptance gates.

## 1.4.0 — 2026-10-08

### Added
- **Local-First Efficiency Mode** for projects optimizing token usage, development time and infrastructure cost.
- Explicit environment truth model: local working tree, local HEAD, remote branch, main and production are distinct states.
- Grouped local verification pattern: one blocking verify command, with legacy/non-blocking debt tracked separately.
- Production-by-exception rule during development.
- Local Git checkpoints with remote push/PR only at meaningful milestones.
- Release reconciliation gate before backend production/deployment.
- Canonical pattern: `patterns/LOCAL_FIRST_EFFICIENCY.md`.

### Clarified
- Local development alone does not inherently reduce model tokens; token savings come from grouped verification, concise error reporting, canonical handoffs and fewer redundant remote audits.
- Production should not be used as the routine development/test environment.
- Historical migration chains that cannot rebuild a blank local database require a reviewed baseline/reconciliation strategy rather than repeated ad-hoc patches.
- Handoffs must record local-only state explicitly so a new chat does not assume GitHub contains the newest work.

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
