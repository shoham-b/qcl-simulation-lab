# QCL Simulation Lab Makefile

.PHONY: help install lint format test coverage run clean

help:
	@echo "QCL Simulation Lab - Available targets:"
	@echo "  install  - Install dependencies with uv"
	@echo "  lint     - Run ruff linter"
	@echo "  format   - Format code with ruff"
	@echo "  test     - Run test suite"
	@echo "  coverage - Run tests with coverage"
	@echo "  run      - Run example simulation"
	@echo "  clean    - Remove build artifacts"

install:
	uv sync --group dev

lint:
	uv run ruff format --check
	uv run ruff check

format:
	uv run ruff format
	uv run ruff check --fix

test:
	uv run pytest -q

coverage:
	uv run pytest --cov=qcl_sim --cov-report=term-missing --cov-report=html

run:
	uv run qcl-sim simulate --material ingaas --wavelength 8.5

clean:
	rm -rf build/ dist/ *.egg-info .coverage htmlcov/ .pytest_cache/ .ruff_cache/
