from pathlib import Path

from righttekit.cli.core.scaffolds.fastapi import FastAPIServiceScaffolder


def test_fastapi_scaffolder_renders_files(tmp_path: Path) -> None:
    template_dir = (
        Path(__file__).resolve().parents[3]
        / "righttekit"
        / "cli"
        / "core"
        / "templates"
        / "fastapi"
    )
    scaffolder = FastAPIServiceScaffolder(template_dir=template_dir)

    destination = scaffolder.scaffold(name="Billing API", base_dir=tmp_path)

    assert destination.name == "billing-api"
    assert (destination / "main.py").exists()
    assert 'title="Billing Api"' in (destination / "main.py").read_text(encoding="utf-8")
    assert "billing-api" in (destination / "README.md").read_text(encoding="utf-8")
