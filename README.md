# Project Brain OS

Reusable product + engineering operating system for building software projects with a Product Owner and an AI Project Brain.

## Canonical source

This repository is the **source of truth** for Project Brain OS.

- GitHub = canonical/versioned source.
- ChatGPT Library = activation mirror/fallback.
- Product repositories = project-specific state only.

If a Library copy disagrees with this repository, this repository wins.

## Current version

**v1.4.1**

## Activate in a new chat

Use:

> Activa Project Brain OS desde `DigitalAppcorp/project-brain-os` y trabaja sobre mi proyecto. Audita el estado real antes de hacer código.

For a new product:

> Activa Project Brain OS desde `DigitalAppcorp/project-brain-os`. Vamos a iniciar un proyecto nuevo.

## Core files

- `SKILL.md` — operating system and rules.
- `VERSION` — current stable version.
- `CHANGELOG.md` — generalized learnings and version history.
- `ACTIVATE.txt` — short activation phrases.
- `PROJECT_STARTER.md` — bootstrap workflow for new products.
- `templates/` — reusable project documentation templates.
- `patterns/` — reusable decision/engineering patterns.
- `knowledge/marketing/` — reusable Marketing Intelligence & Growth module (strategy, acquisition, paid media, SEO, CRO, analytics, retention, compliance, monthly source-review protocol). Start at [Marketing Brain](knowledge/marketing/README.md); its own version is 0.1.0 and it does not change core Brain OS v1.4.1.
- `knowledge/ui-ux-frontend/` — reusable UI/UX Frontend Engineering skill: research, interface design, accessibility, responsive/PWA patterns, React-state reliability, evidence-driven critique and QA. Start at [UI/UX Frontend Engineering](knowledge/ui-ux-frontend/README.md). Module version 0.4.0 (READ_ONLY_AUDIT, measured evidence, single normative authority; evaluation fixtures not yet independently run); core Brain OS version remains unchanged.

## Principle

Project Brain OS contains **how to think and work**, not the state of a specific product.

A product-specific fact belongs in that product's repository. A generalized lesson that improves future projects belongs here.


## v1.3 closure rule

Before a module/phase can be marked **COMPLETED**, run **Scope Closure Reconciliation**:

- compare approved product scope, architecture and Definition of Done against what was actually delivered;
- separate implementation evidence from visual/product evidence;
- treat agreed experiments, assets and UX deliverables as real scope, not optional future work;
- leave the phase open if any approved item is implemented but unvalidated, or missing entirely;
- inspect active branches/open PRs when recovering context in a new chat, not only `main`.


## Cross-chat continuity (v1.4.1)

Apply `patterns/VERIFIABLE_HANDOFF.md` before a new chat takes over: short current handoff plus archived history, verified branch HEAD vs main/production, backend state, QA evidence, precise next action and authorization limits. Never copy a particular product's implementation details into this reusable OS.
