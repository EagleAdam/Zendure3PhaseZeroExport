"""Coordinator for SmartFlow Zendure control."""

from __future__ import annotations
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .api import ZendureApiClient

_LOGGER = logging.getLogger(__name__)

class ZendureCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, client: ZendureApiClient) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name="ZendureCoordinator",
            update_interval=None,
        )
        self._client = client
        self.last_simulated_values = {}

    async def async_set_power(self, device_id: str, target_w: int) -> None:
        if self._client._simulation:
            self.last_simulated_values[device_id] = target_w

        await self._client.set_power(device_id, target_w)
