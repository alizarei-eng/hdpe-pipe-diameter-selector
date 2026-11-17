import unittest
from core.pipe_database import (PipeDatabaseError, list_available_pipes,
                                list_available_sdrs)
from core.pipe_sizing import recommend_pipe_diameter

class TestPipeSizing(unittest.TestCase):
    def test_selects_smallest_size_not_exceeding_target(self):
        result = recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5)
        selected = result["recommended_pipe"]
        self.assertEqual(selected["dn_od_mm"], 140)
        self.assertLessEqual(selected["velocity_m_s"], 1.5)
        self.assertFalse(result["target_velocity_exceeded"])

    def test_pe80_is_supported(self):
        result = recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5,
                                         material_grade="PE80", sdr=11)
        self.assertEqual(result["recommended_pipe"]["material_grade"], "PE80")
        self.assertEqual(result["recommended_pipe"]["dn_od_mm"], 140)

    def test_all_sdr_series_are_listed_for_pe80(self):
        self.assertEqual(list_available_sdrs("PE80"), [6.0, 7.4, 9.0, 11.0, 13.6, 17.0, 21.0, 26.0, 33.0, 41.0])

    def test_pe100_sdr6_is_not_supported(self):
        self.assertNotIn(6.0, list_available_sdrs("PE100"))
        with self.assertRaises(PipeDatabaseError):
            recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5,
                                    material_grade="PE100", sdr=6)

    def test_pe100_sdr41_starts_at_315_mm(self):
        records = list_available_pipes("PE100", 41)
        self.assertEqual(min(p["dn_od_mm"] for p in records), 315)
        self.assertEqual(max(p["dn_od_mm"] for p in records), 3000)

    def test_catalogue_reaches_3000_mm(self):
        records = list_available_pipes("PE100", 21)
        self.assertEqual(max(item["dn_od_mm"] for item in records), 3000)

    def test_sdr11_minimum_wall_at_od20_is_2mm(self):
        records = list_available_pipes("PE100", 11)
        item = next(p for p in records if p["dn_od_mm"] == 20)
        self.assertEqual(item["nominal_wall_thickness_mm"], 2.0)

    def test_alternatives_include_velocity_and_pn(self):
        result = recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5)
        self.assertTrue(all("velocity_m_s" in p and "nominal_pressure_bar" in p
                            for p in result["ranked_alternatives"]))

    def test_rejects_nonpositive_inputs(self):
        with self.assertRaises(PipeDatabaseError):
            recommend_pipe_diameter(flow_rate_m3_h=0, target_velocity_m_s=1.5)
        with self.assertRaises(PipeDatabaseError):
            recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=0)

if __name__ == "__main__":
    unittest.main()
