# Status — Why Are Linear RNNs More Parallelizable?

**State: current six-claim audit complete — C1–C4 verified scoped, C5–C6 blocked.**

- Paper: [arXiv:2603.03612](https://arxiv.org/abs/2603.03612)
- ICML submission: `29sn1uqWn3`
- Authors: William Merrill, Hongjian Jiang, Yanhong Li, Anthony Lin, Ashish Sabharwal
- Overall audit: `PARTIAL_C1_C4_VERIFIED_SCOPED_C5_C6_BLOCKED_HISTORICAL_SCORE_4_OF_12_ARCHIVED_BASELINE_5_OF_12_NO_CURRENT_SCORE`
- Current run: `evidence/current/formal_run.json`
- Current run ID: `18bcc462-fbed-4e4b-8af2-9295100aff38`
- Current scientific source commit: `f9a8331fd1deadaef45c02d7399ac116562bac4e`
- Current external score: no new score claimed
- Published candidate history: 4/12; archived judged baseline history: 5/12
- Publication allowed: `false` until a fresh evaluator result exists
- Official author endorsement: `false` / not claimed
- Fixed command: `uv run python repro/src/verify.py`
- Source audit: [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
- Branch map: [`branch-audit.md`](branch-audit.md)
- Commit identity: all reachable history uses `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`
- Recovery bundle SHA-256: `92f82c40b76686d8d9e327d70a63273e76d8b8866eb25298c0cc4b88c557c4f4`

Claim 5’s exact arithmetic core passes but its fixed rational router remains
unresolved. Claim 6 has an extensive release/checkpoint audit but lacks the
paper’s faithful five-model training package. Neither blocked claim is silently
promoted to a pass.
