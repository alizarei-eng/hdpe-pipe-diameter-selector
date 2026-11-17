"""Lookup and geometry utilities for documented PE pipe dimensions.

Only dimensions explicitly present in databases/pipe_standards.json are returned.
The module does not invent missing standard sizes or treat OD/SDR as a substitute
for a documented nominal wall thickness.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATABASE_PATH = Path(__file__).resolve().parents[1] / "databases" / "pipe_standards.json"


class PipeDatabaseError(ValueError):
    """Raised when pipe database input or content is invalid."""


def load_pipe_database(path: str | Path | None = None) -> dict[str, Any]:
    """Load the pipe dimension database from JSON."""
    file_path = Path(path) if path is not None else DATABASE_PATH
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise PipeDatabaseError(f"Pipe database not found: {file_path}") from exc
    except json.JSONDecodeError as exc:
        raise PipeDatabaseError(f"Invalid JSON in pipe database: {file_path}") from exc

    if not isinstance(data.get("pipes"), list):
        raise PipeDatabaseError("Pipe database must contain a 'pipes' list.")
    return data


def list_available_pipes(
    material_grade: str | None = None,
    sdr: float | None = None,
    database: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Return documented pipe records, optionally filtered by grade and SDR."""
    data = database if database is not None else load_pipe_database()
    records = data["pipes"]

    if material_grade is not None:
        grade = material_grade.strip().upper()
        records = [p for p in records if p["material_grade"].upper() == grade]
    if sdr is not None:
        records = [p for p in records if float(p["sdr"]) == float(sdr)]

    return sorted(records, key=lambda p: (p["dn_od_mm"], p["sdr"]))


def get_pipe_dimensions(
    dn_od_mm: float,
    sdr: float,
    material_grade: str = "PE100",
    database: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Find an exact documented OD/SDR/grade combination."""
    if dn_od_mm <= 0 or sdr <= 1:
        raise PipeDatabaseError("OD must be positive and SDR must be greater than 1.")

    data = database if database is not None else load_pipe_database()
    matches = [
        p for p in data["pipes"]
        if float(p["dn_od_mm"]) == float(dn_od_mm)
        and float(p["sdr"]) == float(sdr)
        and p["material_grade"].upper() == material_grade.strip().upper()
    ]
    if not matches:
        raise PipeDatabaseError(
            f"No documented pipe found for grade={material_grade}, "
            f"OD={dn_od_mm} mm, SDR={sdr}. No dimensions were inferred."
        )
    return dict(matches[0])


def calculate_internal_diameter(
    dn_od_mm: float,
    wall_thickness_mm: float,
) -> float:
    """Calculate nominal geometric ID from OD and a supplied wall thickness."""
    if dn_od_mm <= 0 or wall_thickness_mm <= 0:
        raise PipeDatabaseError("OD and wall thickness must be positive.")
    if 2 * wall_thickness_mm >= dn_od_mm:
        raise PipeDatabaseError("Wall thickness must be less than half the OD.")
    return float(dn_od_mm) - 2.0 * float(wall_thickness_mm)


def get_pipe_geometry(
    dn_od_mm: float,
    sdr: float,
    material_grade: str = "PE100",
    database: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Return a database record plus calculated nominal internal diameter."""
    record = get_pipe_dimensions(dn_od_mm, sdr, material_grade, database)
    wall = record.get("nominal_wall_thickness_mm")
    if wall is None:
        raise PipeDatabaseError(
            "Nominal wall thickness is not available for this record; "
            "provide a verified thickness before calculating ID."
        )
    result = dict(record)
    result["nominal_internal_diameter_mm"] = calculate_internal_diameter(
        record["dn_od_mm"], wall
    )
    result["geometry_note"] = (
        "Nominal geometric ID = nominal OD - 2 × nominal wall thickness; "
        "actual bore can vary with dimensional tolerances."
    )
    return result
