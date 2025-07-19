# A2A Text Analysis Agent - Development Makefile
# Provides convenient commands for development, testing, and deployment

.PHONY: help install test test-unit test-integration test-coverage lint format check clean build run docker-build docker-run docker-stop docker-clean install-dev setup

# Default target
help: ## Show this help message
	@echo "A2A Text Analysis Agent - Development Commands"
	@echo "=============================================="
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation and Setup
install: ## Install the package in development mode
	uv pip install -e .

install-dev: ## Install development dependencies
	uv pip install -e ".[dev]"

sync: ## Synchronize dependencies with lock file
	@echo "🔄 Synchronizing dependencies..."
	uv sync
	@echo "✅ Dependencies synchronized!"

sync-frozen: ## Synchronize dependencies with frozen lock file (CI/CD)
	@echo "🔄 Synchronizing dependencies (frozen)..."
	uv sync --frozen
	@echo "✅ Dependencies synchronized (frozen)!"

setup: ## Set up the development environment
	uv venv
	@echo "Virtual environment created. Activate it with:"
	@echo "source .venv/bin/activate  # On Linux/Mac"
	@echo ".venv\\Scripts\\activate     # On Windows"
	@echo ""
	@echo "Then run: make install-dev"
	@echo ""
	@echo "Note: uv will automatically manage the virtual environment!"

# Testing
test: ## Run all tests
	uv run python run_tests.py --type all --verbose

test-unit: ## Run unit tests only
	uv run python run_tests.py --type unit --verbose

test-integration: ## Run integration tests only
	uv run python run_tests.py --type integration --verbose

test-coverage: ## Run tests with coverage report
	uv run python run_tests.py --type all --coverage --verbose

test-watch: ## Run tests in watch mode (requires pytest-watch)
	uv run python -m pytest_watch tests/ -- -v

# Code Quality
lint: ## Run linting checks (flake8)
	@echo "🔍 Running linting checks..."
	uv run python -m flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503
	@echo "✅ Linting passed!"

format: ## Format code with black and isort
	@echo "🎨 Formatting code..."
	uv run python -m black src/ tests/ --line-length=88
	uv run python -m isort src/ tests/ --profile=black
	@echo "✅ Code formatted!"

autoflake: ## Remove unused imports and variables
	@echo "🧹 Removing unused imports and variables..."
	uv run python -m autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive src/ tests/
	@echo "✅ Code cleaned!"

check: ## Run all code quality checks
	@echo "🔍 Running code quality checks..."
	@make autoflake
	@make lint
	@make format
	@echo "✅ All code quality checks passed!"

# Type checking
type-check: ## Run type checking with mypy
	@echo "🔍 Running type checks..."
	uv run python -m mypy src/ --ignore-missing-imports
	@echo "✅ Type checking passed!"

# Security checks
security: ## Run security checks with bandit
	@echo "🔒 Running security checks..."
	uv run python -m bandit -r src/ -f json -o bandit-report.json || true
	@echo "✅ Security checks completed!"

# Cleanup
clean: ## Clean up generated files
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	@echo "✅ Cleanup completed!"

# Build and Run
build: ## Build the package
	@echo "📦 Building package..."
	uv run python -m build
	@echo "✅ Package built!"

run: ## Run the A2A server locally
	@echo "🚀 Starting A2A server..."
	uv run python main.py

run-dev: ## Run the server in development mode
	@echo "🚀 Starting A2A server in development mode..."
	LOG_LEVEL=debug uv run python main.py

# Docker Commands
docker-build: ## Build Docker image
	@echo "🐳 Building Docker image..."
	docker compose build --no-cache
	@echo "✅ Docker image built!"

docker-run: ## Run Docker container
	@echo "🐳 Running Docker container..."
	docker compose up -d
	@echo "✅ Container started! Access at http://localhost:10002"

docker-stop: ## Stop Docker container
	@echo "🛑 Stopping Docker container..."
	docker stop a2a-text-analysis-agent || true
	docker rm a2a-text-analysis-agent || true
	@echo "✅ Container stopped!"

