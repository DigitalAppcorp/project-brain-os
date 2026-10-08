# Local-First Efficiency Pattern

## Purpose

Reduce token usage, engineering latency, infrastructure spend, and production risk during active development.

## Default loop

1. Implement locally.
2. Run one grouped verification command.
3. User returns only PASS or the first actionable error.
4. Commit locally.
5. Continue to next coherent block.
6. Push/PR only at a meaningful checkpoint.
7. Deploy only at release gates unless remote evidence is strictly required.

## Environment truth table

Always distinguish:

| State | Meaning |
| --- | --- |
| Local working tree | What exists only on the developer machine |
| Local HEAD | Last local commit; may not exist remotely |
| Remote feature branch | Last pushed checkpoint |
| main | Last integrated source state |
| Production | Last deployed/runtime state |

Never collapse these into one concept.

## Remote-use test

Before calling a remote provider, ask:
- Can local evidence answer this?
- Does remote verification materially change the decision?
- Is this a release/security/integration gate?
- Does the call/deploy create cost or rate-limit pressure?

If local evidence is sufficient, stay local.

## Verification design

Prefer a single command such as:

`npm run verify`

It should include blocking checks only:
- governance/architecture/privacy contracts;
- type checking;
- build;
- focused tests.

Historical lint debt or known non-blocking warnings should be tracked separately instead of flooding every iteration.

## User interaction

Ask the Product Owner to return:
- `verify PASS`; or
- the first actionable error excerpt.

Do not request full terminal transcripts unless required.

## Backend

Use local database/services for daily work.

For destructive CLI commands:
- pass `--local` explicitly when possible;
- never use `--linked` against production for reset;
- production mutations require the project's normal authorization gate.

If historical migrations cannot rebuild a blank database, establish a reviewed local baseline rather than patching missing legacy objects one at a time.

## Release reconciliation

Before release:
1. inspect local unpushed work;
2. reconcile feature branch vs main;
3. reconcile migration history vs production;
4. validate secrets/providers;
5. complete backup/restore readiness;
6. run final verify;
7. deploy in a controlled batch;
8. smoke test production;
9. update canonical handoff.
