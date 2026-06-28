# Setup

## Prerequisites

- Home Assistant (recent stable version)
- At least one Zendure 2400AC (or compatible) unit
- Per-phase grid power measurements exposed as HA sensors
- Network access from HA to Zendure devices / cloud API

## Installation

1. Clone this repository into your Home Assistant `config` directory:
   ```bash
   git clone https://github.com/<your-user>/smartflow-per-phase.git

2. Copy custom_components/zendure_control into config/custom_components/.

3. Restart Home Assistant.

4. Configure the integration using example_configuration.yaml as a reference.

5. Import blueprints from ha-blueprints/ into Home Assistant.