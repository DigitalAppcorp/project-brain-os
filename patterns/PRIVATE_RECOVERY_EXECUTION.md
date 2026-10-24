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
