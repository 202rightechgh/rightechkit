from pathlib import Path

from righttekit.cli.core.scaffolds.base import ProjectScaffolder


class FastAPIServiceScaffolder(ProjectScaffolder):
    def __init__(self, template_dir: Path) -> None:
        self.template_dir = template_dir

    def scaffold(self, name: str, base_dir: Path) -> Path:
        project_slug = self._slugify(name)
        project_name = self._titleize(name)
        destination = base_dir / project_slug
        destination.mkdir(parents=True, exist_ok=False)

        context = {
            "project_name": project_name,
            "project_slug": project_slug,
        }
        for template in self.template_dir.glob("*.tpl"):
            output_name = template.name.removesuffix(".tpl")
            rendered = template.read_text(encoding="utf-8")
            for key, value in context.items():
                rendered = rendered.replace(f"{{{{ {key} }}}}", value)
            (destination / output_name).write_text(rendered, encoding="utf-8")

        return destination

    @staticmethod
    def _slugify(name: str) -> str:
        return name.strip().lower().replace(" ", "-").replace("_", "-")

    @staticmethod
    def _titleize(name: str) -> str:
        return name.strip().replace("-", " ").replace("_", " ").title()
