from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
    CONF_ACCOUNT_ID,
    CONF_API_TOKEN,
    CONF_SIMULATION,
)


class ZendureConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Zendure 3‑Phase Zero Export."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title="Zendure 3‑Phase Zero Export",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_ACCOUNT_ID): str,
                vol.Required(CONF_API_TOKEN): str,
                vol.Optional(CONF_SIMULATION, default=True): bool,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
