.PHONY: test

test_license:
	uv run ruff format .
	uv run ruff check --select I --fix .
	uv run ruff check --fix .
	@echo "\n#"
	@echo "# Test all licenses"
	@echo "#"
	uv run pytest --no-header -v
	@echo "\n#"
	@echo "# Skip trial license"
	@echo "#"
	uv run pytest --no-header -v -m "not license(license_kind='trial')" 
	@echo "\n#"
	@echo "# Only trial license"
	@echo "#"
	uv run pytest --no-header -v -m "license(license_kind='trial')" 

