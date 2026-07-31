# Reproduction command ledger

This ledger records the consequential commands that establish the experiment
tree, scientific evidence, candidate, and publication. Read-only inspection
commands (`rg`, `sed`, `find`, `git status`, `git diff`) are omitted because
they do not alter or generate evidence.

## Startup and source

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx skill orx-reports
orx projects --json
orx runs e1b77701-0696-4e55-927e-a0011dde9e96
curl -L -A 'OpenResearch-Reproduction/1.0 (arXiv 2603.03612)' https://export.arxiv.org/e-print/2603.03612
uv lock
```

## Fixed scientific command

Every successful formal node ran:

```bash
uv run python repro/src/verify.py
```

Every Hugging Face launch used:

```bash
orx exp run <experiment-id> --flavor cpu-upgrade --timeout 30m --image 'ghcr.io/astral-sh/uv@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58'
orx exp wait <experiment-id> --timeout 480
orx logs <run-id>
```

The successful run IDs, in lineage order, are:

```text
b8b84ad5-d394-408a-aa8b-76e4ab1214bc
0010393c-cfa3-406f-b00a-62f3530b7bd8
5b01911b-996a-48c2-bca1-015477c22888
f5341b8c-3fbd-4b7e-8e05-30c5fe3740a9
8f632753-ee79-42cf-9efb-382708f42638
b147fc79-8d1f-4ddf-811b-254196e18d9e
2237e33d-1712-4233-9367-e1c263516239
614b8914-1f6d-49e3-8ee4-751bd61d8c96
1870e050-4855-4cff-90ed-a16ddf7de3d1
3722216e-11a8-4b94-8c21-80922a99e902
18bcc462-fbed-4e4b-8af2-9295100aff38
```

Release-candidate attempts stopped before producing scientific output:

```text
313534bd-4a73-4816-a795-ab3218a398de  superseded before execution by release-path correction
5bbb5800-20d9-4972-9570-f12401558a5f  superseded before execution by release-count correction
4744e432-bb59-43c2-86fd-3115cdd694a1  superseded before execution by candidate-local link correction
2b2c0509-f824-47ce-8b29-62186129813b  infrastructure failure: invalid container digest; no code executed
2b8f82dd-b1f4-4a0b-a602-4961f9b63be2  stopped during final blind-review provenance correction
```

## Local short validations

```bash
uv run python -m py_compile repro/src/claim6_falsification.py repro/src/claim6_proof.py repro/src/claim6_release_audit.py repro/src/verify.py
uv run marimo check notebooks/linear_rnn_reproduction.py
xmllint --noout reports/linear-rnn-reproduction/images/*.svg
uv add --dev playwright
uv run playwright install chromium
uv run python /tmp/Posterly/tools/poster_check.py pack poster_embed.html
uv run python /tmp/Posterly/tools/run_gates.py poster_embed.html --tokens design_tokens.json --report GATE_REPORT.json
uv run python /tmp/Posterly/tools/render_preview.py poster_embed.html
python3 /tmp/validate_icml_logbook.py --space DineshAI/repro-why-are-linear-rnns-more-parallelizable
release/build_candidate.sh <judged-dir> <fresh-candidate-dir> <allowlist> <manifest>
uv run python repro/src/audit_space_candidate.py <candidate-dir> <judged-dir> <allowlist>
```

## Publication

The exact text-only Hugging Face commit and GitHub mirroring commands are added
to the post-publication record after their returned revisions are known. No
second Space is created.
