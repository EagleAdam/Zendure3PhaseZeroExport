# Architecture

SmartFlow is built around three main layers:

1. **Measurement layer**
   - Reads per-phase grid power from an external meter (e.g. SolarEdge, HomeWizard P1, etc.).
   - Exposes these as Home Assistant sensors.

2. **Control layer**
   - Computes per-phase export limits and battery setpoints.
   - Implemented in `scripts/export_limit.py` and `scripts/phase_matching.py`.

3. **Integration layer**
   - Home Assistant custom component `zendure_control` sends commands to Zendure 2400AC units.
   - Blueprints orchestrate automations using the integration and sensors.

## Data flow

1. Grid meter → HA sensors (per phase)
2. HA sensors → SmartFlow algorithms (Python scripts)
3. Algorithms → target power / export limit per phase
4. Integration → Zendure API calls
5. Feedback loop every N seconds (configurable)

This document will be expanded with sequence diagrams and entity lists as the project matures.
