.PHONY: all us international lint format

all: lint us international

us:
	uv run pytest -s -v

international:
	uv run pytest -s -v --test-data-files asia.yaml europe.yaml

lint: format
	uv run ruff check . --fix
	
format:
	uv run ruff check --select I --fix .
	uv run ruff format .
