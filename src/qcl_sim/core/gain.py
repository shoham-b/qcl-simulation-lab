"""Optical gain calculations."""

import numpy as np

from qcl_sim.materials.database import MaterialSystem


class OpticalGain:
    """Calculate optical gain."""

    def __init__(self, material: MaterialSystem):
        self.material = material

    def calculate_gain(
        self,
        energy_levels: np.ndarray,
        scattering_rates: dict,
        temperature: float,
        bias_field: float,
    ) -> dict:
        """Calculate gain."""
        peak_gain = 45 * (bias_field / 50) * (300 / temperature)
        linewidth = 12 + temperature / 50

        return {
            "peak_gain": peak_gain,
            "linewidth": linewidth,
        }
