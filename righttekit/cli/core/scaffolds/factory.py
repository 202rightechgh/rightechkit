from pathlib import Path

from righttekit.cli.core.scaffolds.base import ProjectScaffolder
from righttekit.cli.core.scaffolds.fastapi import FastAPIServiceScaffolder


class ProjectScaffolderFactory:
    @staticmethod
    def create(project_type: str = "fastapi") -> ProjectScaffolder:
        if project_type != "fastapi":
            raise ValueError(f"Unsupported project type: {project_type}")
        template_dir = Path(__file__).resolve().parent.parent / "templates" / "fastapi"
        return FastAPIServiceScaffolder(template_dir=template_dir)


def scaffold_project(name: str, project_type: str, base_dir: Path) -> Path:
    scaffolder = ProjectScaffolderFactory.create(project_type)
    return scaffolder.scaffold(name=name, base_dir=base_dir)

