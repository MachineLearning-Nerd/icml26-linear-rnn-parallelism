# Evaluator-blind pre-publication red team

The reviewer used only the freshly staged candidate at
`/tmp/linear-rnn-candidate-current.YsEzjf` and the evaluator rubric. Repository
knowledge, OpenResearch logs, experiment descriptions, and hidden dashboard
paths were not used to fill gaps.

## Pass 1 — historical candidate rejected

The earlier candidate exposed only `overview`, `claims`, `evidence`, and the
weak historical verification page. The reviewer could not locate the current
claim contracts, executable symbolic checkers, or raw results. That candidate
was rejected and is retained only as historical evidence.

## Pass 2 — current candidate accepted for release gating

Files opened from the canonical entrypoint:

1. `README.md`
2. `pages/index.md`
3. `pages/executive-summary/page.md`
4. `pages/claim-1/page.md`
5. `pages/claim-2/page.md`
6. `pages/claim-3/page.md`
7. `pages/claim-4/page.md`
8. `pages/claim-5/page.md`
9. `pages/claim-6/page.md`
10. `pages/conclusion/page.md`
11. every current verifier, implementation, raw JSON, checker output, and
    negative-control output linked from those pages

Reviewer conclusions:

| Claim | Current verifier located | Exact contract | Data inline | Raw link | Control | Verdict supported |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Yes | Yes | Yes | Yes | Yes | BLOCKED |

Automated companion audit:

```json
{
  "candidate_file_count": 175,
  "judged_file_count": 128,
  "old_file_set_is_subset": true,
  "protected_historical_files_preserved": 128,
  "superseded_paths_archived": 15,
  "upload_file_count": 62,
  "text_only_upload": true,
  "secret_hits": 0,
  "visibility_matrix_complete": true
}
```

No conclusion was filled from inaccessible evidence. Claims 5 and 6 remain
visibly blocked. The live judge may disagree with the scientific strength of a
certificate; that uncertainty is represented in the forecast rather than
hidden.
