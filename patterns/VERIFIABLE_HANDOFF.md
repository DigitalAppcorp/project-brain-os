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

## Chat-limit interruption protocol

When the Product Owner says the conversation is saturated, broken or they must move to a new chat, **stop feature implementation first** and make continuity the active deliverable:

1. Fetch the remote product repo's *active PR HEAD*, `main`, latest CI outcome, and backend/environment facts available with safe read-only calls. An old handoff is not evidence that the active branch has stopped moving.
2. Read the product's current `ACTIVE_HANDOFF`. If chronological additions make it long or contradictory, save its full previous text under `docs/archive/` and replace it with a compact, authoritative live snapshot. Do not erase the historical trail. In the product roadmap, put a short pointer to that snapshot near the top.
3. Record exact prior authorizations and forbidden gates, backend applied vs DRAFT, unresolved technical/UX requirements, and a **single first action** to take after restart. Mark unknown local worktree or credentials as unknown. Avoid user identifiers, secrets and unnecessary logs.
4. Update reusable OS patterns separately from product state: *product-specific findings belong only in the product repo*. If OS needs improvement, create its own change branch/PR; do not alter its stable version or deploy without the appropriate gate.
5. **Verify remote persistence and CI of both updates**. Do not say "updated" when a tool failed, a commit was not pushed, a pull request is only draft, or only a predecessor's CI passed. If one repository cannot be updated, describe the precise exception and offer the last verified recovery path.
6. End with a short activation phrase pointing to the canonical repository, the **active branch/PR rather than only `main`**, and the authoritative live handoff. A new chat must audit again before coding.

This protocol is a *continuity operation*, not authorization to perform destructive backend work, merge unrelated PRs, or change costs. A user's generic "continue" preserves existing gate restrictions.
