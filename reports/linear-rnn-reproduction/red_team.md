# Evaluator-blind pre-publication red team

The review used only a freshly staged candidate and the evaluator rubric. It
did not use the repository worktree, OpenResearch logs, experiment
descriptions, or dashboard paths to fill gaps.

## Pass 1 — rejected

Candidate:
`/tmp/linear-rnn-space-candidate.vxm4gx`.

Files opened from canonical navigation:

1. `README.md`
2. `logbook.json`
3. `pages/index.md`
4. `pages/overview/page.md`
5. `pages/claims/page.md`
6. `pages/evidence/page.md`
7. `pages/verification-run/page.md`

The staging overlay had failed because the downloaded README was read-only.
The reviewer could not locate the current verifier, current claim contracts,
new raw evidence, or complete visibility matrix. Claims 1-5 therefore remained
toy-only and Claim 6 remained missing from the evaluator’s perspective. The
candidate was rejected.

Fix: make only the new, isolated staging directory user-writable before the
additive overlay; rebuild from a fresh empty directory. The judged snapshot
itself remains read-only and unchanged.

## Pass 2 — accepted for release gating

Candidate:
`/tmp/linear-rnn-space-candidate.SVDCsi`.

Files opened from canonical navigation:

1. `README.md`
2. `pages/index.md`
3. `pages/release-overview/page.md`
4. `pages/current-claim-1/page.md`
5. `pages/current-claim-2/page.md`
6. `pages/current-claim-3/page.md`
7. `pages/current-claim-4/page.md`
8. `pages/current-claim-5/page.md`
9. `pages/current-claim-6/page.md`
10. every code, contract, certificate, raw result, checker, and control linked
    from those pages

Reviewer conclusions:

| Claim | Located current verifier | Exact contract | Raw evidence | Control | Verdict supported |
| --- | --- | --- | --- | --- | --- |
| 1 | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Yes | Yes | Yes | Yes | BLOCKED |

The automated companion audit reported:

```json
{
  "candidate_file_count": 126,
  "judged_file_count": 16,
  "old_file_set_is_subset": true,
  "protected_historical_files_unchanged": 11,
  "upload_file_count": 113,
  "text_only_upload": true,
  "secret_hits": 0,
  "visibility_matrix_complete": true
}
```

No conclusion was filled from inaccessible evidence. The live judge may still
disagree with the scientific strength of a certificate; that uncertainty is
represented by the claim-level confidence forecast.
