# Pattern — Private recovery execution boundary

Before a backup or restore, distinguish **authorized operation**, **connected
executor**, **private destination** and **credential/key custody**. Repository
access or an administrative connector does not prove execution access to the
operator's computer. A cloud workspace is not that computer merely because it
has the same repository.

- When backup transfers to external services are forbidden, do not export
  private data to a cloud executor as a substitute for a missing local terminal.
  Installing tools, inspecting source and testing synthetic fixtures can proceed.
- Existing operator-bound credentials or encryption identities stay in their
  authorized environment. Do not ask for them in chat, export their values,
  reset them or create replacement keys merely to overcome executor mismatch.
- Preserve the original authorization and request only the missing capability:
  connect execution on the designated private machine. Do not ask the owner to
  repeat technical diagnostics or an already-authorized operation.
- Record actual results separately: tooling, synthetic integrity, private
  export, real hashes, encryption/decryption, isolated database restore,
  catalog/data comparison, service behavior and off-site recovery. No earlier
  stage proves a later one. Historical restore evidence covers its snapshot.
- For cross-platform backup tools, verify actual producer encodings and line
  endings with synthetic fixtures. Parse a supported byte-order mark without
  normalizing the original bytes used for integrity hashes.
- Record exact blockers and unexecuted gates durably. Continue independent
  safe fixes, then hand off one concrete access action. Never report recovery
  PASS or automatic background continuation while essential gates remain open.

Product-specific paths, identities, approvals and evidence belong in the product
repository. Never put private backup files, object paths, row fingerprints or
secrets in this reusable pattern.

## Fidelity of the recovered logical state

- Treat database rows that change during an export as a snapshot problem, not
  as differences to waive. Capture table data and verification evidence in one
  read-only repeatable-read transaction when a faithful comparison requires it.
  Sequence state is not MVCC; record the exact values observed separately.
- Audit extension-owned internal tables and initial schema grants: a successful
  logical dump/restore can still omit them. Preserve a private, hashed recovery
  supplement when needed and compare the complete assembled result.
- Map COPY columns explicitly. Generated columns belong in the source evidence
  but must be regenerated during import. Export partition parents without
  duplicating their children. Compare logical column order, not physical attnum
  gaps left by historical column removal.
- Check the actual lifetime of temporary administrative credentials. Export
  roles before a long dump, or refresh only the failed later connection through
  the existing official authentication; preserve completed artifacts.
- App sandbox virtualization can change canonical Windows paths without a
  filesystem link. Reject linked ancestors first, then resolve a canonical root
  for integrity checks. Keep original bytes and checksums unchanged.
- Preloaded database schedulers/workers can run immediately during recovery.
  Use a new network-isolated target, inhibit restored jobs, direct auxiliary
  workers away from recovered data and verify original final role privileges.
- If encryption follows a successful restore, verify that every extracted file
  is byte-identical to the actual restored inputs. Record that chain of
  evidence explicitly; never infer database or HTTP service recovery from an
  archive checksum alone.
