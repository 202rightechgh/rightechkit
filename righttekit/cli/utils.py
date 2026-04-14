from pathlib import Path

import click


def echo_info(message: str) -> None:
    click.secho(message, fg="cyan")


def echo_success(message: str) -> None:
    click.secho(message, fg="green")


def echo_warning(message: str) -> None:
    click.secho(message, fg="yellow")


def project_root() -> Path:
    return Path.cwd()
