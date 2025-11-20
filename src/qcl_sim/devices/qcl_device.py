"""QCL device model."""

import numpy as np

from qcl_sim.core.band_structure import BandStructure
from qcl_sim.core.gain import OpticalGain
from qcl_sim.core.scattering import ScatteringRates
from qcl_sim.core.transport import ElectronTransport
from qcl_sim.materials.database import MATERIAL_DB, DesignType, MaterialSystem


class QCLDevice:
    """Quantum Cascade Laser device."""

    def __init__(
        self,
        material: MaterialSystem,
        design: DesignType,
        wavelength: float,
        num_periods: int = 25,
        temperature: float = 77.0,
    ):
        self.material = material
        self.design = design
        self.wavelength = wavelength
        self.num_periods = num_periods
        self.temperature = temperature
        self.material_props = MATERIAL_DB[material]

        self.band_structure = BandStructure(material, design)
        self.scattering = ScatteringRates(material, temperature)
        self.gain = OpticalGain(material)
        self.transport = ElectronTransport(material, num_periods)

    def simulate(self, bias_field: float) -> dict:
        """Run simulation."""
        energy_levels = self.band_structure.calculate_levels(self.wavelength, bias_field)
        scattering_rates = self.scattering.calculate_rates(energy_levels, bias_field)
        gain_result = self.gain.calculate_gain(
            energy_levels, scattering_rates, self.temperature, bias_field
        )
        transport_result = self.transport.calculate_iv(
            energy_levels, self.temperature, bias_field
        )

        return {
            "peak_gain": gain_result["peak_gain"],
            "threshold_current": transport_result["threshold_current"],
            "upper_lifetime": scattering_rates["upper_lifetime"],
            "lower_lifetime": scattering_rates["lower_lifetime"],
            "transition_energy": energy_levels[-1] - energy_levels[-2],
            "energy_levels": energy_levels,
            "slope_efficiency": transport_result["slope_efficiency"],
        }
