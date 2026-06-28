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
            update_interval=None,  # driven by automations
        )
        self._client = client

    async def async_set_power(self, device_id: str, target_w: int) -> None:
        await self._client.set_power(device_id, target_w)

