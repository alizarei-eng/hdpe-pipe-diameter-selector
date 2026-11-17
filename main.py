"""HDPE pipe diameter selector. Run with: python main.py"""
from __future__ import annotations

from core.pipe_database import (
    PipeDatabaseError,
    list_available_material_grades,
    list_available_sdrs,
)
from core.pipe_sizing import recommend_pipe_diameter


def read_positive_float(prompt: str) -> float:
    """Read a finite positive number from the terminal."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0 and value < float("inf"):
                return value
        except ValueError:
            pass
        print("Invalid input. Please enter a positive number.")


def choose_from_list(title: str, options: list, formatter=str):
    """Print numbered options and return the option selected by its number."""
    if not options:
        raise PipeDatabaseError(f"No options available for: {title}")

    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}) {formatter(option)}")

    while True:
        raw_choice = input(f"Enter the number (1-{len(options)}): ").strip()
        try:
            choice = int(raw_choice)
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

    try:
        # Step 1: choose a material grade by its menu number.
        grades = list_available_material_grades()
        grade = choose_from_list("Available PE material grades:", grades, str)

        # Step 2: show only SDR values that exist for the selected grade.
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
    print(
        f"{'OD (mm)':>9} {'ID (mm)':>10} {'Velocity (m/s)':>17} "
        f"{'PN (bar)':>10} {'Meets target':>14}"
    )
    for item in result["ranked_alternatives"]:
        status = "YES" if item["within_target"] else "NO"
        print(
            f"{item['dn_od_mm']:>9.0f} "
            f"{item['nominal_internal_diameter_mm']:>10.1f} "
            f"{item['velocity_m_s']:>17.3f} "
            f"{item['nominal_pressure_bar']:>10} {status:>14}"
        )

    print("\nEngineering limitations:")
    for note in result["limitations"]:
        print(f"- {note}")


if __name__ == "__main__":
    main()
