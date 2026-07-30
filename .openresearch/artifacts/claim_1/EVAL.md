# Claim 1 evaluation

Command: `uv run python repro/src/verify.py`

Expected current verdict after a successful run: `VERIFIED`, scoped to the
exact contract in `claim_contract.json`.

The result is not based on increasing the toy sweep. The universal part is the
parametric affine-monoid derivation and balanced-tree resource recurrence.
The independent finite checker and boundary cases are defenses against
implementation errors.
