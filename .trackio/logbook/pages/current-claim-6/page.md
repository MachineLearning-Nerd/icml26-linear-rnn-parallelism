# Current verification - Claim 6

**Current verdict: BLOCKED after routes 1-2 of 4.**

## Exact claim and paper values

Figure 2 reports that only the nonlinear RNN generalizes well on deterministic
graph connectivity:

| Model | 1-100 | 101-200 | 201-300 |
| --- | ---: | ---: | ---: |
| RNN | 100.00% | 98.60% | 96.50% |
| RWKV-7 | 100.00% | 82.23% | 72.44% |
| DeltaNet | 77.87% | 57.39% | 50.00% |
| Mamba | 74.99% | 73.95% | 50.95% |
| Transformer | 95.60% | 68.20% | 62.15% |

Paper archive SHA-256:
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.
Primary released code commit:
`e6d2832c0be35b93630a094124ae8dbabcbfb18d`.

## Route 1 - exact released-artifact audit

The current verifier downloads the four exact released splits, five model
scripts, generator, RNN launcher, and sole checkpoint. Git blob IDs make the
download fail closed.

Every released label is checked with both pointer traversal and breadth-first
search. The verifier also evaluates a non-reachability endpoint signature:
`edge_out_of_source AND edge_into_target`.

The source audit found:

- the Bernoulli bucket assignment is unreachable because every bucket is
  initialized to zero before the `not 0 and not 1` guard;
- the RNN launcher passes unsupported `--post_act_clip` and `--tf32` flags;
- the RNN script's final evaluation passes an unsupported `amp` argument;
- the only DGC checkpoint, named `best_model_SAN-Simple_RNN_RELU.pt`, contains
  one-layer self-attention tensors and no RNN tensors.

The terminal release audit checked 190,000 examples. Reachability and the
endpoint-only signature were both exactly 100% accurate on all four splits.
The run used Hugging Face `cpu-upgrade`, exposed 64 logical CPUs, took
39.959394 seconds in the verifier, and completed in 63 seconds.

## Route 2 - exact released-checkpoint evaluation

The only released DGC checkpoint is evaluated as the one-layer, four-head
`SAN-Simple` architecture encoded by its tensor names and launcher. An exact
last-query evaluator avoids unnecessary quadratic attention work; it must first
match a separate quadratic implementation on deterministic controls.

All 90,000 released validation examples are evaluated and compared to the
Transformer row of Figure 2. Exact accuracies and intervals are pending this
node's terminal run.

## Why this does not resolve Claim 6

The audits are direct evidence about the public release and its sole checkpoint.
They are not a faithful five-model neural training run. Claim 6 therefore
remains `BLOCKED`.

## Reproduction

```bash
uv run python repro/src/verify.py
```

Current verifier:

- `repro/src/claim6_proof.py`
- `repro/src/claim6_release_audit.py`
- `.openresearch/artifacts/claim_6/claim_contract.json`

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Current Claim 5 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | This page | Yes | Pending terminal run | Author commit | Yes | Yes | Yes | BLOCKED |
