import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "databases" / "manufacturer_catalogues" / "gf_pe100_water_fittings_2022.json"


class TestGFFittingsCatalogue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATA_PATH.open("r", encoding="utf-8") as file:
            cls.data = json.load(file)
        cls.fittings = cls.data["fittings"]

    def find(self, fitting_type, diameter, sdr=None):
        matches = [
            item for item in self.fittings
            if item["fitting_type"] == fitting_type
            and item["main_diameter_mm"] == diameter
            and (sdr is None or item["sdr"] == sdr)
        ]
        self.assertEqual(len(matches), 1)
        return matches[0]

    def test_dataset_count_and_unique_product_rows(self):
        self.assertEqual(len(self.fittings), self.data["summary"]["record_count"])
        keys = [
            (item["fitting_type"], item["main_diameter_mm"], item["sdr"], item["source_page"])
            for item in self.fittings
        ]
        self.assertEqual(len(keys), len(set(keys)))

    def test_electrofusion_coupler_110_sdr11(self):
        item = self.find("electrofusion_coupler", 110, 11)
        self.assertEqual(item["product_code"], "753911614E")
        self.assertEqual(item["dimensions_mm"]["L"], 145)
        self.assertAlmostEqual(item["weight_kg"], 0.691)

    def test_electrofusion_elbow_90_110(self):
        item = self.find("electrofusion_elbow_90", 110)
        self.assertEqual(item["dimensions_mm"]["Z"], 76)
        self.assertAlmostEqual(item["weight_kg"], 1.224)

    def test_equal_tee_110(self):
        item = self.find("electrofusion_tee_90_equal", 110)
        self.assertEqual(item["dimensions_mm"]["H"], 104)
        self.assertAlmostEqual(item["weight_kg"], 1.576)

    def test_tapping_saddle_separates_main_and_outlet_diameters(self):
        item = self.find("tapping_saddle_monoline_cutter_8mm", 110)
        self.assertEqual(item["branch_diameter_mm"], 20)
        self.assertEqual(item["dimensions_mm"]["H"], 199)
        self.assertAlmostEqual(item["weight_kg"], 0.631)

    def test_all_records_are_traceable_and_positive(self):
        for item in self.fittings:
            self.assertEqual(item["record_status"], "transcribed_manufacturer_catalogue")
            self.assertTrue(item["source_page"])
            self.assertTrue(item["source_table"])
            self.assertGreater(item["main_diameter_mm"], 0)
            self.assertGreater(item["pressure_rating_bar"], 0)
            self.assertGreater(item["weight_kg"], 0)


if __name__ == "__main__":
    unittest.main()
