#!/usr/bin/env python3
"""Unit and public-source integration tests for the additive sensitivity audit."""
import json
import random
import unittest

import run_sensitivity as analysis


class UnitTests(unittest.TestCase):
    def test_frozen_threshold_grid(self):
        protocol = json.loads((analysis.HERE / "protocol.json").read_text())
        self.assertEqual(analysis.THRESHOLDS, protocol["gse65145"]["reciprocal_overlap_thresholds"])

    def test_censoring_is_not_exact_numeric(self):
        for cell, expected in [("<0.2", "left_censored"), (">0.2", "right_censored"),
                               ("≤0.2", "left_censored"), ("≥0.2", "right_censored"),
                               (None, "missing"), ("NA", "missing"), ("inf", "nonfinite")]:
            value, status = analysis.numeric_cell(cell)
            self.assertIsNone(value)
            self.assertEqual(status, expected)
        self.assertEqual(analysis.numeric_cell("0.2"), (0.2, "observed"))

    def test_median_paired_delta_not_difference_of_medians(self):
        rows = [{"gentamicin_percent": g, "untreated_percent": u,
                 "gentamicin_status": "observed", "untreated_status": "observed",
                 "context_6nt": str(i)} for i, (g, u) in enumerate([(0, 0), (10, 9), (11, 0)])]
        result = analysis.ptc_estimates(rows)
        self.assertEqual(result["median_paired_delta_percentage_points"], 1)
        self.assertEqual(result["difference_of_marginal_medians_percentage_points"], 10)
        self.assertEqual(result, analysis.ptc_estimates(list(reversed(rows))))
        rows[0]["gentamicin_status"] = "left_censored"
        self.assertIn("insufficient", analysis.ptc_estimates(rows)["status"])
        self.assertIn("insufficient", analysis.ptc_estimates([])["status"])

    def test_coordinate_selection_no_signal_input(self):
        anchor = {"chrom": "chr1", "txStart": 100, "txEnd": 200}
        coordinates = [("chr1", 99, 201), ("chr1", 100, 200),
                       ("chr1", 0, 1000), ("chr2", 100, 200)]
        self.assertEqual(analysis.eligible_feature_indices(coordinates, anchor, .95), [1, 0])
        self.assertEqual(analysis.eligible_feature_indices(coordinates, anchor, 1), [1])
        self.assertEqual(analysis.eligible_feature_indices([coordinates[0]], anchor, 1), [])

    def test_geometric_positive_guard_and_no_pseudocount(self):
        values = {"Pro": [1, 4], "Qui": [1, 1], "Rap": [2, 8]}
        self.assertAlmostEqual(analysis.contrasts(values, "geometric")["ratios"]["Rap_over_Pro"], 2)
        values["Qui"][0] = 0
        self.assertIn("insufficient", analysis.contrasts(values, "geometric")["status"])
        values["Qui"] = []
        self.assertIn("insufficient", analysis.contrasts(values)["status"])


class SourceIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = analysis.checked_sources(analysis.ROOT)
        cls.ptc = analysis.ptc_analysis(analysis.ROOT)
        cls.gse = analysis.gse_analysis(analysis.ROOT)

    def test_verified_sources_and_original_scripts(self):
        self.assertEqual(len(self.sources), 14)

    def test_ptc_inventory_and_censoring(self):
        self.assertEqual(self.ptc["complete_source_table_inventory"]["populated_source_rows"], 5837)
        self.assertEqual(self.ptc["complete_source_table_inventory"]["blank_formatted_rows"], 5837)
        self.assertEqual(self.ptc["valid_UGA_rows_in_complete_table"], 2724)
        self.assertEqual(self.ptc["nearest_variant_row_count"], 12)
        self.assertEqual(self.ptc["unique_nearest_6nt_context_count"], 8)
        self.assertEqual(self.ptc["minimum_hamming_distance"], 1)
        self.assertEqual(self.ptc["exact_6nt_rows"], 0)
        for counts in self.ptc["value_status_counts"].values():
            self.assertEqual(counts["observed"], 12)
            self.assertEqual(sum(v for k, v in counts.items() if k != "observed"), 0)

    def test_ptc_finite_leave_outs_and_group_removal(self):
        rows = self.ptc["nearest_rows"]
        baseline = self.ptc["baseline"]
        shuffled = rows.copy()
        random.Random(24).shuffle(shuffled)  # Test order-invariance only; analysis has no stochastic step.
        self.assertEqual(baseline, analysis.ptc_estimates(shuffled))
        self.assertAlmostEqual(baseline["median_paired_delta_percentage_points"], .0165)
        self.assertEqual(baseline["positive_paired_deltas"], 11)
        self.assertEqual(baseline["negative_paired_deltas"], 1)
        self.assertEqual(len(self.ptc["leave_one_variant_row_out"]), 12)
        self.assertTrue(all(r["n_variant_rows"] == 11 for r in self.ptc["leave_one_variant_row_out"]))
        self.assertEqual(len(self.ptc["leave_one_context_group_out"]), 8)
        for row in self.ptc["leave_one_context_group_out"]:
            context = row["omitted_context_6nt"]
            expected_omitted = {r["excel_row"] for r in rows if r["context_6nt"] == context}
            self.assertEqual(set(row["omitted_excel_rows"]), expected_omitted)
            self.assertEqual(row["n_unique_contexts"], 7)
            self.assertEqual(row["n_variant_rows"], 12 - len(expected_omitted))
        ranges = [("row_leave_out_median_paired_delta_range_percentage_points", .014, .019),
                  ("context_group_leave_out_median_paired_delta_range_percentage_points", .0135, .0285)]
        for key, low, high in ranges:
            self.assertAlmostEqual(self.ptc[key]["min"], low)
            self.assertAlmostEqual(self.ptc[key]["max"], high)

    def test_gse_rows_thresholds_and_fixed_n(self):
        self.assertEqual(self.gse["sample_counts_per_condition"], {"Pro": 2, "Qui": 2, "Rap": 2})
        self.assertEqual(self.gse["row_count_per_track"], 149122)
        self.assertEqual(self.gse["locus_overlapping_row_count"], 18)
        self.assertEqual([r["qualifying_feature_count"] for r in self.gse["threshold_summaries"]], [3, 3, 3, 3, 0])
        self.assertEqual(self.gse["threshold_summaries"][-1]["status"], "insufficient_no_eligible_feature")
        for f in self.gse["features"]:
            self.assertEqual(len(f["leave_one_sample_out"]), 6)
            for row in f["leave_one_sample_out"]:
                self.assertEqual(sorted(row["remaining_sample_counts"].values()), [1, 2, 2])
            for ratios in f["cross_sample_ratios"].values():
                self.assertEqual(len(ratios["values"]), 4)

    def test_gse_primary_and_direction_robustness(self):
        primary = self.gse["primary_feature"]
        self.assertEqual(primary["track_row_1based_without_header"], 116255)
        self.assertAlmostEqual(primary["arithmetic"]["ratios"]["Rap_over_Pro"], .5857063642506453)
        self.assertAlmostEqual(primary["geometric"]["ratios"]["Rap_over_Pro"], .584998, places=6)
        for f in self.gse["features"]:
            self.assertLess(f["arithmetic"]["ratios"]["Rap_over_Pro"], 1)
            self.assertLess(f["geometric"]["ratios"]["Rap_over_Pro"], 1)
            self.assertTrue(all(r["ratios"]["Rap_over_Pro"] < 1 for r in f["leave_one_sample_out"]))
            self.assertLess(f["cross_sample_ratios"]["Rap_over_Pro"]["max"], 1)
            self.assertLess(f["arithmetic"]["ratios"]["Qui_over_Pro"], 1)
            self.assertGreater(f["arithmetic"]["ratios"]["Rap_over_Qui"], 1)

    def test_bounded_machine_readable_interpretation(self):
        result = analysis.interpretations(self.ptc, self.gse)
        self.assertEqual(result["stable"][0]["status"], "positive_in_all_deletions")
        self.assertEqual(result["stable"][1]["status"], "below_one_in_all_calculated_diagnostics")
        self.assertEqual(result["insufficient"][0]["status"], "insufficient_no_eligible_feature")
        self.assertEqual(result["insufficient"][1]["status"], "not_identifiable_from_these_data")


if __name__ == "__main__":
    unittest.main(verbosity=2)
