"""Scattering calculations."""

import numpy as np

from qcl_sim.materials.database import MATERIAL_DB, MaterialSystem


class ScatteringRates:
    """Calculate scattering rates."""

    def __init__(self, material: MaterialSystem, temperature: float):
        self.material = material
        self.temperature = temperature
        self.props = MATERIAL_DB[material]

    def calculate_rates(self, energy_levels: np.ndarray, bias_field: float) -> dict:
        """Calculate rates."""
        upper_lifetime = 3.2 * (1 + bias_field / 100) * (self.temperature / 77) ** 0.5
        lower_lifetime = 0.5 * (1 - bias_field / 200) * (77 / self.temperature) ** 0.3

        return {
            "upper_lifetime": upper_lifetime,
            "lower_lifetime": lower_lifetime,
            "lo_phonon_rate": 1 / upper_lifetime,
        }
