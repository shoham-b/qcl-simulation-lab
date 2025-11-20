"""Material systems and properties."""

from enum import Enum
from typing import NamedTuple


class MaterialSystem(Enum):
    """Material systems."""
    INGAAS_INALAS = "ingaas_inalas"
    GAAS_ALGAAS = "gaas_algaas"
    STRAIN_BALANCED = "strain_balanced"


class DesignType(Enum):
    """Design types."""
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"
    SUPERLATTICE = "superlattice"


class MaterialProperties(NamedTuple):
    """Material properties."""
    effective_mass: float
    barrier_height: float
    lo_phonon_energy: float
    refractive_index: float
    thermal_conductivity: float


MATERIAL_DB = {
    MaterialSystem.INGAAS_INALAS: MaterialProperties(
        effective_mass=0.043,
        barrier_height=0.52,
        lo_phonon_energy=34.0,
        refractive_index=3.3,
        thermal_conductivity=5.0,
    ),
    MaterialSystem.GAAS_ALGAAS: MaterialProperties(
        effective_mass=0.067,
        barrier_height=0.28,
        lo_phonon_energy=36.0,
        refractive_index=3.27,
        thermal_conductivity=45.0,
    ),
    MaterialSystem.STRAIN_BALANCED: MaterialProperties(
        effective_mass=0.041,
        barrier_height=0.60,
        lo_phonon_energy=33.5,
        refractive_index=3.35,
        thermal_conductivity=4.5,
    ),
}
