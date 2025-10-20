.PHONY: all test lint clean

### Default target(s)
all: test

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix


### Run unit tests
test: lint
	uv run pytest -s -v
	TEST_PORTS=9001,9002 TEST_SERVERS=env1.com,env2.com uv run pytest -s -v
	uv run pytest --test-servers=cmdline1.com,cmdline2.com --test-ports=8005,8006,8007 -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .
