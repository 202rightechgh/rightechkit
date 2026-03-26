[build-system]
requires = ["hatchling>=1.27.0"]
build-backend = "hatchling.build"

[project]
name = "{{ project_slug }}"
version = "0.1.0"
description = "{{ project_name }} service scaffolded by RightTeKit"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
  "fastapi>=0.116.0",
  "uvicorn>=0.30.0",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.2.0",
]

