import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "databases" / "manufacturer_catalogues" / "gf_pe100_water_2022.json"


class TestGFPE100ManufacturerCatalogue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATA_PATH.open("r", encoding="utf-8") as file:
            cls.data = json.load(file)
        cls.pipes = cls.data["pipes"]

    def find(self, od, sdr):
        matches = [
            p for p in self.pipes
            if p["dn_od_mm"] == od and p["sdr"] == sdr
        ]
        self.assertEqual(len(matches), 1)
        return matches[0]

    def test_dataset_count_and_unique_keys(self):
        self.assertEqual(len(self.pipes), self.data["summary"]["record_count"])
        keys = [(p["dn_od_mm"], p["sdr"]) for p in self.pipes]
        self.assertEqual(len(keys), len(set(keys)))

    def test_known_110_mm_sdr11_catalogue_entry(self):
        pipe = self.find(110, 11)
        self.assertEqual(pipe["minimum_wall_thickness_mm"], 10.0)
        self.assertEqual(pipe["nominal_pressure_bar"], 16)
        self.assertAlmostEqual(pipe["average_mass_kg_m"], 3.20)

    def test_small_diameter_sdr13_6_entry(self):
        pipe = self.find(20, 13.6)
        self.assertEqual(pipe["minimum_wall_thickness_mm"], 1.6)
        self.assertAlmostEqual(pipe["average_mass_kg_m"], 0.10)

    def test_catalogue_missing_combination_is_not_fabricated(self):
        matches = [
            p for p in self.pipes
            if p["dn_od_mm"] == 1200 and p["sdr"] == 13.6
        ]
        self.assertEqual(matches, [])

    def test_all_records_have_traceable_positive_dimensions(self):
        for pipe in self.pipes:
            self.assertEqual(pipe["record_status"], "transcribed_manufacturer_catalogue")
            self.assertTrue(pipe["source_table"])
            self.assertGreater(pipe["minimum_wall_thickness_mm"], 0)
            self.assertGreater(pipe["average_mass_kg_m"], 0)


if __name__ == "__main__":
    unittest.main()
