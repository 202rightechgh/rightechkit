import click

from righttekit.cli.core.launchers.uvicorn import UvicornLauncher
from righttekit.cli.utils import echo_info


@click.command("launch")
@click.option("--app", "app_target", help="ASGI target in the form module:attribute.")
@click.option("--host", default="127.0.0.1", show_default=True, help="Host to bind.")
@click.option("--port", default=8000, show_default=True, type=int, help="Port to bind.")
@click.option("--reload", is_flag=True, help="Enable autoreload for development.")
def launch_command(
    app_target: str | None,
    host: str,
    port: int,
    reload: bool,
) -> None:
    """Launch a local ASGI application with Uvicorn."""
    launcher = UvicornLauncher(app_target=app_target, host=host, port=port, reload=reload)
    echo_info(f"Launching {launcher.app_target} on http://{host}:{port}")
    launcher.run()

