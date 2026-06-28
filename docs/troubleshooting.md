
---

## docs/troubleshooting.md

```markdown
# Troubleshooting

## No entities from `zendure_control`

- Check Home Assistant logs for integration errors.
- Verify API credentials and network reachability.
- Confirm `manifest.json` is correctly installed under `custom_components/zendure_control`.

## Export limit not applied

- Ensure automations based on the blueprints are enabled.
- Verify that per-phase sensors are updating.
- Check that safety watchdog is not blocking control due to invalid data.

## General tips

- Enable debug logging for the integration during initial setup.
- Test with conservative limits before relying on the system unattended.
