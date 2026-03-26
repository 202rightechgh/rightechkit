import sys
from pathlib import Path

from righttekit.cli.core.testing.builder import PytestCommandBuilder
from righttekit.cli.core.testing.options import PytestOptions


def test_builder_includes_requested_flags() -> None:
    options = PytestOptions(
        coverage=True,
        html_cov=True,
        target=Path("tests/cli"),
        verbose=True,
    )

    command = PytestCommandBuilder(options).build()

    assert command == [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "--cov=righttekit",
        "--cov-report=term-missing",
        "--cov-report=html",
        "tests/cli",
    ]
