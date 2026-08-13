# Release gate

The current evidence bundle is publication-ready for review when interpreted
as C1–C4 `VERIFIED` and C5–C6 `BLOCKED`:

- every claim has a source anchor, executable route, raw record, checker, and control;
- C1–C4 exact constructions pass their scoped checks;
- C5 and C6 blockers are explicit and fail closed;
- the conditional complexity assumptions and finite-evidence boundary are documented;
- the historical score snapshots are labeled rather than overwritten.

The old five-claim `outputs/publication_gate.json` is retained as historical
campaign provenance. The six-claim current status is in
`evidence/current/formal_run.json` and the per-claim directories.
