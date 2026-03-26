from pathlib import Path

import click

from righttekit.cli.core.testing.options import PytestOptions
from righttekit.cli.core.testing.runner import PytestRunner
from righttekit.cli.utils import echo_info


@click.command("test")
@click.option("--coverage", is_flag=True, help="Enable coverage reporting.")
@click.option("--html-cov", is_flag=True, help="Generate htmlcov output.")
@click.option(
    "--file",
    "target",
    type=click.Path(path_type=Path),
    help="Optional file or directory to test.",
)
@click.option("--verbose", is_flag=True, help="Run pytest in verbose mode.")
def test_command(
    coverage: bool,
    html_cov: bool,
    target: Path | None,
    verbose: bool,
) -> None:
    """Run pytest using RightTeKit defaults."""
    echo_info("Running tests")
    options = PytestOptions(
        coverage=coverage,
        html_cov=html_cov,
        target=target,
        verbose=verbose,
    )
    PytestRunner(options).run()
