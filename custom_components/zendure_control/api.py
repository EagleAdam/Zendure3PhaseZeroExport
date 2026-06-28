"""Minimal Zendure API client placeholder."""

from __future__ import annotations


class ZendureApiClient:
    def __init__(self, account_id: str, api_token: str) -> None:
        self._account_id = account_id
        self._api_token = api_token

    async def set_power(self, device_id: str, target_w: int) -> None:
        """Set target power for a device.

        TODO: Implement real HTTP calls to Zendure API.
        """
        # Placeholder: log or mock behaviour
        return
