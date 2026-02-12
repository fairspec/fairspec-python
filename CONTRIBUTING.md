---
title: Contributing
sidebar:
  order: 2
---

Thank you for your interest in contributing to Fairspec Python! This document provides guidelines and instructions for contributing to this project.

## Project Overview

Project is a monorepo with the following packages:

- `fairspec-metadata`: Core metadata functionality
- `fairspec-dataset`: File-related functionality
- `fairspec-table`: Table-related functionality
- `fairspec-library`: All the above functionality
- `fairspec-terminal`: Terminal interface
- `fairspec`: Meta-package that re-exports the underlying functionality

## Development Environment

### Prerequisites

- **Python**: v3.12 or higher
- **uv**: v0.7.0 or higher

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/fairspec-python.git fairspec-python
   cd fairspec-python
   ```

2. Install dependencies
   ```bash
   uv run task install
   ```

## Development Workflow

### Code Style and Quality

We use Ruff for linting and formatting, and ty for type checking:

- **Lint**: Check for code issues
  ```bash
  uv run task lint
  ```

- **Format**: Auto-fix formatting issues
  ```bash
  uv run task format
  ```

- **Type Check**: Verify Python types
  ```bash
  uv run task type
  ```

### Testing

Tests are collocated with the code and use pytest:

- **Run All Tests**: (includes linting and type checking)
  ```bash
  uv run task test
  ```

- **Run Tests Only**: (without linting/type checking)
  ```bash
  uv run task spec
  ```

- **Run a Specific Test**:
  ```bash
  uv run pytest path/to/test_spec.py
  ```

## Code Style Guidelines

- Use Python with strict type checking
- Target Python 3.12+
- Tests should be placed in `*_spec.py` files alongside the code
- Use 4-space indentation, UTF-8 encoding, and LF line endings
- Use PascalCase for classes, snake_case for functions, methods, and variables

## Making Changes to the Meta-Package

When adding new functionality:

1. Add it to the appropriate package first
2. Ensure it's properly exported from that package
3. No additional work is needed for the meta-package as it automatically re-exports everything

## Submitting Changes

1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Make your changes with appropriate tests
3. Ensure the code passes all checks: `uv run task test`
4. Commit your changes with a descriptive message
5. Submit a pull request

## License

By contributing to Fairspec Python, you agree that your contributions will be licensed under the project's license.

Thank you for your contribution!
