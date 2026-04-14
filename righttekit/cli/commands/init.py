from pathlib import Path

import click

from righttekit.cli.core.scaffolds.factory import scaffold_project
from righttekit.cli.utils import echo_info, echo_success


@click.command("init")
@click.argument("name")
@click.option(
    "--type",
    "project_type",
    type=click.Choice(["fastapi"]),
    default="fastapi",
    show_default=True,
    help="Project type to scaffold.",
)
@click.option(
    "--directory",
    type=click.Path(path_type=Path, file_okay=False),
    default=Path("services"),
    show_default=True,
    help="Base directory to create the project in.",
)
def init_command(name: str, project_type: str, directory: Path) -> None:
    """Scaffold a new service project."""
    echo_info(f"Creating {project_type} service '{name}'")
    destination = scaffold_project(
        name=name, project_type=project_type, base_dir=directory
    )
    echo_success(f"Project created at {destination}")
