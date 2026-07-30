"""Qualify candidate counterevidence against the exact Figure 2 assumptions."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

AUTHOR_COMMIT = "e6d2832c0be35b93630a094124ae8dbabcbfb18d"
API_BASE = "https://arg-git.informatik.uni-kl.de/api/v4/projects/pub%2FLinearRNN"
USER_AGENT = "OpenResearch-Reproduction/1.0 (arXiv 2603.03612)"

REQUIRED_IDENTITIES = (
    "released_dataset_identity",
    "figure_model_row_identity",
    "figure_checkpoint_identity",
    "figure_training_protocol_identity",
    "stochastic_run_identity",
)


def fetch_json(path, parameters):
    query = urllib.parse.urlencode(parameters)
    request = urllib.request.Request(
        f"{API_BASE}/{path}?{query}",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def release_inventory():
    entries = []
    page = 1
    while True:
        batch = fetch_json(
            "repository/tree",
            {
                "ref": AUTHOR_COMMIT,
                "recursive": "true",
                "per_page": 100,
                "page": page,
            },
        )
        if not batch:
            break
        entries.extend(batch)
        page += 1
    commits = fetch_json(
        "repository/commits",
        {"ref_name": AUTHOR_COMMIT, "per_page": 100},
    )
    paths = {entry["path"] for entry in entries}
    if len(entries) != 170 or sum(entry["type"] == "blob" for entry in entries) != 152:
        raise AssertionError("author release inventory changed")
    if [commit["id"] for commit in commits] != [
        AUTHOR_COMMIT,
        "85a41acb56bfcb571c2a4105f916f90207bd669b",
    ]:
        raise AssertionError("author release history changed")
    absent = {
        name: name not in paths
        for name in (
            "requirements.txt",
            "pyproject.toml",
            "environment.yml",
            "uv.lock",
            "dgc/mamba.sh",
        )
    }
    if not all(absent.values()):
        raise AssertionError("a previously absent release input now exists")
    checkpoints = sorted(
        path for path in paths if path.startswith("dgc/") and path.endswith(".pt")
    )
    if checkpoints != [
        "dgc/data/n100/checkpoints/best_model_SAN-Simple_RNN_RELU.pt"
    ]:
        raise AssertionError("DGC checkpoint inventory changed")
    return {
        "tree_entries": len(entries),
        "blobs": sum(entry["type"] == "blob" for entry in entries),
        "commit_count": len(commits),
        "commit_ids": [commit["id"] for commit in commits],
        "absent_reproducibility_inputs": absent,
        "dgc_checkpoints": checkpoints,
    }


def contains_all(text, fragments):
    missing = [fragment for fragment in fragments if fragment not in text]
    if missing:
        raise AssertionError(f"released launcher changed; missing {missing}")


def protocol_audit(local_files):
    launchers = {
        name: local_files[f"dgc/{name}.sh"].read_text()
        for name in ("rnn", "transformer", "delta", "rwkv")
    }
    contains_all(
        launchers["rnn"],
        ("--max_steps 30000", "--batch_size 256", "--emb_dim 128",
         "--hidden 256", "--layers 1", "--lr 3e-4"),
    )
    contains_all(
        launchers["transformer"],
        ("--max_steps 30000", "--batch_size 64", "--emb_dim 64",
         "--nhead 2", "--layers 1", "--ff_dim 32", "--lr 3e-4"),
    )
    contains_all(
        launchers["delta"],
        ("--max_steps 30000", "--batch_size 128", "--emb_dim 128",
         "--hidden_size 256", "--layers 1", "--num_heads 4"),
    )
    contains_all(
        launchers["rwkv"],
        ("--max_steps 30000", "--batch_size 64", "--emb_dim 128",
         "--hidden 256", "--rwkv7_depth 2", "--lr 3e-5"),
    )
    mamba = local_files["dgc/train_mamba.py"].read_text()
    contains_all(
        mamba,
        ('default=30000', 'default=256', 'default=4', 'default=16',
         "from mamba_ssm.modules.mamba_simple import Mamba"),
    )
    return {
        "paper_main": {
            "batch_size": 64,
            "learning_rate": 1e-4,
            "weight_decay": 1e-4,
            "max_steps": 60000,
        },
        "paper_appendix": {
            "batch_size": 128,
            "learning_rate": 3e-4,
            "model_dimension": 256,
            "layers": 2,
            "max_steps": 60000,
            "transformer_heads": 4,
            "mamba_state": 128,
        },
        "released_launchers": {
            "RNN": "batch=256, emb=128, hidden=256, layers=1, lr=3e-4, steps=30000",
            "Transformer": "batch=64, emb=64, heads=2, layers=1, ff=32, lr=3e-4, steps=30000",
            "DeltaNet": "batch=128, emb=128, hidden=256, layers=1, heads=4, steps=30000",
            "RWKV-7": "batch=64, emb=128, hidden=256, layers=2, lr=3e-5, steps=30000",
            "Mamba": "no DGC launcher; script defaults batch=256, layers=4, state=16, steps=30000",
        },
        "paper_internal_conflicts": [
            "main batch 64 versus appendix batch 128",
            "main learning rate 1e-4 versus appendix 3e-4",
        ],
        "release_conflicts": [
            "all available launch paths cap at 30000 rather than 60000 steps",
            "RNN, Transformer, DeltaNet, and Mamba dimensions or depths differ from the appendix",
            "no DGC Mamba launcher fixes a command",
        ],
    }


def qualifies(candidate):
    return all(candidate[identity] for identity in REQUIRED_IDENTITIES)


def falsification_qualification():
    candidates = {
        "released_checkpoint_divergence": {
            "released_dataset_identity": True,
            "figure_model_row_identity": True,
            "figure_checkpoint_identity": False,
            "figure_training_protocol_identity": False,
            "stochastic_run_identity": False,
        },
        "repaired_generator_shortcut_collapse": {
            "released_dataset_identity": False,
            "figure_model_row_identity": False,
            "figure_checkpoint_identity": False,
            "figure_training_protocol_identity": False,
            "stochastic_run_identity": False,
        },
        "released_endpoint_rule": {
            "released_dataset_identity": True,
            "figure_model_row_identity": False,
            "figure_checkpoint_identity": False,
            "figure_training_protocol_identity": False,
            "stochastic_run_identity": False,
        },
    }
    accepted = {name: qualifies(candidate) for name, candidate in candidates.items()}
    if any(accepted.values()):
        raise AssertionError("assumption-breaking evidence was accepted as falsification")

    # Meta-control: the qualifier itself must accept a fully identified result.
    complete_control = {identity: True for identity in REQUIRED_IDENTITIES}
    if not qualifies(complete_control):
        raise AssertionError("qualification checker rejected complete evidence")
    return {
        "required_identities": list(REQUIRED_IDENTITIES),
        "candidates": candidates,
        "accepted_as_falsification": accepted,
        "negative_control": {
            "name": "available checkpoint divergence with no Figure 2 checkpoint identity",
            "expected": "rejected as a valid falsification",
            "observed": "rejected",
        },
        "checker_control": {
            "name": "synthetic fully identified result",
            "expected": "accepted by qualifier",
            "observed": "accepted",
        },
        "falsification_succeeded": False,
    }


def check(local_files):
    return {
        "passed": True,
        "exact_claim": (
            "Under the Figure 2 DGC dataset and training protocol, the five named "
            "model rows attain the displayed three-bin accuracies and only the "
            "nonlinear RNN maintains near-perfect length generalization."
        ),
        "domain": "the finite Figure 2 DGC train/validation/test protocol",
        "quantifiers": (
            "five named architectures, three finite length bins, and the "
            "unreported stochastic run or aggregation represented by Figure 2"
        ),
        "assumptions": list(REQUIRED_IDENTITIES),
        "release_inventory": release_inventory(),
        "protocol_audit": protocol_audit(local_files),
        "qualification": falsification_qualification(),
        "status": "did_not_falsify",
        "blocker": (
            "No available result has Figure 2 checkpoint, training-protocol, "
            "and stochastic-run identity; the paper and release do not define "
            "one consistent reproducible five-model protocol."
        ),
    }
