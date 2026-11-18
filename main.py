"""HDPE pipe diameter selector. Run with: python main.py"""
from __future__ import annotations

from core.pipe_database import (
    PipeDatabaseError,
    list_available_material_grades,
    list_available_sdrs,
)
from core.pipe_sizing import recommend_pipe_diameter
from core.fluid_properties import estimate_from_ec


def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
            if value > 0 and value < float("inf"):
                return value
        except ValueError:
            pass
        print("Invalid input. Please enter a positive number.")


def choose_from_list(title: str, options: list, formatter=str):
    if not options:
        raise PipeDatabaseError(f"No options available for: {title}")
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}) {formatter(option)}")
    while True:
        try:
            choice = int(input(f"Enter the number (1-{len(options)}): ").strip())
            if 1 <= choice <= len(options):
                selected = options[choice - 1]
                print(f"Selected: {formatter(selected)}")
                return selected
        except ValueError:
            pass
        print(f"Invalid selection. Enter a number from 1 to {len(options)}.")


def main() -> None:
    print("\n======================================")
    print("       HDPE PIPE DIAMETER SELECTOR")
    print("======================================")

    flow = read_positive_float("\nFlow rate (m3/h): ")
    velocity = read_positive_float("Target velocity (m/s): ")

    print("\nOptional fluid-property estimate (does not change velocity-based pipe sizing):")
    ec = read_positive_float("Electrical conductivity EC (mS/cm, compensated to 25 °C): ")
    temperature = read_positive_float("Water temperature (°C): ")
    try:
        fluid = estimate_from_ec(ec, temperature)
    except ValueError as exc:
        print(f"Fluid-property input error: {exc}")
        return

    try:
        grades = list_available_material_grades()
        grade = choose_from_list("Available PE material grades:", grades, str)
        sdrs = list_available_sdrs(grade)
        sdr = choose_from_list(
            f"Available SDR values for {grade}:",
            sdrs,
            lambda value: f"SDR {value:g}",
        )
        result = recommend_pipe_diameter(
            flow_rate_m3_h=flow,
            target_velocity_m_s=velocity,
            material_grade=grade,
            sdr=sdr,
        )
    except (PipeDatabaseError, ValueError) as exc:
        print(f"\nSelection error: {exc}")
        return

    print("\n--- FLUID PROPERTY ESTIMATE (SCREENING ONLY) ---")
    print(f"EC                    : {fluid.ec_ms_cm:.3f} mS/cm")
    print(f"Estimated TDS         : {fluid.tds_mg_l:.0f} mg/L")
    print(f"Estimated density     : {fluid.density_kg_m3:.3f} kg/m3")
    print(f"Estimated kinematic viscosity: {fluid.kinematic_viscosity_m2_s:.6g} m2/s")
    print("Note: fluid properties do not affect this tool's velocity-only diameter recommendation.")

    pipe = result["recommended_pipe"]
    print("\n--- RECOMMENDED CATALOGUE PIPE ---")
    print(f"Material grade       : {pipe['material_grade']}")
    print(f"Nominal outside dia. : {pipe['dn_od_mm']:.0f} mm")
    print(f"SDR                  : {pipe['sdr']:g}")
    print(f"Nominal wall         : {pipe['nominal_wall_thickness_mm']:.1f} mm")
    print(f"Nominal inside dia.  : {pipe['nominal_internal_diameter_mm']:.1f} mm")
    print(f"Nominal pressure ref.: {pipe['nominal_pressure_bar']} bar")
    print(f"Calculated velocity  : {pipe['velocity_m_s']:.3f} m/s")
    print(f"Target velocity      : {velocity:.3f} m/s")
    if result["target_velocity_exceeded"]:
        print("\nWARNING: No available catalogue size meets the target velocity.")
        print(result["selection_method"])
    else:
        print("\nSelection criterion: smallest available OD that does not exceed target.")
    print("\n--- CATALOGUE ALTERNATIVES ---")
    print(f"{'OD (mm)':>9} {'ID (mm)':>10} {'Velocity (m/s)':>17} {'PN (bar)':>10} {'Meets target':>14}")
    for item in result["ranked_alternatives"]:
        status = "YES" if item["within_target"] else "NO"
        print(f"{item['dn_od_mm']:>9.0f} {item['nominal_internal_diameter_mm']:>10.1f} {item['velocity_m_s']:>17.3f} {item['nominal_pressure_bar']:>10} {status:>14}")
    print("\nEngineering limitations:")
    for note in result["limitations"]:
        print(f"- {note}")


if __name__ == "__main__":
    main()
