lint:
	pre-commit run -a --hook-stage manual $(hook)

unit-tests:
	echo "Running tests..."
	make install
	make run-unit-tests

integration-tests:
	echo "Running integration tests"
	make install
	make run-integration-tests

install-pre-commit:
	pre-commit install --install-hooks
	pre-commit install --hook-type commit-msg

uninstall-pre-commit:
	pre-commit uninstall

clean:
	rm -rf .venv

install:
	uv sync --frozen --no-install-project
	uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name="{{ project_name }}"

run-unit-tests:
	uv run python -m pytest src/tests

run-integration-tests:
	uv run kedro run --no-sync --pipeline=default --env=test
