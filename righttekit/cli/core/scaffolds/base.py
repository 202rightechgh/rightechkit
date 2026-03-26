from abc import ABC, abstractmethod
from pathlib import Path


class ProjectScaffolder(ABC):
    @abstractmethod
    def scaffold(self, name: str, base_dir: Path) -> Path:
        """Create a project and return its path."""

