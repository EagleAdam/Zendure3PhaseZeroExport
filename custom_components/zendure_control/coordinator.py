"""Coordinator for SmartFlow Zendure control."""

from __future__ import annotations
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .api import ZendureApiClient


class ZendureCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, client: ZendureApiClient) -> None:
        super().__init__(
            hass,
            hass.logger,
            name="ZendureCoordinator",
            update_interval=None,
        )
        self._client = client
        self.last_simulated_values = {}  # store intended setpoints

    async def async_set_power(self, device_id: str, target_w: int) -> None:
        """Set or simulate power."""
        if self._client._simulation:
            # Store simulated value for HA sensors
            self.last_simulated_values[device_id] = target_w

        await self._client.set_power(device_id, target_w)
