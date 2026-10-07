# Pattern — Scope Closure Reconciliation

Use immediately before marking any module, phase, milestone or PR-backed feature **COMPLETED**.

## Why

A module can have:
- working code;
- passing backend tests;
- a merged core;
- Product Owner approval of the tested flow;

and still be incomplete because another already-approved deliverable was never implemented or never shown.

Closure is therefore a reconciliation task, not a feeling.

## Required reconciliation

Build a compact matrix from the canonical product spec, architecture and Definition of Done:

| Approved item | Implemented | Backend applied | Runtime tested | Product/visual approved | Merged |
|---|---:|---:|---:|---:|---:|

Every approved item must be classified.

Examples of items that count when explicitly approved:
- core flows;
- RLS/ownership rules;
- migrations;
- fake doors / instrumentation;
- visual assets;
- 3D models / animations;
- empty/error states;
- accessibility requirements;
- persistence / F5;
- second-account privacy tests;
- analytics;
- required seed/catalog data.

## Closure rule

A phase is **COMPLETED** only when:
1. every approved in-scope item exists;
2. required backend changes are applied;
3. required technical tests pass;
4. required runtime/visual tests pass;
5. the Product Owner has seen/approved the product-facing items that require acceptance;
6. the PR is merged;
7. `main` is verified;
8. roadmap + handoff reflect the real state.

If any approved item is missing or unvalidated:
- keep Gate 8 open;
- record the exact missing item;
- do not silently reinterpret it as “future”.

## Evidence separation

Never infer:
- build PASS ⇒ visual PASS;
- backend PASS ⇒ UX PASS;
- code present ⇒ runtime works;
- one tested flow ⇒ all approved scope accepted;
- Product Owner “looks good” ⇒ approval of unseen features.

Record each evidence type separately.

## Premature closure recovery

If a phase was marked complete too early:
1. reopen it explicitly;
2. preserve original merge/migration history;
3. create a forward correction branch/PR;
4. record what was missing and why;
5. validate the missing scope;
6. only then close again.

Do not rewrite old migrations or pretend the earlier closure never happened.

## New-chat recovery

When taking over an existing project:
1. read canonical handoff/roadmap;
2. inspect open PRs and active branches;
3. if active work exists outside `main`, read the handoff/docs from that branch;
4. verify the current defect/next action from repo state;
5. continue from the exact unresolved verification instead of restarting planning.
