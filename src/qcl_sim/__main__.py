"""Command-line interface."""

import typer
from rich.console import Console
from rich.table import Table

from qcl_sim.devices.qcl_device import QCLDevice
from qcl_sim.materials.database import DesignType, MaterialSystem

app = typer.Typer(help="QCL Simulation Laboratory")
console = Console()


@app.command()
def simulate(
    material: str = typer.Option("ingaas", help="Material (ingaas/gaas/strain)"),
    design: str = typer.Option("vertical", help="Design (vertical/diagonal/superlattice)"),
    wavelength: float = typer.Option(8.5, help="Wavelength (μm)"),
    temperature: float = typer.Option(77, help="Temperature (K)"),
    bias_field: float = typer.Option(50, help="Bias field (kV/cm)"),
    num_periods: int = typer.Option(25, help="Number of periods"),
):
    """Run QCL simulation."""
    console.print("\n[bold cyan]QCL Simulation Laboratory[/bold cyan]")
    console.print("=" * 50)

    material_map = {
        "ingaas": MaterialSystem.INGAAS_INALAS,
        "gaas": MaterialSystem.GAAS_ALGAAS,
        "strain": MaterialSystem.STRAIN_BALANCED,
    }
    design_map = {
        "vertical": DesignType.VERTICAL,
        "diagonal": DesignType.DIAGONAL,
        "superlattice": DesignType.SUPERLATTICE,
    }

    device = QCLDevice(
        material=material_map[material],
        design=design_map[design],
        wavelength=wavelength,
        num_periods=num_periods,
        temperature=temperature,
    )

    console.print(f"\n[green]Configuration:[/green]")
    console.print(f"  Material: {material}")
    console.print(f"  Design: {design}")
    console.print(f"  Wavelength: {wavelength} μm")

    console.print(f"\n[yellow]Running simulation...[/yellow]")
    results = device.simulate(bias_field=bias_field)

    table = Table(title="\nResults")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Peak Gain", f"{results['peak_gain']:.1f} cm⁻¹")
    table.add_row("Threshold Current", f"{results['threshold_current']:.2f} kA/cm²")
    table.add_row("Upper Lifetime", f"{results['upper_lifetime']:.2f} ps")
    table.add_row("Transition Energy", f"{results['transition_energy']:.1f} meV")

    console.print(table)
    console.print("\n[green]✓ Complete![/green]\n")


@app.command()
def info():
    """Show information."""
    console.print("\n[bold cyan]QCL Simulation Laboratory v0.1.0[/bold cyan]")
    console.print("\nPython framework for quantum cascade laser simulation.\n")


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
