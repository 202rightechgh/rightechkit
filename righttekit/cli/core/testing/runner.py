import subprocess

from righttekit.cli.core.testing.builder import PytestCommandBuilder
from righttekit.cli.core.testing.options import PytestOptions


class PytestRunner:
    def __init__(self, options: PytestOptions) -> None:
        self.options = options

    def run(self) -> None:
        command = PytestCommandBuilder(self.options).build()
        raise SystemExit(subprocess.call(command))
