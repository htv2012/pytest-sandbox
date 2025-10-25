all: lint
	uv run pytest -s -v

lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet


