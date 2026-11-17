"""HDPE pipe diameter selector. Run with: python main.py"""
from __future__ import annotations
from core.pipe_database import (PipeDatabaseError, list_available_sdrs,
                                list_available_material_grades)
from core.pipe_sizing import recommend_pipe_diameter

def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0 and value < float("inf"):
                return value
        except ValueError:
            pass
        print("Please enter a positive number.")

def main() -> None:
    print("\\n======================================")
    print("       HDPE PIPE DIAMETER SELECTOR")
    print("======================================")
    flow = read_positive_float("Flow rate (m3/h): ")
    velocity = read_positive_float("Target velocity (m/s): ")
    grades = list_available_material_grades()
    grade = input(f"PE material grade {grades} [PE100]: ").strip().upper() or "PE100"
    if grade not in grades:
        print(f"Unsupported grade. Available grades: {grades}")
        return
    sdrs = list_available_sdrs(grade)
    print(f"Available SDR values for {grade}: {sdrs}")
    default_sdr = 11.0 if 11.0 in sdrs else sdrs[0]
    sdr_text = input(f"Pipe SDR {sdrs} [{default_sdr:g}]: ").strip()
    try:
        sdr = float(sdr_text) if sdr_text else default_sdr
        result = recommend_pipe_diameter(flow_rate_m3_h=flow, target_velocity_m_s=velocity,
                                         material_grade=grade, sdr=sdr)
    except (PipeDatabaseError, ValueError) as exc:
        print(f"\\nSelection error: {exc}")
        return
    pipe = result["recommended_pipe"]
    print("\\n--- RECOMMENDED CATALOGUE PIPE ---")
    print(f"Material grade       : {pipe['material_grade']}")
    print(f"Nominal outside dia. : {pipe['dn_od_mm']:.0f} mm")
    print(f"SDR                  : {pipe['sdr']:g}")
    print(f"Nominal wall         : {pipe['nominal_wall_thickness_mm']:.1f} mm")
    print(f"Nominal inside dia.  : {pipe['nominal_internal_diameter_mm']:.1f} mm")
    print(f"Nominal pressure ref.: {pipe['nominal_pressure_bar']} bar")
    print(f"Calculated velocity  : {pipe['velocity_m_s']:.3f} m/s")
    print(f"Target velocity      : {velocity:.3f} m/s")
    if result["target_velocity_exceeded"]:
        print("\\nWARNING: No available catalogue size meets the target velocity.")
        print(result["selection_method"])
    else:
        print("\\nSelection criterion: smallest available OD that does not exceed target.")
    print("\\n--- CATALOGUE ALTERNATIVES ---")
    print(f"{'OD (mm)':>9} {'ID (mm)':>10} {'Velocity (m/s)':>17} {'PN (bar)':>10} {'Meets target':>14}")
    for item in result["ranked_alternatives"]:
        status = "YES" if item["within_target"] else "NO"
        print(f"{item['dn_od_mm']:>9.0f} {item['nominal_internal_diameter_mm']:>10.1f} "
              f"{item['velocity_m_s']:>17.3f} {item['nominal_pressure_bar']:>10} {status:>14}")
    print("\\nEngineering limitations:")
    for note in result["limitations"]:
        print(f"- {note}")

if __name__ == "__main__":
    main()
