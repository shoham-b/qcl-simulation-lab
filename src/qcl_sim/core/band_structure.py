"""Band structure calculations."""

import numpy as np

from qcl_sim.materials.database import DesignType, MaterialSystem


class BandStructure:
    """Calculate energy levels."""

    def __init__(self, material: MaterialSystem, design: DesignType):
        self.material = material
        self.design = design

    def calculate_levels(self, wavelength: float, bias_field: float) -> np.ndarray:
        """Calculate energy levels."""
        h = 4.135667696e-15  # eV·s
        c = 2.998e14  # μm/s
        photon_energy = (h * c) / wavelength * 1000  # meV

        if self.design == DesignType.VERTICAL:
            levels = np.array([
                0.0,
                photon_energy * 0.25,
                photon_energy * 0.85,
                photon_energy * 1.85,
            ])
        elif self.design == DesignType.DIAGONAL:
            levels = np.array([
                0.0,
                photon_energy * 0.5,
                photon_energy * 1.2,
                photon_energy * 2.2,
            ])
        else:  # SUPERLATTICE
            levels = np.array([photon_energy * i * 0.6 for i in range(5)])

        field_correction = 1 + bias_field / 200
        return levels * field_correction
