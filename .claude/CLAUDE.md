# Claude

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Guidelines

- Prioritize using LSP capabilities if possible
- When resolving a TODO, follow its instructions literally
- Run type checking as part of your tasks
- Run specs as part of your tasks
- Run linting as part of your tasks

## Commands

- Run `uv run task lint` to lint the code using Ruff
- Run `uv run task format` to auto-fix formatting issues with Ruff
- Run `uv run task type` to run type checking
- Run `uv run task test` to run the full test suite including linting, type checking, and tests
- Run `uv run task spec` to run only the pytest tests
- Run `uv run pytest path/to/test.py` to run a single test file
- Run `uv run pytest -k "test name"` to run a single test by name

## Formats

- Use 4-space indentation, UTF-8 encoding, and LF line endings
- Use PascalCase for classes, snake_case for functions, methods, and variables
- Place high-level public items first in a file and low-level private items last

## Types

- Use Python type hints; target Python 3.12+
- Never use `Any` without permission

## Specs

- Place unit tests in `test_<module>.py` files and don't add useless comments like "Arrange", "Act", "Assert"

## Docs

- Add docstrings only for public APIs and don't use them for files
- Don't write `#` comments in the code
