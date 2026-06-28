"""Export limit calculation for SmartFlow."""

from __future__ import annotations


def compute_export_limit(
    phase_power_w: float,
    max_export_w: float,
) -> int:
    """Compute export limit for a single phase.

    Positive phase_power_w means import from grid.
    Negative phase_power_w means export to grid.

    Returns a target battery power (W) to reduce export.
    """
    if phase_power_w >= 0:
        # Importing or neutral: no need to push power
        return 0

    export_w = -phase_power_w
    if export_w <= max_export_w:
        # Within allowed export
        return 0

    # Try to offset excess export
    excess = export_w - max_export_w
    return int(excess)
