.PHONY: install test lint format build publish

install:
	poetry install --with dev

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

build:
	poetry build

publish:
	poetry publish
