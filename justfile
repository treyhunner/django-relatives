# Show available commands
_default:
    @printf 'Automation tasks:\n'
    @just --list --unsorted --list-heading '' --list-prefix '  - '

# Install dependencies and set up dev environment
setup:
    uv sync --all-groups

# Run tests on current Python
test *args:
    uv run python runtests.py {{ args }}

# Run tests with coverage
test-cov:
    uv run coverage run runtests.py
    uv run coverage report
    uv run coverage html

# Run full tox test matrix
test-matrix:
    uv run tox -p

# Format code with ruff
format:
    uv run ruff check --fix
    uv run ruff format

# Lint source code
lint:
    uv run ruff check
    uv run ruff format --check

# Run all checks (format, lint, test)
check: format lint test

# Build Sphinx docs
docs:
    uv run sphinx-build -W -b dirhtml docs docs/_build

# Build the package
build:
    uv sync  # Force uv version error if applicable
    uv build --clear

# Publish to PyPI
publish:
    uv publish

# Bump version (usage: just bump patch|minor|major)
bump value:
    uv version --bump {{ value }}

# Make Django migrations
makemigrations:
    uv run python runtests.py makemigrations
