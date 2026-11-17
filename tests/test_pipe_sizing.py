import unittest
from core.pipe_database import PipeDatabaseError, list_available_pipes
from core.pipe_sizing import recommend_pipe_diameter


class TestPipeSizing(unittest.TestCase):
    def test_selects_smallest_size_not_exceeding_target(self):
        result = recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5)
        selected = result["recommended_pipe"]
        self.assertEqual(selected["dn_od_mm"], 140)
        self.assertLessEqual(selected["velocity_m_s"], 1.5)
        self.assertFalse(result["target_velocity_exceeded"])

    def test_pe80_is_supported(self):
        result = recommend_pipe_diameter(
            flow_rate_m3_h=50,
            target_velocity_m_s=1.5,
            material_grade="PE80",
            sdr=11,
        )
        self.assertEqual(result["recommended_pipe"]["material_grade"], "PE80")
        self.assertEqual(result["recommended_pipe"]["dn_od_mm"], 140)

    def test_catalogue_reaches_3000_mm(self):
        records = list_available_pipes("PE100", 11)
        self.assertEqual(max(item["dn_od_mm"] for item in records), 3000)
        result = recommend_pipe_diameter(
            flow_rate_m3_h=5000,
            target_velocity_m_s=0.1,
            material_grade="PE100",
            sdr=11,
        )
        self.assertEqual(result["recommended_pipe"]["dn_od_mm"], 3000)
        self.assertTrue(result["target_velocity_exceeded"])

    def test_alternatives_include_velocity(self):
        result = recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=1.5)
        self.assertEqual(len(result["ranked_alternatives"]), len(list_available_pipes("PE100", 11)))
        self.assertTrue(all("velocity_m_s" in p for p in result["ranked_alternatives"]))

    def test_rejects_nonpositive_inputs(self):
        with self.assertRaises(PipeDatabaseError):
            recommend_pipe_diameter(flow_rate_m3_h=0, target_velocity_m_s=1.5)
        with self.assertRaises(PipeDatabaseError):
            recommend_pipe_diameter(flow_rate_m3_h=50, target_velocity_m_s=0)


if __name__ == "__main__":
    unittest.main()
