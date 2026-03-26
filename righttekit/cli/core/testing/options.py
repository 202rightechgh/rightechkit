from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PytestOptions:
    coverage: bool = False
    html_cov: bool = False
    target: Path | None = None
    verbose: bool = False
