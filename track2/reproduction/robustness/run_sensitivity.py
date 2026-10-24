#!/usr/bin/env python3
"""Additive, post-hoc exploratory finite-set diagnostics; no biological inference.

Uses only hash-verified public source bytes, never original result snapshots.
See protocol.json and its pre-execution amendment. No randomization or p-values.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import platform
import statistics as stats
import tarfile
from collections import Counter
from importlib.metadata import version
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TARGET = "gagagt"
SAMPLES = [("GSM1588051", "Pro", 1), ("GSM1588052", "Pro", 2),
           ("GSM1588053", "Qui", 1), ("GSM1588054", "Qui", 2),
           ("GSM1588055", "Rap", 1), ("GSM1588056", "Rap", 2)]
CONTRASTS = {"Rap_over_Pro": ("Rap", "Pro"), "Qui_over_Pro": ("Qui", "Pro"),
             "Rap_over_Qui": ("Rap", "Qui")}
THRESHOLDS = [0.95, 0.975, 0.99, 0.995, 1.0]
ORIGINAL_PROTOCOL_SHA = "7f22f7a108501bd0cccbd24e2a0fe76d6feec75ba118cdc1bbf9d17824fc1b78"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked_sources(root):
    manifest = json.loads((root / "input_manifest.json").read_text())
    result = []
    for item in manifest["inputs"] + manifest["bundled_public_references"]:
        path = root / item["path"]
        if sha(path) != item["sha256"]:
            raise ValueError(f"Source hash differs: {item['path']}; stop and review")
        result.append({"path": item["path"], "sha256": item["sha256"], "url": item["url"]})
    for path, expected in json.loads((root / "original_script_hashes.json").read_text()).items():
        if sha(root / path) != expected:
            raise ValueError(f"Original script changed: {path}")
    if sha(HERE / "protocol.json") != ORIGINAL_PROTOCOL_SHA:
        raise ValueError("Frozen original protocol bytes changed")
    return result


def numeric_cell(value):
    text = str(value).strip()
    if text.lower() in {"", "none", "na", "nan"}:
        return None, "missing"
    if text.startswith(("<", ">", "≤", "≥")):
        return None, "left_censored" if text[0] in {"<", "≤"} else "right_censored"
    try:
        number = float(text)
    except ValueError:
        return None, "nonnumeric"
    if not math.isfinite(number):
        return None, "nonfinite"
    return number, "observed"


def load_ptc(workbook):
    wb = openpyxl.load_workbook(workbook, read_only=True, data_only=True)
    rows = wb["Supp_Table 3"].iter_rows(values_only=True)
    headers = list(next(rows))
    records = []
    inventory = {"worksheet_rows_after_header_including_blank_formatting": 0,
                 "populated_source_rows": 0, "blank_formatted_rows": 0,
                 "valid_stop_codon_rows": 0, "UGA_rows_with_invalid_context": 0}
    for excel_row, row in enumerate(rows, 2):
        inventory["worksheet_rows_after_header_including_blank_formatting"] += 1
        if not any(value is not None for value in row):
            inventory["blank_formatted_rows"] += 1
            continue
        inventory["populated_source_rows"] += 1
        rec = dict(zip(headers, row))
        stop = str(rec["stop_type"]).lower()
        inventory["valid_stop_codon_rows"] += stop in {"tga", "taa", "tag"}
        if stop != "tga":
            continue
        context = str(rec["up_123nt"]).lower() + str(rec["down_123nt"]).lower()
        if len(context) != 6 or set(context) - set("acgt"):
            inventory["UGA_rows_with_invalid_context"] += 1
            continue
        gent, gent_status = numeric_cell(rec["Gentamicin"])
        untreated, untreated_status = numeric_cell(rec["Untreated"])
        records.append({"excel_row": excel_row, "mutation_identifier": str(rec["mutation_identifier"]),
                        "gene": str(rec["GENEINFO"]), "context_6nt": context,
                        "hamming_distance": sum(a != b for a, b in zip(context, TARGET)),
                        "gentamicin_percent": gent, "gentamicin_status": gent_status,
                        "untreated_percent": untreated, "untreated_status": untreated_status})
    wb.close()
    if not records:
        raise ValueError("No valid UGA rows")
    distance = min(r["hamming_distance"] for r in records)
    nearest = sorted((r for r in records if r["hamming_distance"] == distance),
                     key=lambda r: (r["context_6nt"], r["mutation_identifier"], r["excel_row"]))
    return records, nearest, inventory


def ptc_estimates(rows):
    if not rows:
        return {"status": "insufficient_no_rows"}
    if any(r["gentamicin_status"] != "observed" or r["untreated_status"] != "observed" for r in rows):
        return {"status": "insufficient_missing_or_censored_values"}
    gent = stats.median(r["gentamicin_percent"] for r in rows)
    untreated = stats.median(r["untreated_percent"] for r in rows)
    deltas = [r["gentamicin_percent"] - r["untreated_percent"] for r in rows]
    return {"status": "calculated", "n_variant_rows": len(rows),
            "n_unique_contexts": len({r["context_6nt"] for r in rows}),
            "gentamicin_median_percent": gent, "untreated_median_percent": untreated,
            "median_paired_delta_percentage_points": stats.median(deltas),
            "difference_of_marginal_medians_percentage_points": gent - untreated,
            "positive_paired_deltas": sum(x > 0 for x in deltas),
            "zero_paired_deltas": sum(x == 0 for x in deltas),
            "negative_paired_deltas": sum(x < 0 for x in deltas)}


def loo_range(records, field):
    values = [r[field] for r in records if r.get("status") == "calculated"]
    return {"min": min(values), "max": max(values)} if values else None


def ptc_analysis(root):
    all_rows, nearest, inventory = load_ptc(root / "ptc/supp_tables.xlsx")
    counts = Counter(r["context_6nt"] for r in nearest)
    baseline = ptc_estimates(nearest)
    result = {"target_6nt": TARGET, "complete_source_table_inventory": inventory,
              "valid_UGA_rows_in_complete_table": len(all_rows),
              "exact_6nt_rows": sum(r["hamming_distance"] == 0 for r in all_rows),
              "minimum_hamming_distance": nearest[0]["hamming_distance"],
              "nearest_variant_row_count": len(nearest), "unique_nearest_6nt_context_count": len(counts),
              "context_multiplicity": dict(sorted(counts.items())),
              "value_status_counts": {key: {status: sum(r[key] == status for r in nearest)
                                             for status in ("observed", "missing", "left_censored",
                                                            "right_censored", "nonnumeric", "nonfinite")}
                                      for key in ["gentamicin_status", "untreated_status"]},
              "baseline": baseline, "nearest_rows": nearest,
              "unit": "measured variant rows and distinct local sequence contexts, not independent patients/replicates",
              "scope": "Finite-set influence diagnostics; no exact BUB1B L737* efficacy or new experimental evidence"}
    if baseline["status"] != "calculated":
        result["interpretation"] = "insufficient: missing/censored nearest paired observations"
        return result
    row_loo = []
    for omit in nearest:
        retained = [r for r in nearest if r["excel_row"] != omit["excel_row"]]
        row_loo.append({"omitted_excel_row": omit["excel_row"],
                        "omitted_mutation_identifier": omit["mutation_identifier"],
                        "omitted_context_6nt": omit["context_6nt"], **ptc_estimates(retained)})
    group_loo = []
    context_summaries = []
    for context in sorted(counts):
        omitted = [r for r in nearest if r["context_6nt"] == context]
        retained = [r for r in nearest if r["context_6nt"] != context]
        group_loo.append({"omitted_context_6nt": context, "omitted_variant_row_count": len(omitted),
                          "omitted_excel_rows": [r["excel_row"] for r in omitted], **ptc_estimates(retained)})
        context_summaries.append({"context_6nt": context, **ptc_estimates(omitted)})
    key = "median_paired_delta_percentage_points"
    result.update({"leave_one_variant_row_out": row_loo, "leave_one_context_group_out": group_loo,
                   "within_context_summaries": context_summaries,
                   "equal_context_weighted_median_of_context_median_deltas_percentage_points":
                       stats.median(r[key] for r in context_summaries),
                   "row_leave_out_median_paired_delta_range_percentage_points": loo_range(row_loo, key),
                   "context_group_leave_out_median_paired_delta_range_percentage_points": loo_range(group_loo, key),
                   "row_leave_out_positive_median_count": sum(r[key] > 0 for r in row_loo),
                   "group_leave_out_positive_median_count": sum(r[key] > 0 for r in group_loo),
                   "range_label": "exhaustive finite-set deletion range, NOT confidence interval"})
    return result


def load_tracks(root):
    annotation = json.loads((root / "gse65145/hg19_chr15_refseq.json").read_text())
    anchors = [r for r in annotation["ncbiRefSeq"] if r["name"] == "NM_001211.6" and r["name2"] == "BUB1B"]
    if len(anchors) != 1:
        raise ValueError("Ambiguous canonical annotation")
    anchor = anchors[0]
    tracks, coords, metadata = {}, None, []
    with tarfile.open(root / "gse65145/GSE65145_RAW.tar") as archive:
        if len(archive.getmembers()) != 6:
            raise ValueError("Expected six processed public tracks")
        for gsm, condition, replicate in SAMPLES:
            name = f"{gsm}_{condition}_rep{replicate}.txt.gz"
            handle = archive.extractfile(name)
            if handle is None:
                raise ValueError(f"Missing tar member {name}")
            data = gzip.decompress(handle.read()).decode().splitlines()
            if not data[0].startswith("track type=bedGraph"):
                raise ValueError("Unexpected processed track format")
            sample_coords, values = [], []
            for line in data[1:]:
                chrom, left, right, value = line.split("\t")
                left, right, value = int(left), int(right), float(value)
                if left >= right or not math.isfinite(value) or value < 0:
                    raise ValueError("Invalid processed coordinate/value")
                sample_coords.append((chrom, left, right))
                values.append(value)
            if coords is None:
                coords = sample_coords
            elif sample_coords != coords:
                raise ValueError("Coordinate arrays differ between samples")
            titles = [line.split(" = ", 1)[1] for line in (root / f"gse65145/{gsm}.soft").read_text().splitlines()
                      if line.startswith("!Sample_title = ")]
            keyword = {"Pro": "proliferative", "Qui": "queiscent", "Rap": "rapamycin"}[condition]
            if len(titles) != 1 or keyword not in titles[0].lower() or str(replicate) not in titles[0]:
                raise ValueError("GEO sample-label check failed")
            tracks[gsm] = values
            metadata.append({"accession": gsm, "condition": condition, "replicate": replicate,
                             "title": titles[0], "deposited_rows": len(values)})
    return anchor, coords, tracks, metadata


def overlap_metrics(coordinate, anchor):
    chrom, left, right = coordinate
    start, end = anchor["txStart"], anchor["txEnd"]
    overlap = max(0, min(end, right) - max(start, left)) if chrom == anchor["chrom"] else 0
    return {"anchor_overlap_fraction": overlap / (end - start),
            "feature_overlap_fraction": overlap / (right - left),
            "overlap_bp": overlap, "boundary_distance_bp": abs(left - start) + abs(right - end)}


def eligible_feature_indices(coords, anchor, threshold):
    chosen = []
    for i, coord in enumerate(coords):
        m = overlap_metrics(coord, anchor)
        if m["anchor_overlap_fraction"] >= threshold and m["feature_overlap_fraction"] >= threshold:
            chosen.append(i)
    return sorted(chosen, key=lambda i: (overlap_metrics(coords[i], anchor)["boundary_distance_bp"], coords[i], i))


def contrasts(values_by_condition, estimator="arithmetic"):
    if any(not values for values in values_by_condition.values()):
        return {"status": "insufficient_empty_condition"}
    if estimator == "geometric" and any(v <= 0 for values in values_by_condition.values() for v in values):
        return {"status": "insufficient_nonpositive_value_for_geometric_mean"}
    mean = stats.mean if estimator == "arithmetic" else stats.geometric_mean
    means = {c: mean(values) for c, values in values_by_condition.items()}
    ratios = {key: means[a] / means[b] if means[b] > 0 else None for key, (a, b) in CONTRASTS.items()}
    return {"status": "calculated", "estimator": estimator,
            "remaining_sample_counts": {c: len(v) for c, v in values_by_condition.items()},
            "condition_means": means, "ratios": ratios,
            "log2_ratios": {k: math.log2(v) if v is not None and v > 0 else None for k, v in ratios.items()}}


def feature_record(index, coords, anchor, tracks):
    values = {condition: [tracks[gsm][index] for gsm, c, _ in SAMPLES if c == condition]
              for condition in ("Pro", "Qui", "Rap")}
    arithmetic, geometric = contrasts(values), contrasts(values, "geometric")
    cross_ratios = {}
    for name, (num, den) in CONTRASTS.items():
        pairs = [{"numerator_sample": ga, "denominator_sample": gb,
                  "ratio": tracks[ga][index] / tracks[gb][index] if tracks[gb][index] > 0 else None}
                 for ga, ca, _ in SAMPLES if ca == num for gb, cb, _ in SAMPLES if cb == den]
        numeric = [x["ratio"] for x in pairs if x["ratio"] is not None]
        cross_ratios[name] = {"values": pairs, "min": min(numeric) if numeric else None,
                              "max": max(numeric) if numeric else None,
                              "label": "all four unpaired sample ratios; NOT four biological replicates"}
    leave_out = []
    for omit, condition, _ in SAMPLES:
        reduced = {c: [tracks[gsm][index] for gsm, cc, _ in SAMPLES if cc == c and gsm != omit]
                   for c in ("Pro", "Qui", "Rap")}
        leave_out.append({"omitted_sample": omit, "omitted_condition": condition, **contrasts(reduced)})
    coord = coords[index]
    return {"track_row_1based_without_header": index + 1, "chrom": coord[0], "start_0based": coord[1],
            "end_exclusive": coord[2], **overlap_metrics(coord, anchor),
            "values_RPKM_as_deposited": values, "arithmetic": arithmetic, "geometric": geometric,
            "leave_one_sample_out": leave_out, "cross_sample_ratios": cross_ratios,
            "leave_one_sample_out_ratio_ranges": {
                key: {"min": min(r["ratios"][key] for r in leave_out),
                      "max": max(r["ratios"][key] for r in leave_out)} for key in CONTRASTS}}


def gse_analysis(root):
    anchor, coords, tracks, metadata = load_tracks(root)
    selected = {threshold: eligible_feature_indices(coords, anchor, threshold) for threshold in THRESHOLDS}
    union = sorted({i for rows in selected.values() for i in rows})
    feature_map = {i: feature_record(i, coords, anchor, tracks) for i in union}
    threshold_summaries = []
    for threshold, indices in selected.items():
        item = {"reciprocal_overlap_threshold": threshold, "qualifying_feature_count": len(indices),
                "qualifying_track_rows": [i + 1 for i in indices],
                "status": "calculated" if indices else "insufficient_no_eligible_feature"}
        if indices:
            item["ratio_ranges_across_redundant_features"] = {
                key: {"min": min(feature_map[i]["arithmetic"]["ratios"][key] for i in indices),
                      "median": stats.median(feature_map[i]["arithmetic"]["ratios"][key] for i in indices),
                      "max": max(feature_map[i]["arithmetic"]["ratios"][key] for i in indices)}
                for key in CONTRASTS}
        threshold_summaries.append(item)
    overlapping = []
    for i, coord in enumerate(coords):
        metrics = overlap_metrics(coord, anchor)
        if metrics["overlap_bp"] > 0:
            overlapping.append({"track_row_1based_without_header": i + 1, "chrom": coord[0],
                                "start_0based": coord[1], "end_exclusive": coord[2], **metrics,
                                "qualifies_at_primary_0_99": i in selected[0.99]})
    primary = feature_map[selected[0.99][0]] if selected[0.99] else None
    return {"dataset": "GSE65145", "model": "one normal 2DD fibroblast cell line; no MVA genotype",
            "samples": metadata, "sample_counts_per_condition": dict(Counter(c for _, c, _ in SAMPLES)),
            "row_count_per_track": len(coords), "locus_overlapping_row_count": len(overlapping),
            "anchor": {k: anchor[k] for k in ("name", "name2", "chrom", "txStart", "txEnd", "strand")},
            "threshold_summaries": threshold_summaries, "features": [feature_map[i] for i in union],
            "primary_feature": primary, "all_locus_overlaps_annotation_audit_only": overlapping,
            "genomewide_correlation": "not calculated per pre-run amendment 01; shared denominator could mislead",
            "replication_unit": "n=2 samples/condition, one normal cell line. Features, ratios and deletions are not additional biological replicates.",
            "scope": "BUB1B-spanning unstranded RNA features, not BUBR1 protein, mature isoform estimates or functional rescue",
            "confounding_statement": "Serum-restricted quiescence is a descriptive comparator, not a cell-cycle-matched control. No causal proliferation correction, mediator inference, p-value or CI is calculated.",
            "unresolved": "149122 deposited rows versus 149135 probes stated in paper; unchanged unresolved discrepancy"}


def write_csv(path, rows):
    if not rows:
        return
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, sort_keys=True) if isinstance(v, (dict, list)) else v for k, v in row.items()})


def interpretations(ptc, gse):
    """Machine-readable bounded decisions; never upgrade evidence to rescue."""
    ptc_calculated = ptc["baseline"]["status"] == "calculated"
    ptc_positive = ptc_calculated and all(
        row["median_paired_delta_percentage_points"] > 0
        for field in ("leave_one_variant_row_out", "leave_one_context_group_out") for row in ptc[field])
    gse_lower = bool(gse["features"]) and all(
        feature["arithmetic"]["ratios"]["Rap_over_Pro"] < 1
        and feature["geometric"].get("ratios", {}).get("Rap_over_Pro", math.inf) < 1
        and all(row["ratios"]["Rap_over_Pro"] < 1 for row in feature["leave_one_sample_out"])
        and feature["cross_sample_ratios"]["Rap_over_Pro"]["max"] < 1
        for feature in gse["features"])
    return {
        "stable": [
            {"claim": "PTC paired median direction across all specified row/group deletions",
             "status": "positive_in_all_deletions" if ptc_positive else "not_established",
             "scope": "Finite source set, not a confidence statement or exact-variant rescue prediction"},
            {"claim": "GSE BUB1B-spanning Rap/Pro signal direction across specified eligible-feature, estimator and sample diagnostics",
             "status": "below_one_in_all_calculated_diagnostics" if gse_lower else "not_established",
             "scope": "One normal cell line, n=2/condition; RNA features only"}],
        "changes": [
            {"claim": "PTC denominator wording", "measured_variant_rows": ptc["nearest_variant_row_count"],
             "unique_six_base_contexts": ptc["unique_nearest_6nt_context_count"],
             "consequence": "Replace ambiguous '12 contexts' with '12 measured variant rows spanning 8 distinct contexts'; not independent biological replicates"},
            {"claim": "PTC aggregation/deletion changes magnitude, not an efficacy estimate",
             "consequence": "Report paired-median, group-weighted and marginal-median estimands separately"}],
        "insufficient": [
            {"claim": "Exact-span GSE feature estimate", "status": gse["threshold_summaries"][-1]["status"]},
            {"claim": "Causal cell-cycle/proliferation adjustment", "status": "not_identifiable_from_these_data",
             "reason": "Quiescent serum-restricted and rapamycin samples are not cell-cycle matched; no measured cell-cycle covariate adjustment"},
            {"claim": "Exact BUB1B L737*/N1002K functional rescue, BUBR1 protein and clinical efficacy",
             "status": "not_tested"}],
        "candidate_decision": "No candidate promotion. PTC remains a low-priority experimental branch; these GSE data do not support an RNA abundance-increase rationale for sirolimus.",
        "interval_warning": "All reported deletion/cross-sample ranges are diagnostic ranges, not confidence intervals."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=ROOT)
    parser.add_argument("--outdir", type=Path, default=HERE / "results")
    args = parser.parse_args()
    sources = checked_sources(args.input_root)
    result = {"analysis_id": "MVA_EXPLORATORY_ROBUSTNESS_2026-10-24", "schema_version": 1,
              "status": "post-hoc exploratory; not biological validation",
              "protocol_sha256": sha(HERE / "protocol.json"),
              "pre_run_amendment_sha256": sha(HERE / "protocol_amendment_01.json"),
              "analysis_code_sha256": sha(Path(__file__)),
              "software": {"python": platform.python_version(), "openpyxl": version("openpyxl")},
              "source_manifest_sha256": sha(args.input_root / "input_manifest.json"),
              "original_script_manifest_sha256": sha(args.input_root / "original_script_hashes.json"),
              "verified_sources": sources,
              "execution": "deterministic exhaustive finite-set deletions; no random seed needed; no new p-values or confidence intervals",
              "ptc": ptc_analysis(args.input_root), "gse65145": gse_analysis(args.input_root)}
    result["interpretation"] = interpretations(result["ptc"], result["gse65145"])
    args.outdir.mkdir(parents=True, exist_ok=True)
    output = args.outdir / "sensitivity_results.json"
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    write_csv(args.outdir / "ptc_nearest_measured_rows.csv", result["ptc"]["nearest_rows"])
    write_csv(args.outdir / "ptc_leave_one_variant_row_out.csv", result["ptc"].get("leave_one_variant_row_out", []))
    write_csv(args.outdir / "ptc_leave_one_context_group_out.csv", result["ptc"].get("leave_one_context_group_out", []))
    write_csv(args.outdir / "gse_feature_thresholds.csv", result["gse65145"]["threshold_summaries"])
    write_csv(args.outdir / "gse_locus_overlap_audit.csv", result["gse65145"]["all_locus_overlaps_annotation_audit_only"])
    flat_features, flat_loo = [], []
    for feature in result["gse65145"]["features"]:
        identity = {k: feature[k] for k in ("track_row_1based_without_header", "chrom", "start_0based", "end_exclusive")}
        for method in ("arithmetic", "geometric"):
            for contrast, ratio in feature[method].get("ratios", {}).items():
                flat_features.append({**identity, "estimator": method, "contrast": contrast, "ratio": ratio,
                                      "log2_ratio": feature[method]["log2_ratios"][contrast]})
        for deletion in feature["leave_one_sample_out"]:
            for contrast, ratio in deletion["ratios"].items():
                flat_loo.append({**identity, "omitted_sample": deletion["omitted_sample"],
                                 "remaining_sample_counts": deletion["remaining_sample_counts"],
                                 "contrast": contrast, "ratio": ratio})
    write_csv(args.outdir / "gse_feature_estimators.csv", flat_features)
    write_csv(args.outdir / "gse_leave_one_sample_out.csv", flat_loo)
    hashes = {p.name: sha(p) for p in sorted(args.outdir.iterdir()) if p.is_file() and p.name != "artifact_hashes.json"}
    (args.outdir / "artifact_hashes.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print(json.dumps({"output": str(output), "sha256": sha(output),
                      "ptc_baseline": result["ptc"]["baseline"],
                      "ptc_row_LOO_range": result["ptc"].get("row_leave_out_median_paired_delta_range_percentage_points"),
                      "ptc_group_LOO_range": result["ptc"].get("context_group_leave_out_median_paired_delta_range_percentage_points"),
                      "gse_thresholds": result["gse65145"]["threshold_summaries"],
                      "gse_primary_arithmetic": result["gse65145"]["primary_feature"]["arithmetic"]}, indent=2))


if __name__ == "__main__":
    main()
