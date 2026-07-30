"""Exact efficient evaluator for the sole released DGC checkpoint."""
from __future__ import annotations

import math

import torch

from claim6_release_audit import SPLITS

PAPER_TRANSFORMER = {
    "id_1_100": 0.9560,
    "ood_101_200": 0.6820,
    "ood_201_300": 0.6215,
}
TOKEN_IDS = {"-": 1, "0": 2, "1": 3, ";": 4, "T": 5}
HEADS = 4


def tensors(state):
    prefix = "inner.transformer_encoder.layers.0.self_attn.linears"
    model = {
        "embedding": state["inner.encoder.weight"],
        "position": state["inner.pos_encoder.pe"][:, 0],
        "query": state[f"{prefix}.0.weight"],
        "key": state[f"{prefix}.1.weight"],
        "value": state[f"{prefix}.2.weight"],
        "output": state[f"{prefix}.3.weight"],
        "decoder": state["inner.decoder.weight"],
    }
    scaled_embedding = model["embedding"] * math.sqrt(model["embedding"].shape[1])
    for name in ("query", "key", "value"):
        model[f"token_{name}"] = scaled_embedding @ model[name].T
        model[f"position_{name}"] = model["position"] @ model[name].T
    return model


def encode(text):
    return [TOKEN_IDS[character] for character in text.rstrip("\n")] + [TOKEN_IDS["T"]]


def efficient_logits(token_rows, model):
    lengths = torch.tensor([len(row) for row in token_rows], dtype=torch.long)
    width = int(lengths.max())
    tokens = torch.zeros((len(token_rows), width), dtype=torch.long)
    for index, row in enumerate(token_rows):
        tokens[index, :len(row)] = torch.tensor(row)

    dimension = model["embedding"].shape[1]
    head_dimension = dimension // HEADS
    query = (
        model["token_query"][TOKEN_IDS["T"]]
        + model["position_query"][lengths - 1]
    ).view(len(token_rows), HEADS, head_dimension)
    key = (
        model["token_key"][tokens]
        + model["position_key"][:width].unsqueeze(0)
    ).view(
        len(token_rows), width, HEADS, head_dimension
    )
    value = (
        model["token_value"][tokens]
        + model["position_value"][:width].unsqueeze(0)
    ).view(
        len(token_rows), width, HEADS, head_dimension
    )
    scores = torch.einsum("bhd,bthd->bht", query, key) / math.sqrt(head_dimension)
    padding = torch.arange(width).unsqueeze(0) >= lengths.unsqueeze(1)
    scores = scores.masked_fill(padding.unsqueeze(1), float("-inf"))
    attention = torch.softmax(scores, dim=-1)
    context = torch.einsum("bht,bthd->bhd", attention, value).reshape(
        len(token_rows), dimension
    )
    attended = context @ model["output"].T
    return (attended @ model["decoder"].T).squeeze(1)


def quadratic_source_logits(token_rows, model):
    outputs = []
    dimension = model["embedding"].shape[1]
    head_dimension = dimension // HEADS
    for row in token_rows:
        tokens = torch.tensor(row)
        hidden = (
            model["embedding"][tokens] * math.sqrt(dimension)
            + model["position"][:len(row)]
        )
        query = (hidden @ model["query"].T).view(len(row), HEADS, head_dimension)
        key = (hidden @ model["key"].T).view(len(row), HEADS, head_dimension)
        value = (hidden @ model["value"].T).view(len(row), HEADS, head_dimension)
        scores = torch.einsum("thd,shd->hts", query, key) / math.sqrt(head_dimension)
        causal = torch.triu(
            torch.ones((len(row), len(row)), dtype=torch.bool),
            diagonal=1,
        )
        scores = scores.masked_fill(causal.unsqueeze(0), float("-inf"))
        attention = torch.softmax(scores, dim=-1)
        context = torch.einsum("hts,shd->thd", attention, value).reshape(
            len(row), dimension
        )
        attended = context @ model["output"].T
        outputs.append((attended[-1] @ model["decoder"].T).squeeze())
    return torch.stack(outputs)


def wilson_interval(correct, total, z=1.959963984540054):
    proportion = correct / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    radius = (
        z
        * math.sqrt(
            proportion * (1 - proportion) / total
            + z * z / (4 * total * total)
        )
        / denominator
    )
    return [center - radius, center + radius]


def evaluate_split(source_path, target_path, model, batch_size=256):
    total = 0
    correct = 0
    token_rows = []
    labels = []

    def consume():
        nonlocal total, correct
        if not token_rows:
            return
        logits = efficient_logits(token_rows, model)
        predictions = (logits >= 0).to(torch.long)
        expected = torch.tensor(labels)
        correct += int((predictions == expected).sum())
        total += len(labels)
        token_rows.clear()
        labels.clear()

    with source_path.open() as sources, target_path.open() as targets:
        for source_line, target_line in zip(sources, targets, strict=True):
            token_rows.append(encode(source_line))
            labels.append(int(target_line))
            if len(token_rows) == batch_size:
                consume()
    consume()
    return {
        "examples": total,
        "correct": correct,
        "accuracy": correct / total,
        "wilson_95": wilson_interval(correct, total),
    }


def check(local_files):
    checkpoint_path = local_files[
        "dgc/data/n100/checkpoints/best_model_SAN-Simple_RNN_RELU.pt"
    ]
    state = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    model = tensors(state)

    controls = [
        encode("0;0-1;1"),
        encode("0;1-10;10"),
        encode("0;0-10;1-10;10"),
        encode("0;0-1;1-10;10"),
    ]
    efficient = efficient_logits(controls, model)
    quadratic = quadratic_source_logits(controls, model)
    max_difference = float((efficient - quadratic).abs().max())
    if max_difference > 1e-5:
        raise AssertionError("efficient checkpoint evaluator differs from source algebra")

    results = {}
    for split_name, (source_name, target_name) in SPLITS.items():
        if split_name == "train":
            continue
        row = evaluate_split(local_files[source_name], local_files[target_name], model)
        row["paper_transformer_accuracy"] = PAPER_TRANSFORMER[split_name]
        row["absolute_difference"] = abs(
            row["accuracy"] - PAPER_TRANSFORMER[split_name]
        )
        results[split_name] = row

    # An inverted decoder is a parameter-level negative control that must
    # invert every nonzero released prediction.
    inverted = dict(model)
    inverted["decoder"] = -model["decoder"]
    original = efficient_logits(controls, model)
    corrupted = efficient_logits(controls, inverted)
    if not torch.equal(original, -corrupted):
        raise AssertionError("inverted-decoder control did not negate logits")

    return {
        "passed": True,
        "model": "released one-layer SAN-Simple checkpoint",
        "heads": HEADS,
        "efficient_vs_quadratic_max_abs_logit_difference": max_difference,
        "splits": results,
        "negative_control": {
            "name": "invert the released decoder",
            "expected": "negate every control logit",
            "observed": "negated every control logit",
        },
    }
