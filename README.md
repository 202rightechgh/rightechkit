# RightTeKit

RightTeKit is a clean Python toolkit for bootstrapping and running backend services with a
simple CLI:

```bash
right init billing-api
cd services/billing-api
right launch --reload
```

## What it includes

- `right init` for scaffolding a FastAPI service
- `right launch` for running a local app with Uvicorn
- `right test` for consistent pytest execution
- `right version` for package and CLI version info

## Why this repo exists

This project takes the useful parts of a larger internal-style toolkit and starts from a
smaller, cleaner base:

- no import-time side effects
- no unfinished CLI options shipped as if they work
- standard `pyproject.toml` metadata instead of tool-specific packaging lock-in
- straightforward templates instead of a heavy scaffolding stack

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## Using With Poetry

You do not push a package "to Poetry". You push this code to a git repository, and then
Poetry can install it from that repository because this project already uses standard
`pyproject.toml` metadata.

Push the code to your remote:

```bash
git add .
git commit -m "Initial RightTeKit package"
git remote add origin <your-repo-url>
git push -u origin main
```

Install it in another project with Poetry:

```bash
poetry add git+https://github.com/<org>/<repo>.git
```

Pin to a tag or branch when you want a stable install target:

```bash
poetry add git+https://github.com/<org>/<repo>.git#v0.1.0
poetry add git+https://github.com/<org>/<repo>.git#main
```

## CLI

### `right init`

Creates a FastAPI service in `services/<name>` by default.

```bash
right init billing-api
right init billing-api --directory .
```

### `right launch`

Runs a local ASGI app. By default it looks for `main:app` in the current directory.

```bash
right launch
right launch --app main:app --reload --port 8080
```

### `right test`

Wraps pytest with a few ergonomic flags.

```bash
right test
right test --coverage --html-cov
right test --file tests/cli
```

## Project layout

```text
righttekit/
├── righttekit/               # Python package
│   └── cli/                  # CLI commands and helpers
├── tests/                    # Unit tests
└── docs/                     # Lightweight project docs
```

## License

Apache 2.0. See [LICENSE](./LICENSE).
