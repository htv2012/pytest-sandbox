FILE ?= *.py

run: lint
	uv run pytest -s -vv $(FILE)

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

