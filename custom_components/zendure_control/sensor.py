"""Simulated output sensors."""

from __future__ import annotations
from homeassistant.helpers.entity import Entity
from homeassistant.core import HomeAssistant
from . import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    entities = []
    for device_id in coordinator.last_simulated_values.keys():
        entities.append(SmartFlowSimulatedPowerSensor(coordinator, device_id))

    async_add_entities(entities)


class SmartFlowSimulatedPowerSensor(Entity):
    def __init__(self, coordinator, device_id):
        self._coordinator = coordinator
        self._device_id = device_id

    @property
    def name(self):
        return f"SmartFlow Simulated Power {self._device_id}"

    @property
    def state(self):
        return self._coordinator.last_simulated_values.get(self._device_id, 0)
