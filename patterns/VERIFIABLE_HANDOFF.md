# Pattern — Verifiable Compact Handoff (cross-chat continuity)

## Purpose

Keep the software project's behavior, decisions and next action consistent across new chats **without copying a whole conversation**. The canonical repository, not a chat's memory, is the source of truth.

## Two layers

1. **Live snapshot**: a short `ACTIVE_HANDOFF` (ideally 3–8 KB, not a chronological diary) with verified current state.
2. **History archive**: immutable or append-only records of past migrations/bugs/QA and their evidence. Do not destroy them; archive as the snapshot grows.

Product facts stay **only in the product repository**. Generalizable workflow rules stay in Project Brain OS.

## Verify before writing

- Read AGENTS / roadmap / active-module specification.
- Fetch the **current remote feature branch HEAD** and its tree. Inspect `main`, open PRs, check results and deployment separately.
- Record local HEAD and unpushed working tree **only if actually observed**; otherwise say *unknown*, don't invent.
- Read provider schema, migrations, functions, permissions and relevant state when they materially affect the handoff.
- Differentiate: **designed** / **committed** / **build PASS** / **backend applied** / **signed runtime tested** / **Product Owner visually approved** / **merged** / **released**.
- Never call a test PASS from code existing, CI queued, or a synthetic-only test; record method, scope and limitations.

## Precedence and contradiction control

- Keep the live handoff **short and authoritative**. When it becomes a chronological log, archive the full original verbatim, then replace the live file with a current snapshot rather than appending again.
- Put a clear **"verified as of / source / scope"** at the top. Older evidence is history, not a current claim. A new chat should not have to scan dozens of superseded checkpoints to identify the gate.
- When a past heading says **"completed"** but a later acceptance matrix remains open, distinguish *product decision closed*, *implementation/verification incomplete*, and *phase formally closed*. Do not silently overwrite historic product decisions.
- Record the most recent **positive and failed** CI evidence accurately. Verification of a parent commit does not prove the next documentation commit passed; recheck the new branch HEAD.
- State **unknown** explicitly for local unpushed changes, external credentials/writers and runtime behavior not accessible to the agent. Never infer absence from a repository search.
- Include a copyable activation instruction pointing to the canonical project files, not a transcript. A future agent must fetch the latest remote state before implementing.
- Never include real user IDs, JWTs, storage paths of users, medical/payment details or secrets in cross-chat handoffs.

## Required live snapshot

- Project, product owner role, active operating mode (local-first or hosted-first), canonical Brain OS version.
- Branch and last verified HEAD, base main SHA, relevant PRs, Preview vs Production and runtime CI.
- Scope and active module/gate; passed and remaining acceptance criteria.
- Exact migrations already applied, database fixture counts only when recently verified, Edge/function state.
- Current *single next step* with conditions, owner of the step and proof required.
- Explicit previous Product Owner authorizations, expiration/scope, and risky actions requiring a fresh gate.
- Bugs/risks that prevent closure, where to look and tests to reproduce.
- Cost, privacy, security, data retention and irreversible operations guards.
- Handoff timestamp, evidence provenance and uncertainty.

## Transfer algorithm

1. Draft concise snapshot from verified repo/provider facts and Product Owner's actual prior acceptance. Keep historical details in archive.
2. Commit snapshot + archive in a **feature branch** when active work is unmerged; never silently write to main or force-push.
3. Verify the Git commit and branch ref; record resulting exact SHA outside the file if self-referential SHA cannot be inserted atomically.
4. Update reusable Project Brain OS only with transferable lessons, never specific project facts.
5. In the new chat: activate OS, read AGENTS + live snapshot + roadmap + active spec, check remote HEAD/PR/CI, then do exactly the pending action. Do not reboot planning.
6. If the snapshot conflicts with live providers, flag and reconcile **read-only first**.

## Paused delegated work, quotas and parallel tracks

When the Product Owner explicitly delegates a **specific bounded operation** to a local agent, browser/computer executor or another permitted tool, do not convert that task into a permanent blocking dependency for all project work:

- Record the task's exact **owner, permitted environment, file/command to resume, checkpoint, authorization limits, existing disposable resources, and PASS/FAIL/BLOCKED state** in the product repository. Do not create a second copy of a test identity or run the same destructive operation from another chat.
- If the executor is paused by a rate limit, unavailable computer or expired session, mark **PAUSED — not failed and not completed**. Do **not** claim that it will resume automatically. Record what the user must do to re-open it and when (if known, with timezone) without inventing quota information.
- The project brain may advance **independent non-interfering tasks**, but cannot mutate records, environment baselines, configurations or prerequisites reserved for the paused task. Before release or irreversible steps, reconcile the delegated task's actual evidence.
- In a new chat, read the latest product-specific checkpoint and provider state rather than resending the original instruction or re-requesting existing Product Owner approvals. Do not treat an unexecuted script or CI PASS as proof of the external runtime outcome.
- If a handoff file grows into contradictory historical banners, replace it with one short authoritative snapshot. Previous revisions in Git are a valid recoverable history even when no separate archive file is used; explicitly link or identify the last historical commit.
- Remember that pushing to a repository may trigger **third-party CI, preview deploys or billing consequences**. Distinguish a manual deployment action from an automatic integration side effect; minimize unnecessary pushes and do not claim remote environments remained entirely inactive without checking.

## Autonomy and approval

A broad instruction to proceed with technical work saves micro-approvals for reversible in-scope steps but is NOT unconditional authority for release, billing, sensitive/real user data deletion, or bypassing product acceptance. Follow the product's stricter policy when present. Visual validation belongs to Product Owner; backend verification to AI. Don't ask Product Owner to run terminal commands if connected tools can do it.

## Quality bar

A new AI must be able to answer within minutes:
- Where are we exactly?
- What is actually passing?
- What is only staged or pending?
- What should I do next and what must I not touch?
- Which decisions are closed, and what truly needs Product Owner input?

If not, the handoff is incomplete.
