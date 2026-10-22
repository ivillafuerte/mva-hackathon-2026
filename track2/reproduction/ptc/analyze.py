#!/usr/bin/env python3
"""Context-matched audit of BUB1B L737* readthrough evidence.

This script does not predict clinical efficacy. It extracts the nearest measured
UGA contexts from Supplementary Table 3 of Toledano et al. (2024) and combines
them with exact genomic-coordinate predictions previously streamed from the
authors' RTDetective Figshare resource.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from pathlib import Path

import openpyxl


TARGET = "gagagt"  # three bases before + three bases after UGA


def parse_value(value):
    text = str(value).strip()
    if text in {"", "None", "NA", "nan"}:
        return None, False
    censored = text.startswith(">")
    try:
        return float(text.lstrip("<>= ")), censored
    except ValueError:
        return None, censored


def quantile(values, p):
    values = sorted(values)
    if not values:
        return None
    x = (len(values) - 1) * p
    lo = math.floor(x)
    hi = math.ceil(x)
    if lo == hi:
        return values[lo]
    return values[lo] + (values[hi] - values[lo]) * (x - lo)


def summary(values):
    numeric = [v for v, _ in values if v is not None]
    return {
        "n_numeric": len(numeric),
        "n_right_censored": sum(c for v, c in values if v is not None),
        "min": min(numeric) if numeric else None,
        "q1": quantile(numeric, 0.25),
        "median": quantile(numeric, 0.5),
        "q3": quantile(numeric, 0.75),
        "max": max(numeric) if numeric else None,
    }


def load_predictions(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workbook", required=True, type=Path)
    parser.add_argument("--predictions", default=Path("prediction_extracts.tsv"), type=Path)
    parser.add_argument("--outdir", default=Path("results"), type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    workbook_hash = hashlib.sha256(args.workbook.read_bytes()).hexdigest()
    wb = openpyxl.load_workbook(args.workbook, read_only=True, data_only=True)
    ws = wb["Supp_Table 3"]
    rows = ws.iter_rows(values_only=True)
    headers = list(next(rows))
    headers[0], headers[1] = "unnamed_0", "unnamed_1"

    records = []
    bub1b_rows = []
    for row in rows:
        rec = dict(zip(headers, row))
        for key in ("stop_type", "up_123nt", "down_123nt"):
            rec[key] = str(rec[key]).lower()
        if rec.get("GENEINFO") == "BUB1B":
            bub1b_rows.append(rec.get("mutation_identifier"))
        if rec["stop_type"] != "tga":
            continue
        context = rec["up_123nt"] + rec["down_123nt"]
        if len(context) != 6:
            continue
        rec["context_6nt"] = context
        rec["hamming_distance"] = sum(a != b for a, b in zip(context, TARGET))
        rec["gentamicin_numeric"], rec["gentamicin_right_censored"] = parse_value(rec["Gentamicin"])
        rec["untreated_numeric"], rec["untreated_right_censored"] = parse_value(rec["Untreated"])
        records.append(rec)

    exact = [r for r in records if r["hamming_distance"] == 0]
    minimum_distance = min(r["hamming_distance"] for r in records)
    nearest = [r for r in records if r["hamming_distance"] == minimum_distance]
    nearest.sort(key=lambda r: (-(r["gentamicin_numeric"] or -1), str(r["mutation_identifier"])))

    with (args.outdir / "nearest_contexts.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = [
            "GENEINFO", "mutation_identifier", "context_6nt", "hamming_distance",
            "Gentamicin", "Untreated", "G418", "Clitocine", "DAP", "SJ6986", "SRI"
        ]
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(nearest)

    gent_values = [(r["gentamicin_numeric"], r["gentamicin_right_censored"]) for r in nearest]
    untreated_values = [(r["untreated_numeric"], r["untreated_right_censored"]) for r in nearest]
    paired_deltas = [
        r["gentamicin_numeric"] - r["untreated_numeric"]
        for r in nearest
        if r["gentamicin_numeric"] is not None and r["untreated_numeric"] is not None
    ]

    predictions = load_predictions(args.predictions)
    supported = [p for p in predictions if p["model_status"] == "supported_six_drug_model"]
    excluded = [p for p in predictions if p["model_status"] != "supported_six_drug_model"]
    supported.sort(key=lambda p: -float(p["predicted_readthrough_percent"]))

    results = {
        "analysis_id": "L737_RT_CONTEXT_GATE_2026-10-09",
        "source_workbook_sha256": workbook_hash,
        "exact_measured_6nt_context_matches": len(exact),
        "nearest_measured_context_hamming_distance": minimum_distance,
        "nearest_measured_context_count": len(nearest),
        "nearest_context_gentamicin_percent": summary(gent_values),
        "nearest_context_untreated_percent": summary(untreated_values),
        "nearest_context_paired_delta_percentage_points": summary([(v, False) for v in paired_deltas]),
        "bub1b_variants_in_measured_table": sorted(set(bub1b_rows)),
        "l737star_present_in_measured_table": any("L737" in str(x) for x in bub1b_rows),
        "exact_coordinate_predictions_supported_models": supported,
        "exact_coordinate_predictions_excluded_low_signal_models": excluded,
        "decision": {
            "gentamicin_plus_mefloquine": "retain_as_low-priority_experimental_branch_only",
            "reason": [
                "No exact BUB1B L737* measurement was found in the 5,837-PTC experimental table.",
                "No exact six-nucleotide flanking-context match was present in that table.",
                "Nearest measured contexts showed only a small median gentamicin-minus-untreated increment.",
                "The gentamicin predictive model was excluded from the paper's six supported models because of low signal.",
                "Mefloquine combination evidence comes from other genes and does not model endogenous BUB1B NMD or BUBR1 function."
            ],
            "nonapproved_positive_controls": ["DAP", "SJ6986", "Clitocine", "SRI"],
            "clinical_claim": "none"
        }
    }
    (args.outdir / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
