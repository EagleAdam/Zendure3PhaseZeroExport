from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN
from .api import ZendureApiClient
from .coordinator import ZendureCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Zendure integration from a config entry."""

    account_id = entry.data["account_id"]
    api_token = entry.data["api_token"]
    simulation = entry.data.get("simulation_mode", True)

    client = ZendureApiClient(
        account_id=account_id,
        api_token=api_token,
        simulation=simulation,
    )

    coordinator = ZendureCoordinator(hass, client)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "client": client,
        "coordinator": coordinator,
    }

    # Load platforms
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
