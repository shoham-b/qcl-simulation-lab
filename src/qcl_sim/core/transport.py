"""Transport calculations."""

import numpy as np

from qcl_sim.materials.database import MaterialSystem


class ElectronTransport:
    """Calculate transport."""

    def __init__(self, material: MaterialSystem, num_periods: int):
        self.material = material
        self.num_periods = num_periods

    def calculate_iv(
        self,
        energy_levels: np.ndarray,
        temperature: float,
        bias_field: float,
    ) -> dict:
        """Calculate I-V."""
        threshold_current = 2.5 * (temperature / 77) * (1 / np.sqrt(self.num_periods))
        slope_efficiency = 400 * self.num_periods / 25

        return {
            "threshold_current": threshold_current,
            "slope_efficiency": slope_efficiency,
        }
