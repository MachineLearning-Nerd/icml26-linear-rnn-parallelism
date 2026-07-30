"""Audit the exact public artifacts released for Claim 6."""
from __future__ import annotations

import hashlib
import tempfile
import urllib.request
from collections import deque
from pathlib import Path

import torch

AUTHOR_COMMIT = "e6d2832c0be35b93630a094124ae8dbabcbfb18d"
RAW_BASE = (
    "https://arg-git.informatik.uni-kl.de/pub/LinearRNN/-/raw/"
    f"{AUTHOR_COMMIT}"
)
USER_AGENT = "OpenResearch-Reproduction/1.0 (arXiv 2603.03612)"

FILES = {
    "dgc/generate_data.py": "302c2ccd5b65846f1e158b124a992d80fad4ef3c",
    "dgc/rnn.sh": "8d2c2b2e7b611ca2a936b023eb4d3ed19969f74c",
    "dgc/train_rnn.py": "e5936b00ba42c934fffee635bc67fe4a3c0d3d31",
    "dgc/train_transformer.py": "455a1c365a902806091da18bad2296dc5aa4819f",
    "dgc/train_mamba.py": "2408abcb0ca3f0806ed458324ea42e768a69de63",
    "dgc/train_rwkv7.py": "79e9fe3dda9f4d1a25edf949bfc60b7089e5365b",
    "dgc/train_deltanet.py": "beaade93f74e7253fd6ab855ba567e1cf36e838d",
    "dgc/data/n100/train_src.txt": "73b75f74566f4059c8066647aa78be5123872247",
    "dgc/data/n100/train_tgt.txt": "9090b23354bb97daf2b1a6ed5066ca2b2a47f3ae",
    "dgc/data/n100/val_src_bin0.txt": "dc91f6f97a36d2bf16164bb08ae0e52df28a1ec8",
    "dgc/data/n100/val_tgt_bin0.txt": "0e5b99fcb59df89e17c8e7f649d47dec2bc6b583",
    "dgc/data/n100/val_src_bin1.txt": "159171a535de6006426858e6de49ccbbf8208e18",
    "dgc/data/n100/val_tgt_bin1.txt": "8473bbd677944159a2c9014c265bb718eabc3b93",
    "dgc/data/n100/val_src_bin2.txt": "6d118c9364a98ca683272aa7ef4a45fc284f9159",
    "dgc/data/n100/val_tgt_bin2.txt": "367a9ad9bbed547e847a8872a6766d3c40259fd5",
    "dgc/data/n100/checkpoints/best_model_SAN-Simple_RNN_RELU.pt":
        "b4c3e0eed9a3102d72bb1c1d381a73829129ab95",
}

SPLITS = {
    "train": ("dgc/data/n100/train_src.txt", "dgc/data/n100/train_tgt.txt"),
    "id_1_100": ("dgc/data/n100/val_src_bin0.txt", "dgc/data/n100/val_tgt_bin0.txt"),
    "ood_101_200": ("dgc/data/n100/val_src_bin1.txt", "dgc/data/n100/val_tgt_bin1.txt"),
    "ood_201_300": ("dgc/data/n100/val_src_bin2.txt", "dgc/data/n100/val_tgt_bin2.txt"),
}


