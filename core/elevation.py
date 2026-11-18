"""Elevation and static-head calculations for a pipeline."""
from __future__ import annotations


def calculate_static_head(*, elevation_start_m: float, elevation_end_m: float) -> float:
    """Return z_end - z_start in metres.

    Positive means uphill to the destination; negative means downhill.
    Both elevations must use the same vertical datum.
    """
    values = (elevation_start_m, elevation_end_m)
    if any(not isinstance(value, (int, float)) for value in values):
        raise TypeError("Elevations must be numeric values.")
    if any(value != value or value in (float("inf"), float("-inf")) for value in values):
        raise ValueError("Elevations must be finite numbers.")
    return float(elevation_end_m) - float(elevation_start_m)
