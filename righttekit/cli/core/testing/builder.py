import sys

from righttekit.cli.core.testing.options import PytestOptions


class PytestCommandBuilder:
    def __init__(self, options: PytestOptions) -> None:
        self.options = options

    def build(self) -> list[str]:
        command = [sys.executable, "-m", "pytest"]
        if self.options.verbose:
            command.append("-v")
        if self.options.coverage:
            command.extend(["--cov=righttekit", "--cov-report=term-missing"])
            if self.options.html_cov:
                command.append("--cov-report=html")
        if self.options.target is not None:
            command.append(str(self.options.target))
        return command
