from pathlib import Path

import uvicorn

from righttekit.cli.core.launchers.base import BaseLauncher


class UvicornLauncher(BaseLauncher):
    def __init__(
        self,
        app_target: str | None = None,
        host: str = "127.0.0.1",
        port: int = 8000,
        reload: bool = False,
    ) -> None:
        self.host = host
        self.port = port
        self.reload = reload
        self.app_target = app_target or self._detect_app_target()

    def run(self) -> None:
        uvicorn.run(
            self.app_target,
            host=self.host,
            port=self.port,
            reload=self.reload,
        )

    @staticmethod
    def _detect_app_target() -> str:
        cwd = Path.cwd()
        if (cwd / "main.py").exists():
            return "main:app"
        if (cwd / "app.py").exists():
            return "app:app"
        raise FileNotFoundError(
            "Could not infer an ASGI app. Pass --app explicitly, for example --app main:app."
        )
