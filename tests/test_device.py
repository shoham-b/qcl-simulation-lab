"""Tests for QCL device."""

import pytest

from qcl_sim import DesignType, MaterialSystem, QCLDevice


def test_device_creation():
    """Test device creation."""
    device = QCLDevice(
        material=MaterialSystem.INGAAS_INALAS,
        design=DesignType.VERTICAL,
        wavelength=8.5,
        num_periods=25,
        temperature=77,
    )
    assert device is not None
    assert device.wavelength == 8.5


def test_simulation():
    """Test simulation."""
    device = QCLDevice(
        material=MaterialSystem.GAAS_ALGAAS,
        design=DesignType.DIAGONAL,
        wavelength=10.0,
        num_periods=30,
        temperature=300,
    )
    results = device.simulate(bias_field=50)
    
    assert "peak_gain" in results
    assert "threshold_current" in results
    assert results["peak_gain"] > 0


@pytest.mark.parametrize(
    "material",
    [
        MaterialSystem.INGAAS_INALAS,
        MaterialSystem.GAAS_ALGAAS,
        MaterialSystem.STRAIN_BALANCED,
    ],
)
def test_all_materials(material):
    """Test all materials."""
    device = QCLDevice(
        material=material,
        design=DesignType.VERTICAL,
        wavelength=8.0,
    )
    results = device.simulate(bias_field=45)
    assert results["peak_gain"] > 0
