"""Phase matching logic for SmartFlow."""

from __future__ import annotations
from typing import Tuple


def distribute_power_across_phases(
    l1_target: int,
    l2_target: int,
    l3_target: int,
    total_available_w: int,
) -> Tuple[int, int, int]:
    """Distribute available power across phases.

    Very simple placeholder strategy:
    - Cap each phase at total_available_w / 3
    - Return per-phase targets.
    """
    per_phase_cap = total_available_w // 3

    l1 = min(l1_target, per_phase_cap)
    l2 = min(l2_target, per_phase_cap)
    l3 = min(l3_target, per_phase_cap)

    return l1, l2, l3
