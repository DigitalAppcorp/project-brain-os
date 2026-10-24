# Pattern — Backend Safety

For private backups and isolated restores, also apply
[Private recovery execution boundary](PRIVATE_RECOVERY_EXECUTION.md): verify
the actual executor and destination before exporting any private data.

Before mutation:
1. inspect current schema;
2. inspect grants/RLS/functions/storage;
3. define ownership and threat surface;
4. prepare versioned migration;
5. least privilege review;
6. preflight build/diff;
7. obtain explicit approval when project policy requires it.

After mutation:
1. verify schema;
2. owner/non-owner tests;
3. invalid-input tests;
4. destructive tests with rollback where possible;
5. security/performance advisors;
6. record migration state in docs;
7. never rewrite applied migration history—use forward migrations.
