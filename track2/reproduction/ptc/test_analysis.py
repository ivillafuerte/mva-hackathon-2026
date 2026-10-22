#!/usr/bin/env python3
import json
from pathlib import Path


result = json.loads(Path("results/results.json").read_text())
assert result["exact_measured_6nt_context_matches"] == 0
assert result["nearest_measured_context_hamming_distance"] == 1
assert result["nearest_measured_context_count"] == 12
assert result["l737star_present_in_measured_table"] is False
supported = {x["treatment"]: float(x["predicted_readthrough_percent"]) for x in result["exact_coordinate_predictions_supported_models"]}
assert supported["DAP"] > supported["G418"]
assert supported["SJ6986"] > supported["G418"]
excluded = {x["treatment"] for x in result["exact_coordinate_predictions_excluded_low_signal_models"]}
assert excluded == {"Gentamicin", "FUr"}
print("PASS: context gate invariants")
