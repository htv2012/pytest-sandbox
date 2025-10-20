.PHONY: all test lint clean py

### Default target(s)
all: test

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

py:
	uv run ipython

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .
