"""Zendure API client with simulation mode."""

from __future__ import annotations
import logging

_LOGGER = logging.getLogger(__name__)


class ZendureApiClient:
    def __init__(self, account_id: str, api_token: str, simulation: bool = False) -> None:
        self._account_id = account_id
        self._api_token = api_token
        self._simulation = simulation

    async def set_power(self, device_id: str, target_w: int) -> None:
        """Set target power for a device.

        In simulation mode, no real API call is made.
        """
        if self._simulation:
            _LOGGER.info(
                "[SIMULATION] Would set device %s to %s W",
                device_id,
                target_w,
            )
            return

        # TODO: Implement real HTTP call
        _LOGGER.debug("Setting device %s to %s W", device_id, target_w)
        return
