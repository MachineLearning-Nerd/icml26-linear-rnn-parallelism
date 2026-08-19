# Environment and reproduction boundary

## Locked software and command

- Python: `3.12`
- Package manager: `uv`
- Lockfile: [`uv.lock`](uv.lock)
- Fixed campaign command:

```bash
uv sync
uv run python repro/src/verify.py
```

The current formal run used one algorithm thread on Hugging Face `cpu-upgrade`,
with 64 visible and affinity CPUs, 1129.264233 seconds, and no GPU. Run ID:
`18bcc462-fbed-4e4b-8af2-9295100aff38`.

## Source and scope

- Source archive: `f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`
- Current scientific source commit: `f9a8331fd1deadaef45c02d7399ac116562bac4e`
- Current record: C1–C4 `VERIFIED_SCOPED`, C5–C6 `BLOCKED`
- GPU used: no
- Current score claimed: no

The old five-claim `outputs/` files are historical campaign provenance. The
six-claim current status is in `evidence/current/`; finite exact checks and
source-anchored reductions do not independently prove every complexity-class
quantifier.