docker-clean: ## Clean up Docker resources
	@echo "🧹 Cleaning up Docker resources..."
	docker system prune -f
	@echo "✅ Docker cleanup completed!"

docker-compose-up: ## Start services with Docker Compose
	@echo "🐳 Starting services with Docker Compose..."
	docker compose up -d
	@echo "✅ Services started!"

docker-compose-down: ## Stop services with Docker Compose
	@echo "🛑 Stopping services with Docker Compose..."
	docker compose down
	@echo "✅ Services stopped!"

docker-compose-logs: ## View Docker Compose logs
	docker compose logs -f

# Quality Assurance Pipeline
qa: ## Run complete quality assurance pipeline
	@echo "🔍 Running complete QA pipeline..."
	@make clean
	@make install-dev
	@make check
	@make type-check
	@make security
	@make test-coverage
	@echo "✅ QA pipeline completed!"

# Development Workflow
dev-setup: ## Complete development setup
	@echo "🚀 Setting up development environment..."
	@make setup-env
	@make setup
	@make sync
	@make install-dev
	@make check
	@echo "✅ Development environment ready!"
	@echo "⚠️  Don't forget to add your Google AI API key to .env file!"

# Documentation
docs: ## Generate documentation
	@echo "📚 Generating documentation..."
	uv run python -m pdoc --html src/a2a_text_analysis_agent --output-dir docs
	@echo "✅ Documentation generated in docs/"

# Performance
benchmark: ## Run performance benchmarks
	@echo "⚡ Running performance benchmarks..."
	uv run python -m pytest tests/ -m benchmark --benchmark-only

# Monitoring
monitor: ## Monitor server health
	@echo "📊 Monitoring server health..."
	@while true; do \
		curl -s http://localhost:10002/health > /dev/null && echo "✅ Server healthy" || echo "❌ Server down"; \
		sleep 5; \
	done



# CI/CD Commands
ci-test: ## Run tests for CI/CD pipeline
	uv run python run_tests.py --type all --coverage

ci-lint: ## Run linting for CI/CD pipeline
	uv run python -m flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503 --count --statistics

ci-format: ## Check formatting for CI/CD pipeline
	uv run python -m black --check src/ tests/ --line-length=88

# Utility Commands
check-deps: ## Check for outdated dependencies
	@echo "📦 Checking for outdated dependencies..."
	uv run python -m pip list --outdated

update-deps: ## Update dependencies
	@echo "📦 Updating dependencies..."
	uv run python -m pip install --upgrade -r requirements.txt

env-check: ## Check environment variables
	@echo "🔍 Checking environment variables..."
	@if [ -f .env ]; then \
		echo "✅ .env file found"; \
		cat .env | grep -v "^#" | grep -v "^$$" || echo "No environment variables set"; \
	else \
		echo "❌ .env file not found. Copy from .env.example"; \
	fi

env-setup: ## Set up environment variables
	@echo "🔧 Setting up environment variables..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✅ .env file created from .env.example"; \
	else \
		echo "✅ .env file already exists"; \
	fi

# Helpers
version: ## Show package version
	@uv run python -c "import src.a2a_text_analysis_agent; print(src.a2a_text_analysis_agent.__version__)" 2>/dev/null || echo "Version: 0.1.0"

version-sync: ## Sync version from pyproject.toml to __init__.py
	@echo "🔄 Syncing version..."
	@VERSION=$$(uv run python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])") && \
	echo "Version from pyproject.toml: $$VERSION" && \
	sed -i "s/__version__ = \".*\"/__version__ = \"$$VERSION\"/" src/a2a_text_analysis_agent/__init__.py && \
	echo "✅ Version synced to __init__.py"

info: ## Show project information
	@echo "📋 Project Information"
	@echo "====================="
	@echo "Package: A2A Text Analysis Agent"
	@make version
	@echo "Python: $(shell uv run python --version 2>/dev/null || echo 'Not available')"
	@echo "Pip: $(shell uv run python -m pip --version 2>/dev/null || echo 'Not available')"
	@echo "Docker: $(shell docker --version 2>/dev/null || echo 'Not installed')"
	@echo "Docker Compose: $(shell docker compose version 2>/dev/null || echo 'Not installed')" 