#!/usr/bin/env python3
"""Reproduce a descriptive, locus-level audit of public GSE65145 processed tracks."""
from pathlib import Path
import argparse, gzip, hashlib, json, math, statistics, tarfile

SAMPLES = [
    ("GSM1588051", "Pro", 1), ("GSM1588052", "Pro", 2),
    ("GSM1588053", "Qui", 1), ("GSM1588054", "Qui", 2),
    ("GSM1588055", "Rap", 1), ("GSM1588056", "Rap", 2),
]
def sha(data):
    return hashlib.sha256(data).hexdigest()

def run(root):
    annotation_bytes = (root / "hg19_chr15_refseq.json").read_bytes()
    annotation = json.loads(annotation_bytes)
    matches = [r for r in annotation["ncbiRefSeq"]
               if r["name2"] == "BUB1B" and r["name"] == "NM_001211.6"]
    assert len(matches) == 1, "Expected one canonical BUB1B anchor"
    anchor = matches[0]
    start, end = anchor["txStart"], anchor["txEnd"]
    archive_bytes = (root / "GSE65145_RAW.tar").read_bytes()
    tracks, sample_info, coordinate_rows = {}, [], None
    overlapping_indices, eligible_indices = [], []
    with tarfile.open(root / "GSE65145_RAW.tar") as archive:
        assert len(archive.getmembers()) == 6, "Expected six processed samples"
        for gsm, condition, replicate in SAMPLES:
            member_name = f"{gsm}_{condition}_rep{replicate}.txt.gz"
            member = archive.getmember(member_name)
            compressed = archive.extractfile(member).read()
            data = gzip.decompress(compressed)
            lines = data.decode("utf-8").splitlines()
            assert lines[0].startswith("track type=bedGraph"), "Unexpected format"
            coords, values = [], []
            for line in lines[1:]:
                chrom, left, right, value = line.split("\t")
                left, right, value = int(left), int(right), float(value)
                assert left < right and math.isfinite(value) and value >= 0
                coords.append((chrom, left, right))
                values.append(value)
            if coordinate_rows is None:
                coordinate_rows = coords
                for i, (chrom, left, right) in enumerate(coords):
                    overlap = max(0, min(end, right) - max(start, left))
                    if chrom != anchor["chrom"] or overlap == 0:
                        continue
                    overlapping_indices.append(i)
                    if overlap / (end - start) >= 0.99 and overlap / (right - left) >= 0.99:
                        eligible_indices.append(i)
            else:
                assert coords == coordinate_rows, "Track coordinates/order differ"
            tracks[gsm] = values
            metadata_bytes = (root / f"{gsm}.soft").read_bytes()
            titles = [l.split(" = ", 1)[1] for l in metadata_bytes.decode().splitlines()
                      if l.startswith("!Sample_title = ")]
            assert len(titles) == 1
            assert str(replicate) in titles[0]
            # Preserve GEO's observed spelling for the serum-reduced samples.
            title_words = {"Pro":"proliferative", "Qui":"queiscent", "Rap":"rapamycin"}
            assert title_words[condition] in titles[0].lower()
            sample_info.append({
                "accession": gsm, "condition": condition, "replicate": replicate,
                "title": titles[0], "deposited_rows": len(values),
                "compressed_member": member_name, "compressed_sha256": sha(compressed),
                "uncompressed_sha256": sha(data), "metadata_sha256": sha(metadata_bytes)
            })
    assert eligible_indices, "No nearly full-span BUB1B features; do not infer a gene signal"
    ordered_indices = sorted(eligible_indices, key=lambda i: (
        abs(coordinate_rows[i][1] - start) + abs(coordinate_rows[i][2] - end),
        coordinate_rows[i]))
    features = []
    for index in ordered_indices:
        coords = coordinate_rows[index]
        vals = {condition: [tracks[gsm][index] for gsm,c,r in SAMPLES if c == condition]
                for condition in ("Pro", "Qui", "Rap")}
        means = {condition: statistics.mean(v) for condition,v in vals.items()}
        assert means["Pro"] > 0 and means["Qui"] > 0
        features.append({
            "track_row_1based_without_header": index + 1,
            "chrom": coords[0], "start_0based": coords[1], "end_exclusive": coords[2],
            "boundary_distance_bp": abs(coords[1]-start)+abs(coords[2]-end),
            "values_RPKM_as_deposited": vals, "arithmetic_means": means,
            "ratios_of_arithmetic_means": {
                "Rap_over_Pro": means["Rap"]/means["Pro"],
                "Qui_over_Pro": means["Qui"]/means["Pro"],
                "Rap_over_Qui": means["Rap"]/means["Qui"]
            }
        })
    report = {
        "analysis_id": "MVA-RAP-GSE65145-001", "recorded_on": "2026-10-10",
        "status": "Completed", "scope": "Descriptive public normal-human-cell RNA feature reanalysis",
        "dataset": "GSE65145", "model": "2DD normal human foreskin fibroblasts; one cell line",
        "groups": {"Pro": "10% FBS, DMSO vehicle",
                   "Qui": "0.5% FBS for five days",
                   "Rap": "500 nM rapamycin for five days, 10% FBS"},
        "samples": sample_info,
        "anchor": {"accession": anchor["name"], "gene": anchor["name2"],
                   "assembly": "hg19", "chrom": anchor["chrom"],
                   "start_0based": start, "end_exclusive": end, "strand": anchor["strand"]},
        "selection_rule": "At least 99% reciprocal interval overlap with canonical RefSeq span; select minimum sum of absolute boundary distances, independent of signal values.",
        "row_count_per_sample": len(coordinate_rows),
        "unique_coordinate_count": len(set(coordinate_rows)),
        "overlapping_row_count": len(overlapping_indices),
        "qualifying_feature_count": len(features),
        "primary_feature": features[0],
        "sensitivity_features": features,
        "primary_percent_difference_Rap_vs_Pro":
            100*(features[0]["ratios_of_arithmetic_means"]["Rap_over_Pro"]-1),
        "sensitivity_Rap_over_Pro_range": [
            min(f["ratios_of_arithmetic_means"]["Rap_over_Pro"] for f in features),
            max(f["ratios_of_arithmetic_means"]["Rap_over_Pro"] for f in features)],
        "inference": "The BUB1B-spanning RNA feature is lower under continuous rapamycin than proliferative vehicle control. These data do not support an abundance-increase rationale for sirolimus in this model.",
        "decision": "Conditional: do not promote sirolimus as a BUBR1-abundance rescue candidate from these data.",
        "limits": [
            "Unstranded genomic-span features, not direct BUBR1 protein measurements or validated mature transcript isoform estimates.",
            "Three overlapping features are sensitivity views of the same locus, not independent biological replicates.",
            "Two biological replicates per condition from one normal cell line; no MVA genotype and no donor-level replication.",
            "Serum reduction is a useful control but is not matched to rapamycin for cell-cycle distribution; no causal proliferation adjustment is claimed.",
            "Continuous 500 nM/five-day treatment; no washout, transient exposure, aneuploidy, mitotic checkpoint or rescue endpoint.",
            "Published normalized RPKM values are used as deposited without re-alignment, count-based differential expression, an added pseudocount, p-values or rescue probabilities.",
            "149122 rows were observed in each deposited track; the paper states 149135 probes. The 13-row difference is not resolved here.",
            "This does not establish that BUBR1 protein falls, rule out post-transcriptional effects, or predict clinical harm or benefit."
        ],
        "source": {"pmid": "26652669", "doi": "10.1080/19491034.2015.1128610",
                   "location": "Figures 1 and 3; Figure S2; Cell culture and RNA-seq analysis methods; GEO processed tracks",
                   "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4915505/"},
        "inputs": [
            {"name":"GSE65145_RAW.tar","sha256":sha(archive_bytes),
             "url":"https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65145/suppl/GSE65145_RAW.tar"},
            {"name":"hg19_chr15_refseq.json","sha256":sha(annotation_bytes),
             "url":"https://api.genome.ucsc.edu/getData/track?genome=hg19;track=ncbiRefSeq;chrom=chr15;start=40000000;end=41000000"}
        ]
    }
    (root / "gse65145_bub1b_results.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["row_count_per_sample","unique_coordinate_count","overlapping_row_count","qualifying_feature_count","primary_feature","sensitivity_Rap_over_Pro_range"]},indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path, nargs="?", default=Path(__file__).resolve().parent)
    run(parser.parse_args().directory)

