# QCL Simulation Laboratory 🔬⚛️

Quantum Cascade Laser simulation framework in Python.

## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
make install
```

## Usage

```bash
# Run simulation
uv run qcl-sim simulate --material ingaas --wavelength 8.5

# Run tests
make test

# Run example
python examples/basic_simulation.py
```

## Features

- Multiple material systems (InGaAs, GaAs, strain-balanced)
- Band structure calculations
- Gain spectrum analysis
- I-V characteristics
- Rich CLI interface

## Project Structure

```
qcl-simulation-lab/
├── src/qcl_sim/          # Main package
│   ├── core/             # Physics modules
│   ├── devices/          # Device models
│   └── materials/        # Material database
├── tests/                # Test suite
├── examples/             # Usage examples
├── pyproject.toml        # Project config
└── Makefile              # Build commands
```
