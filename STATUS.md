# Status — ICML 2026 linear RNN parallelism

**State: CURRENT EVIDENCE COMPLETE — C1–C4 verified, C5–C6 blocked.**

- Paper: [arXiv:2603.03612](https://arxiv.org/abs/2603.03612)
- Authors: William Merrill, Hongjian Jiang, Yanhong Li, Anthony Lin, Ashish Sabharwal
- Current run: `evidence/current/formal_run.json`
- Current run ID: `18bcc462-fbed-4e4b-8af2-9295100aff38`
- Current scientific source commit: `f9a8331fd1deadaef45c02d7399ac116562bac4e`
- Current external score: no new score claimed
- Published candidate history: 4/12; archived judged baseline history: 5/12
- Fixed command: `uv run python repro/src/verify.py`
- Source audit: [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
- Branch map: [`branch-audit.md`](branch-audit.md)

Claim 5’s exact arithmetic core passes but its fixed rational router remains
unresolved. Claim 6 has an extensive release/checkpoint audit but lacks the
paper’s faithful five-model training package. Neither blocked claim is silently
promoted to a pass.