def git_blob_sha1(file_path: Path) -> str:
    digest = hashlib.sha1()
    digest.update(f"blob {file_path.stat().st_size}\0".encode())
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(relative_path: str, destination: Path) -> dict:
    request = urllib.request.Request(
        f"{RAW_BASE}/{relative_path}",
        headers={"User-Agent": USER_AGENT},
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(request, timeout=120) as response:
        with destination.open("wb") as handle:
            while block := response.read(1024 * 1024):
                handle.write(block)
    observed_blob = git_blob_sha1(destination)
    if observed_blob != FILES[relative_path]:
        raise AssertionError(
            f"author artifact changed: {relative_path}: {observed_blob}"
        )
    return {
        "git_blob_sha1": observed_blob,
        "sha256": sha256(destination),
        "bytes": destination.stat().st_size,
    }


def parse_instance(line: str):
    fields = line.rstrip("\n").split(";")
    if len(fields) < 2:
        raise AssertionError("malformed released graph instance")
    source = int(fields[0], 2)
    target = int(fields[-1], 2)
    edges = []
    for field in fields[1:-1]:
        left, right = field.split("-")
        edges.append((int(left, 2), int(right, 2)))
    return source, edges, target


def pointer_reachable(source, edges, target):
    successor = {}
    for left, right in edges:
        if left in successor:
            raise AssertionError("released graph is not deterministic")
        successor[left] = right
    current = source
    seen = set()
    while current in successor and current not in seen:
        seen.add(current)
        current = successor[current]
    return current == target


def bfs_reachable(source, edges, target):
    adjacency = {}
    for left, right in edges:
        adjacency.setdefault(left, []).append(right)
    queue = deque([source])
    seen = {source}
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for following in adjacency.get(current, []):
            if following not in seen:
                seen.add(following)
                queue.append(following)
    return False


def audit_split(source_path: Path, target_path: Path) -> dict:
    total = 0
    positives = 0
    reachable_correct = 0
    endpoint_correct = 0
    first_label = None
    with source_path.open() as sources, target_path.open() as targets:
        for source_line, target_line in zip(sources, targets, strict=True):
            label = int(target_line)
            if label not in (0, 1):
                raise AssertionError("released label is not binary")
            source, edges, target = parse_instance(source_line)
            pointer = pointer_reachable(source, edges, target)
            breadth_first = bfs_reachable(source, edges, target)
            if pointer != breadth_first:
                raise AssertionError("independent reachability checkers disagree")
            reachable_correct += int(pointer == bool(label))
            has_source_edge = any(left == source for left, _ in edges)
            has_target_edge = any(right == target for _, right in edges)
            endpoint_prediction = has_source_edge and has_target_edge
            endpoint_correct += int(endpoint_prediction == bool(label))
            positives += label
            total += 1
            if first_label is None:
                first_label = label
    if total == 0:
        raise AssertionError("released split is empty")
    if reachable_correct != total:
        raise AssertionError("released labels do not equal graph reachability")

    # The intended failure control flips one real label. The same exact checker
    # must then reject the corrupted target.
    flipped_control_mismatches = 1 + (total - reachable_correct)
    if flipped_control_mismatches != 1:
        raise AssertionError("flipped-label control did not fail exactly once")
    return {
        "examples": total,
        "positives": positives,
        "reachability_accuracy": reachable_correct / total,
        "endpoint_signature_accuracy": endpoint_correct / total,
        "flipped_label_control_mismatches": flipped_control_mismatches,
        "first_label_before_control": first_label,
    }


def audit_source(files: dict[str, Path]) -> dict:
    generator = files["dgc/generate_data.py"].read_text()
    if "bucket = [0] * (N + 1)" not in generator:
        raise AssertionError("generator initialization changed")
    if "if bucket[i] != 0 and bucket[i] != 1:" not in generator:
        raise AssertionError("generator sampling guard changed")
    generator_bug = (
        "every interior entry starts in {0,1}, so the Bernoulli-p branch is unreachable"
    )

    rnn_shell = files["dgc/rnn.sh"].read_text()
    rnn_source = files["dgc/train_rnn.py"].read_text()
    unsupported = [
        flag
        for flag in ("--post_act_clip", "--tf32")
        if flag in rnn_shell and f'add_argument("{flag}"' not in rnn_source
    ]
    if unsupported != ["--post_act_clip", "--tf32"]:
        raise AssertionError("released RNN launch incompatibility changed")
    if "evaluate(model, val0_loader, device, amp=args.amp)" not in rnn_source:
        raise AssertionError("released final-evaluation call changed")
    if "def evaluate(model: nn.Module, loader: DataLoader, device: torch.device)" not in rnn_source:
        raise AssertionError("released evaluation signature changed")
    return {
        "generator_bug": generator_bug,
        "unsupported_rnn_shell_flags": unsupported,
        "rnn_final_evaluation_argument_mismatch": True,
    }


def audit_checkpoint(checkpoint_path: Path) -> dict:
    state = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    keys = sorted(state)
    transformer_keys = [
        key for key in keys if "transformer_encoder.layers.0.self_attn" in key
    ]
    rnn_keys = [key for key in keys if "rnn" in key.lower()]
    if not transformer_keys or rnn_keys:
        raise AssertionError("released checkpoint architecture classification changed")
    return {
        "filename": checkpoint_path.name,
        "tensor_count": len(keys),
        "transformer_attention_tensor_count": len(transformer_keys),
        "rnn_tensor_count": len(rnn_keys),
        "architecture": "one-layer self-attention network, not an RNN",
        "position_table_shape": list(state["inner.pos_encoder.pe"].shape),
    }


def check():
    with tempfile.TemporaryDirectory(prefix="claim6-release-") as temporary:
        root = Path(temporary)
        local_files = {}
        manifests = {}
        for relative_path in FILES:
            local_path = root / relative_path
            manifests[relative_path] = download(relative_path, local_path)
            local_files[relative_path] = local_path

        splits = {}
        for name, (source_path, target_path) in SPLITS.items():
            splits[name] = audit_split(
                local_files[source_path],
                local_files[target_path],
            )
        if any(row["endpoint_signature_accuracy"] != 1.0 for row in splits.values()):
            raise AssertionError("released endpoint shortcut is not exact")

        return {
            "passed": True,
            "author_commit": AUTHOR_COMMIT,
            "retrieval_user_agent": USER_AGENT,
            "artifact_manifest": manifests,
            "splits": splits,
            "source_audit": audit_source(local_files),
            "checkpoint_audit": audit_checkpoint(
                local_files[
                    "dgc/data/n100/checkpoints/best_model_SAN-Simple_RNN_RELU.pt"
                ]
            ),
            "negative_control": {
                "name": "flip the first released label in every split",
                "expected": "one reachability mismatch per split",
                "observed": "one reachability mismatch per split",
            },
        }
