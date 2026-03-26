import click

from righttekit.cli.commands.init import init_command
from righttekit.cli.commands.launch import launch_command
from righttekit.cli.commands.test import test_command
from righttekit.cli.commands.version import version_command


@click.group()
def cli() -> None:
    """RightTeKit CLI for scaffolding, launching, and testing services."""


cli.add_command(init_command)
cli.add_command(launch_command)
cli.add_command(version_command)
cli.add_command(test_command)

