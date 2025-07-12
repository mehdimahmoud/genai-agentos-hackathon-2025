# Contributing to A2A Text Analysis Agent

Thank you for your interest in contributing to the A2A Text Analysis Agent! This guide will help you understand the development workflow, available commands, and best practices.

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- `uv` (modern Python package manager) - [Install here](https://docs.astral.sh/uv/getting-started/installation/)
- Docker (optional, for containerized development)
- Make (for development commands)

### First-Time Setup
```bash
# Clone the repository
git clone <repository-url>
cd a2a-server

# Complete development setup (recommended)
make dev-setup

# Or step by step:
make setup          # Create virtual environment
make sync           # Synchronize dependencies
make install-dev    # Install development dependencies
make env-setup      # Set up environment variables
```

## 📋 Development Commands

### Project Setup & Installation

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make setup` | Create virtual environment | First time setup |
| `make sync` | Synchronize dependencies with lock file | After dependency changes, team updates |
| `make sync-frozen` | Synchronize with frozen lock file | CI/CD pipelines, production builds |
| `make install` | Install package in development mode | After setup |
| `make install-dev` | Install development dependencies | Development setup |
| `make dev-setup` | Complete development setup | First time, fresh environment |

### Testing

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make test` | Run all tests | Before commits, CI/CD |
| `make test-unit` | Run unit tests only | Quick development feedback |
| `make test-integration` | Run integration tests only | A2A protocol testing |
| `make test-coverage` | Run tests with coverage report | Quality assurance |
| `make test-watch` | Run tests in watch mode | Active development |
| `make quick-test` | Quick test run | Fast feedback |

### Code Quality

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make lint` | Run linting checks (flake8) | Before commits, code review |
| `make format` | Format code with black and isort | Before commits |
| `make autoflake` | Remove unused imports and variables | Code cleanup |
| `make check` | Run all code quality checks | Before commits, CI/CD |
| `make type-check` | Run type checking with mypy | Type safety verification |
| `make security` | Run security checks with bandit | Security audit |
| `make quick-lint` | Quick lint check | Fast feedback |
| `make quick-format` | Quick format check | Fast feedback |

### Development Workflow

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make run` | Run the A2A server locally | Local development |
| `make run-dev` | Run server in development mode | Debugging |
| `make qa` | Run complete quality assurance pipeline | Before releases |
| `make clean` | Clean up generated files | Troubleshooting |
| `make build` | Build the package | Distribution |

### Docker Development

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make docker-build` | Build Docker image | Container development |
| `make docker-run` | Run Docker container | Container testing |
| `make docker-stop` | Stop Docker container | Cleanup |
| `make docker-clean` | Clean up Docker resources | System cleanup |
| `make docker-compose-up` | Start services with Docker Compose | Full stack development |
| `make docker-compose-down` | Stop services with Docker Compose | Cleanup |
| `make docker-compose-logs` | View Docker Compose logs | Debugging |

### Environment & Configuration

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make env-setup` | Set up environment variables | First time setup |
| `make env-check` | Check environment variables | Troubleshooting |
| `make check-deps` | Check for outdated dependencies | Maintenance |
| `make update-deps` | Update dependencies | Maintenance |

### Utility Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `make help` | Show all available commands | Reference |
| `make version` | Show package version | Version checking |
| `make info` | Show project information | System info |
| `make docs` | Generate documentation | Documentation |
| `make benchmark` | Run performance benchmarks | Performance testing |
| `make monitor` | Monitor server health | Production monitoring |

## 🔄 Development Workflow

### Daily Development Cycle

1. **Start of Day**
   ```bash
   git pull
   make sync          # Ensure dependencies are up to date
   make test          # Verify everything still works
   ```

2. **Feature Development**
   ```bash
   # Create feature branch
   git checkout -b feature/your-feature-name
   
   # Make changes, then:
   make format        # Format your code
   make lint          # Check for issues
   make test          # Run tests
   make type-check    # Verify types
   ```

3. **Before Committing**
   ```bash
   make check         # Run all quality checks
   make test          # Run all tests
   make test-coverage # Check coverage
   ```

4. **Before Pull Request**
   ```bash
   make qa            # Complete quality assurance
   make docs          # Update documentation if needed
   ```

### When to Use Specific Commands

#### `uv sync` vs `uv pip install`

- **Use `uv sync`** when:
  - You've modified `pyproject.toml`
  - You've pulled changes that include dependency updates
  - You want to ensure exact dependency versions
  - Setting up a fresh environment

- **Use `uv pip install`** when:
  - Installing specific packages temporarily
  - Testing new dependencies
  - Quick one-off installations

#### Testing Strategy

- **`make test-unit`**: During active development for quick feedback
- **`make test-integration`**: When working on A2A protocol features
- **`make test-coverage`**: Before commits to ensure good coverage
- **`make test-watch`**: During active development for continuous feedback

#### Code Quality Pipeline

- **`make format`**: Always before committing
- **`make lint`**: Before commits and during code review
- **`make type-check`**: For type safety verification
- **`make security`**: Before releases and security audits

## 🏗️ Project Structure

```
a2a-server/
├── src/
│   └── a2a_text_analysis_agent/
│       ├── agents/          # Agent implementations
│       ├── core/            # Core agent functionality
│       ├── protocol/        # A2A protocol implementation
│       ├── schemas/         # A2A protocol schemas
│       ├── services/        # Server and service layer
│       ├── tools/           # Text analysis tools
│       └── utils/           # Utility functions
├── tests/                   # Comprehensive test suite
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── main.py                 # Application entry point
├── pyproject.toml          # Project configuration
├── requirements.txt         # Runtime dependencies
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Docker Compose setup
├── Makefile                # Development commands
└── README.md              # Project documentation
```

## 🧪 Testing Guidelines

### Unit Tests
- Test individual functions and classes
- Mock external dependencies
- Focus on business logic
- Fast execution

### Integration Tests
- Test A2A protocol compliance
- Test agent communication
- Test end-to-end workflows
- Use real protocol schemas

### Test Naming Convention
- Files: `test_*.py`
- Classes: `Test*`
- Methods: `test_*`

### Running Tests
```bash
# All tests
make test

# Specific test file
uv run python -m pytest tests/unit/test_text_analysis_agent.py

# With coverage
make test-coverage

# Watch mode for development
make test-watch
```

## 🔧 Configuration Management

### Environment Variables
- **Development**: Use `.env` file (not committed)
- **Production**: Use environment variables or secure config management
- **Docker**: Use `docker-compose.yml` environment section

### Dependency Management
- **Runtime**: `requirements.txt` for deployment
- **Development**: `pyproject.toml` with `[project.optional-dependencies]`
- **Lock File**: `uv.lock` for reproducible builds

## 🐳 Docker Development

### Local Development with Docker
```bash
# Build and run with Docker Compose
make docker-compose-up

# View logs
make docker-compose-logs

# Stop services
make docker-compose-down
```

### Docker Best Practices
- Use multi-stage builds for production
- Keep images small and secure
- Use non-root users
- Proper health checks

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8
- Use type hints
- Docstrings for public APIs
- Maximum line length: 88 characters

### Import Organization
```python
# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import requests
from typing import Optional

# Local imports
from .core.agent import Agent
from .utils.helpers import helper_function
```

### Naming Conventions
- **Classes**: `PascalCase` (e.g., `TextAnalysisAgent`)
- **Functions/Methods**: `snake_case` (e.g., `analyze_text`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_PORT`)
- **Files**: `snake_case` (e.g., `text_analysis_agent.py`)

## 🔍 Debugging Tips

### Common Issues

1. **Import Errors**
   ```bash
   make clean
   make sync
   make install-dev
   ```

2. **Test Failures**
   ```bash
   make test-unit -- -v  # Verbose output
   make test-integration -- -s  # Show print statements
   ```

3. **Docker Issues**
   ```bash
   make docker-clean
   make docker-build --no-cache
   ```

### Debugging Commands
```bash
# Check environment
make env-check

# Check dependencies
make check-deps

# Monitor server
make monitor

# View logs
make docker-compose-logs
```

## 🚀 Release Process

### Pre-Release Checklist
1. `make qa` - Complete quality assurance
2. `make test-coverage` - Ensure good coverage
3. `make security` - Security audit
4. `make docs` - Update documentation
5. `make build` - Test package build

### Release Steps
1. Update version in `pyproject.toml`
2. Create release branch
3. Run full test suite
4. Update CHANGELOG.md
5. Create pull request
6. Merge and tag release

## 🤝 Contributing Guidelines

### Pull Request Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run quality checks: `make qa`
5. Run tests: `make test`
6. Update documentation if needed
7. Submit pull request

### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No security issues
- [ ] Performance considerations
- [ ] Error handling appropriate

## 📚 Additional Resources

- [A2A Protocol Specification](https://developers.google.com/assistant/conversational/agent-to-agent)
- [Google ADK Documentation](https://developers.google.com/assistant/conversational/agent-development-kit)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Packaging User Guide](https://packaging.python.org/)

## 🆘 Getting Help

- Check existing issues and pull requests
- Search documentation
- Run `make help` for command reference
- Ask questions in discussions

Thank you for contributing to the A2A Text Analysis Agent! 🎉 