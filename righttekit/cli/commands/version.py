import click

from righttekit.version import __version__


@click.command("version")
def version_command() -> None:
    """Print the RightTeKit version."""
    click.echo(__version__)

