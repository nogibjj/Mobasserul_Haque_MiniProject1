# Define variables
PYTHON = python
PYLINT = pylint
BLACK = black
PYTEST = pytest
DOCKER = docker

# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Format code using Black
format:
	$(BLACK) *.py

# Lint code using Pylint
lint:
	$(PYLINT) --disable=R,C --ignore-patterns=test_*?py *.py

# Run tests using Pytest
test:
	$(PYTHON) -m pytest --cov=palindrome_checker test_palindrome_checker.py

# Build Docker image
docker-build:
	$(DOCKER) build -f .devcontainer/Dockerfile -t python-dev .

# Run Docker container
docker-run:
	$(DOCKER) run --rm -v "$(PWD)":/workspace -p 8000:8000 python-dev

# Default target
all: install format lint test
