import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "databases" / "hydraulic_fittings.json"


class TestHydraulicFittingReferences(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATA_PATH.open("r", encoding="utf-8") as file:
            cls.data = json.load(file)
        cls.fittings = cls.data["fittings"]

    def find(self, fitting_type, flow_path=None):
        matches = [item for item in self.fittings if item["fitting_type"] == fitting_type and (flow_path is None or item["flow_path"] == flow_path)]
        self.assertEqual(len(matches), 1)
        return matches[0]

    def test_all_11_legacy_records_transferred(self):
        self.assertEqual(len(self.fittings), 11)
        self.assertEqual(len({item["id"] for item in self.fittings}), 11)

    def test_elbow_k_values_preserved(self):
        self.assertAlmostEqual(self.find("elbow_90_long_radius")["k"], 0.2)
        self.assertAlmostEqual(self.find("elbow_90_standard")["k"], 0.9)
        self.assertAlmostEqual(self.find("elbow_45")["k"], 0.4)

    def test_tee_flow_paths_are_separate(self):
        straight = self.find("tee", "straight_run")
        branch = [item for item in self.fittings if item["fitting_type"] == "tee" and item["flow_path"] == "branch_flow"]
        self.assertEqual(straight["flow_path"], "straight_run")
        self.assertAlmostEqual(straight["k"], 0.6)
        self.assertEqual(len(branch), 1)
        self.assertAlmostEqual(branch[0]["k"], 1.8)

    def test_valves_and_boundary_losses_preserved(self):
        expected = {
            "gate_valve": 0.15,
            "ball_valve": 0.05,
            "globe_valve": 10.0,
            "swing_check_valve": 2.0,
            "sharp_edged_entrance": 0.5,
            "pipe_exit_large_tank": 1.0,
        }
        for fitting_type, value in expected.items():
            self.assertAlmostEqual(self.find(fitting_type)["k"], value)

    def test_records_have_valid_k_and_provenance(self):
        self.assertEqual(self.data["provenance"]["transfer_status"], "copied_from_existing_project")
        self.assertTrue(self.data["provenance"]["source_file"])
        for item in self.fittings:
            self.assertGreaterEqual(item["k"], 0)
            self.assertTrue(item["flow_path"])
            self.assertEqual(item["geometry_status"], "generic_reference")


if __name__ == "__main__":
    unittest.main()
