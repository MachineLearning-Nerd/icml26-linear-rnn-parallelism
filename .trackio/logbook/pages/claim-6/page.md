# Claim 6 — Figure 2 generalization

## Current formal regression

**Verdict: BLOCKED on Figure 2 training.** A constructive nonlinear RNN is
900/900 in each of the 1–100, 101–200, and 201–300 bands. On the complete
29,367-instance graph domain it is 29,367/29,367; removing integer-exact ReLU
zero tests yields 24,085/29,367 (82.0138%), below the 24,328/29,367 majority
baseline (82.8413%). This is an expressivity ablation, not the missing
five-model training comparison.

[Current verifier](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/blob/main/repro/src/verify.py) ·
[implementation](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/blob/main/repro/src/judge_accepted_checks.py) ·
[raw](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/blob/main/evidence/current/claim_6/raw.json) ·
[checker](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/blob/main/evidence/current/claim_6/checker_output.json) ·
[control](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/blob/main/evidence/current/claim_6/negative_control_output.json)

**Current verdict: BLOCKED after all four required routes.**

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

All 90,000 released validation examples were evaluated:

| Split | Released checkpoint | Figure 2 Transformer | Absolute gap |
| --- | ---: | ---: | ---: |
| 1-100 | 52.52% | 95.60% | 43.08 points |
| 101-200 | 50.0167% | 68.20% | 18.1833 points |
| 201-300 | 50.8867% | 62.15% | 11.2633 points |

The efficient and quadratic evaluators agree within `2.98e-8`. The terminal
run used 64 logical CPUs, took 213.398840 seconds in the verifier, and completed
in 238 seconds.

## Route 3 - generator repair sensitivity

Only the impossible sentinel is repaired: interior vertices start unassigned
rather than in bucket zero. The paper's 10,000-example test-bin scale is
regenerated for `p` in `{0.1, 0.5, 0.9}` and seeds `0`, `1`, and `260303612`.
Every label must still equal graph reachability. The endpoint shortcut is
measured against a matched control that restores the released bug.

The terminal run checked 270,000 examples. Every label matched independent
reachability. The endpoint-only accuracy ranged from 50.00% to 54.83%; both
OOD bins were exactly 50.00% in every configuration. Restoring the released bug
returned 100% endpoint accuracy (95% Wilson lower bound 99.9616%). The run used
Hugging Face `cpu-upgrade`, exposed 64 logical CPUs, took 222.060673 seconds in
the verifier, and completed in 249 seconds.

## Route 4 - exact-assumption falsification qualification

The exact Figure 2 statement is a five-model, three-bin result under one finite
training protocol. A counterexample qualifies only when released-dataset,
model-row, Figure-checkpoint, training-protocol, and stochastic-run identity
all hold.

The verifier inventories all 170 paths and both commits at the pinned author
revision. It confirms one DGC checkpoint, no dependency lock, and no DGC Mamba
launcher. It also checks these incompatible protocols:

| Source | Batch | LR | Layers/steps |
| --- | ---: | ---: | --- |
| Main text | 64 | 1e-4 | 60,000 steps |
| Appendix | 128 | 3e-4 | 2 layers, 60,000 steps |
| Released RNN | 256 | 3e-4 | 1 layer, 30,000 steps |
| Released Transformer | 64 | 3e-4 | 1 layer, 30,000 steps |
| Released DeltaNet | 128 | default 3e-4 | 1 layer, 30,000 steps |
| Released RWKV-7 | 64 | 3e-5 | 2 layers, 30,000 steps |
| Released Mamba | no launcher | script default 3e-4 | 4 layers, 30,000 steps |

The released-checkpoint divergence, repaired-generator result, and endpoint
rule are each rejected as valid falsifications because they violate at least
one required identity. A fully identified meta-control is accepted. No valid
counterexample is available, so the mandatory fourth route does not falsify
the claim.

## Why this does not resolve Claim 6

The audits are direct evidence about the public release and its sole checkpoint.
They are not a faithful five-model neural training run. The exact Figure
checkpoints, seeds, logs, locked environment, and one consistent protocol are
missing. Claim 6 therefore remains `BLOCKED`, not `VERIFIED` or `FALSIFIED`.

## Reproduction

```bash
uv run python repro/src/verify.py
```

Evaluator-visible current verifier and records:

- [cumulative proof checker](../../repro/src/claim6_proof.py)
- [release audit](../../repro/src/claim6_release_audit.py)
- [checkpoint evaluator](../../repro/src/claim6_checkpoint_eval.py)
- [generator sensitivity](../../repro/src/claim6_generator_sensitivity.py)
- [falsification qualifier](../../repro/src/claim6_falsification.py)
- [claim contract](../../evidence/claim_6/claim_contract.json)
- [route 1 raw output](../../evidence/claim_6/raw_route_1.json)
- [route 2 raw output](../../evidence/claim_6/raw_route_2.json)
- [route 3 raw output](../../evidence/claim_6/raw_route_3.json)
- [route 4 raw output](../../evidence/claim_6/raw_route_4.json)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Current Claim 5 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | This page | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
