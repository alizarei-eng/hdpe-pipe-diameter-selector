"""Velocity-based selection of a documented HDPE catalogue size."""
from __future__ import annotations
import math
from typing import Any
from core.pipe_database import PipeDatabaseError, list_available_pipes

def recommend_pipe_diameter(*, flow_rate_m3_h: float, target_velocity_m_s: float,
                            material_grade: str = "PE100", sdr: float = 11,
                            database: dict[str, Any] | None = None) -> dict[str, Any]:
    """Choose the smallest available OD whose nominal velocity is at or below target."""
    if not math.isfinite(flow_rate_m3_h) or flow_rate_m3_h <= 0:
        raise PipeDatabaseError("Flow rate must be a finite number greater than zero.")
    if not math.isfinite(target_velocity_m_s) or target_velocity_m_s <= 0:
        raise PipeDatabaseError("Target velocity must be a finite number greater than zero.")
    grade = material_grade.strip().upper()
    flow_m3_s = float(flow_rate_m3_h) / 3600.0
    records = list_available_pipes(material_grade=grade, sdr=sdr, database=database)
    if not records:
        raise PipeDatabaseError(f"No catalogue records for grade={grade}, SDR={sdr}. Check available grade/SDR combinations.")
    candidates = []
    for record in records:
        wall = record.get("nominal_wall_thickness_mm")
        if wall is None:
            continue
        od_mm = float(record["dn_od_mm"])
        id_mm = od_mm - 2.0 * float(wall)
        if id_mm <= 0:
            continue
        area_m2 = math.pi * (id_mm / 1000.0) ** 2 / 4.0
        velocity = flow_m3_s / area_m2
        candidates.append({
            "material_grade": grade, "dn_od_mm": od_mm, "sdr": float(record["sdr"]),
            "nominal_wall_thickness_mm": float(wall), "nominal_internal_diameter_mm": id_mm,
            "velocity_m_s": velocity, "within_target": velocity <= target_velocity_m_s,
            "velocity_margin_m_s": target_velocity_m_s - velocity,
            "nominal_pressure_bar": record.get("nominal_pressure_bar"),
            "source_id": record.get("source_id"), "status": record.get("status")
        })
    if not candidates:
        raise PipeDatabaseError(f"No usable catalogue dimensions found for grade={grade}, SDR={sdr}.")
    candidates.sort(key=lambda item: item["dn_od_mm"])
    compliant = [item for item in candidates if item["within_target"]]
    if compliant:
        selected, exceeded = compliant[0], False
        note = "Selected the smallest available OD whose nominal calculated velocity is at or below target."
    else:
        selected, exceeded = candidates[-1], True
        note = "Even the largest available OD exceeds target velocity; review the design or catalogue range."
    return {
        "input": {"flow_rate_m3_h": float(flow_rate_m3_h), "target_velocity_m_s": float(target_velocity_m_s),
                  "material_grade": grade, "sdr": float(sdr)},
        "recommended_pipe": selected, "target_velocity_exceeded": exceeded,
        "ranked_alternatives": candidates, "selection_method": note,
        "limitations": [
            "ID uses nominal OD minus twice the nominal wall thickness; actual bore varies with tolerances.",
            "Several wall thicknesses in this reference dataset are ratio-derived estimates, not individually transcribed Table 2 values; verify before design release.",
            "PN is a reference rating and does not include temperature derating or project-specific design factors.",
            "Pressure loss, pump curve, water hammer, chemical compatibility, installation and manufacturer availability are not checked."
        ]
    }
