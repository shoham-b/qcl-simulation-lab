"""Basic QCL simulation example."""

from qcl_sim import DesignType, MaterialSystem, QCLDevice


def main():
    """Run basic simulation."""
    device = QCLDevice(
        material=MaterialSystem.INGAAS_INALAS,
        design=DesignType.VERTICAL,
        wavelength=8.5,
        num_periods=25,
        temperature=77,
    )
    
    results = device.simulate(bias_field=50)
    
    print("\nQCL Simulation Results")
    print("=" * 40)
    print(f"Peak Gain: {results['peak_gain']:.1f} cm⁻¹")
    print(f"Threshold: {results['threshold_current']:.2f} kA/cm²")
    print(f"Upper Lifetime: {results['upper_lifetime']:.2f} ps")
    print(f"Transition Energy: {results['transition_energy']:.1f} meV")


if __name__ == "__main__":
    main()
