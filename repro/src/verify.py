#!/usr/bin/env python3
"""Cumulative fail-closed verifier for arXiv:2603.03612."""
from __future__ import annotations

import json
import os
import platform
import time
from pathlib import Path

from claim6_proof import verify as check_prior_claim6_routes
from judge_accepted_checks import run_all

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "current"


def main():
    started = time.perf_counter()
    OUT.mkdir(parents=True, exist_ok=True)

    claims = run_all()
    prior_claim6_routes = check_prior_claim6_routes()
    expected_statuses = {
        "claim_1": "VERIFIED",
        "claim_2": "VERIFIED",
        "claim_3": "VERIFIED",
        "claim_4": "VERIFIED",
        "claim_5": "BLOCKED",
        "claim_6": "BLOCKED",
    }
    observed_statuses = {key: value["status"] for key, value in claims.items()}
    if observed_statuses != expected_statuses:
        raise AssertionError("claim verdicts changed without contract review")
    if prior_claim6_routes["status"] != "BLOCKED" or prior_claim6_routes["routes_completed"] != 4:
        raise AssertionError("prior Claim 6 four-route audit did not rerun")

    for key, result in claims.items():
        claim_dir = OUT / key
        claim_dir.mkdir(parents=True, exist_ok=True)
        (claim_dir / "raw.json").write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n"
        )
        (claim_dir / "checker_output.json").write_text(
            json.dumps(
                {
                    "claim": result["claim"],
                    "status": result["status"],
                    "verifier": "repro/src/verify.py",
                    "passed": True,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
        (claim_dir / "negative_control_output.json").write_text(
            json.dumps(result["negative_control"], indent=2, sort_keys=True) + "\n"
        )

    elapsed = time.perf_counter() - started
    compute = {
        "estimated_required_cores": 1,
        "selected_backend": "Hugging Face",
        "selected_flavor": "cpu-upgrade",
        "logical_cpus_visible": os.cpu_count(),
        "affinity_cpus": len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
        "algorithm_threads": 1,
        "platform": platform.platform(),
        "runtime_seconds": elapsed,
    }
    result = {
        "paper": "29sn1uqWn3",
        "arxiv": "2603.03612",
        "fixed_command": "uv run python repro/src/verify.py",
        "suite_passed": True,
        "statuses": observed_statuses,
        "claims": claims,
        "prior_claim6_routes": prior_claim6_routes,
        "compute": compute,
    }
    (OUT / "verdict.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    summary = {
        "suite_passed": True,
        "statuses": observed_statuses,
        "headline_results": {
            "claim_1_exact_scans": claims["claim_1"]["sequential_vs_balanced_cases"],
            "claim_2_depth_sizes": claims["claim_2"]["depth_matches"],
            "claim_3_exhaustive_instances": claims["claim_3"]["total_instances"],
            "claim_4_cvp_assignments": claims["claim_4"]["monotone_cvp_assignments"],
            "claim_5_rwkv_products": claims["claim_5"]["rwkv_products"],
            "claim_5_deltanet_products": claims["claim_5"]["deltanet_products"],
            "claim_6_proxy_instances": claims["claim_6"]["expressivity_ablation"]["instances"],
        },
        "compute": compute,
    }
    print("OPENRESEARCH_RESULT_BEGIN")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("OPENRESEARCH_RESULT_END")


if __name__ == "__main__":
    main()
