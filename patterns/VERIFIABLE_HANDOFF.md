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

## Operational readiness for irreversible hosted actions

- **Deployment access is not execution capability.** Before a sensitive or destructive hosted trial, prove that the *same bounded execution workflow* can authenticate as the real authorized operator, call the supported runtime endpoint, manage required server-side flags, and perform a verifiable immediate rollback. Merely being able to push code, list secrets or inspect a provider does not prove these powers.
- Keep the release-wide gate disabled. A narrowly authorized test may use an additional allowlist-bound, disabled-by-default route; never make the release route broadly executable as a shortcut.
- Verify immutable resource identity, reference safety and expected live state just before any irreversible operation. For object storage, metadata/database presence, SDK info, HTTP accessibility and CDN propagation are distinct evidence; don't equate them.
- If invocation, permissions, flag management, or rollback are not demonstrably operable, **fail closed before activating**. Record the operator dependency and precise next step in the product handoff, preserve previous approvals in scope, and do not ask the Product Owner to repeat already accepted QA.
- Distinguish **safe code deployed**, **operator gate ready**, **destructive action executed**, **origin absence verified**, and **public access/CDN verified** as separate states. An unsuccessful or partial cleanup is not a full PASS. No user tokens, user-owned storage paths, or credentials belong in generic operating-system patterns.

## Handoff when other executors have continued

- When a user requests a new chat after several agents have worked in parallel, **fetch the newest remote branch, runtime state and compact handoff before writing**. A newer verified checkpoint supersedes an older chat summary; do not overwrite it or reintroduce superseded blockers.
- **Prefer a minimal correction or a verified no-op** if the current snapshot already covers the truth. Unnecessary documentation pushes trigger CI and sometimes preview integrations, and create false-looking new milestones.
- For an irreversible operation already authorized but still blocked, preserve its **exact resource scope, remaining operator capability, fail-closed controls, rollback prerequisite and authorization validity**. Do not infer execution merely from deployment access or a visible browser UI; do not ask for the same approval again without changed scope.
- Distinguish observations made by connected read-only provider tools from statements relayed by other agents. Do not silently upgrade either into a live authenticated execution PASS.

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

## Faithful source-to-design handoff — avoid manufactured replicas

When the user requests **replication** of an existing product screen in an editable design tool (Figma or equivalent):

- **An editable artifact is not automatically a faithful artifact.** Distinguish three evidences: source app actually inspected, visual match tested against that source, and editable semantic layers (text, controls, vectors, component hierarchy). Each must have independent proof before reporting success.
- A React file's component names or text snippets alone are not enough to recreate a real screen's spacing, imagery, interaction states, responsiveness or overlays. Never fabricate placeholders, generic cards, logos or maps and call them reproductions.
- Before bulk conversion, verify which live runtime/revision the user actually uses; compare against the code HEAD, confirm accessible routes and whether authenticated states are observable. Never assert Preview equals the latest branch without SHA evidence.
- For web apps, a screenshot/capture is a **reference**; deliver design-editor native text, auto-layout, icons, real independent images and components. A single flattened screenshot inserted into a design file fails the editable deliverable gate even if pixel-identical.
- Begin with **one real screen and one relevant state**, validate its visual match with the Product Owner, then scale into further routes/steps. If the provider's session/authentication prevents direct inspection, state the limitation precisely and ask for the smallest legitimate evidence (e.g., screenshots or user-controlled computer session), not passwords.
- If the Product Owner rejects a purported reproduction, **mark the existing asset as REJECTED**, leave it out of the completion count and next gate, preserve it only as a noncanonical draft, and document the corrective source-first action explicitly. Never use the rejected draft as a new design source of truth.
- When transferring across chats, include the verified runtime URL and design file link as **references**, not proof of fidelity. Note what was directly observed versus assumed, and do not repeat a failed synthetic reconstruction.

This rule is provider-agnostic and applies to all software products; put project URLs, file keys and exact design decisions only in the product repository.

## Handoff for an approved visual implementation awaiting Product Owner QA

A Product Owner may select a specific numbered visual concept and authorize coding in an active feature branch. After code/build is ready, a handoff must **preserve the choice without turning it into acceptance**:

- Record the **exact selected option and layout contract**, including which surfaces fill the viewport, where controls and scrolling live, and which pre-existing actions must remain usable; label references as *approved design concept*, not a screenshot of implemented runtime.
- Separate **source changes**, **green CI on a specific SHA**, **provider/backend changes**, **browser appearance observed**, **user product acceptance**, **PR merge**, and **production deployment**. Their statuses never imply each other.
- Do not ask the Product Owner to choose the same design again or redelegate implementation to another AI after code was authorized. The next step is to show the actual feature-branch implementation in the user's preview, then fix *specific observed visual/regression issues*.
- Do not infer a local working tree is clean. Before prescribing pull/checkout, ask for or inspect `git status --short`; never advise destructive reset on an unobserved workspace.
- If earlier commits failed but a **later HEAD passed**, record both with precedence. The handoff should identify the newest verified passing commit and the exact still-unverified runtime behavior, not a stale CI blocker.
- Keep new code/refactoring and history in the product repo; the live snapshot should prioritize the **single next acceptance gate**. Pushing only documentation may start CI; verify the newer commit separately rather than inheriting its parent's green status.

This is reusable workflow guidance only. Individual product options, local paths, provider IDs and screenshot descriptions belong in the product handoff, not here.

