# A2A Text Analysis Agent

A proper A2A (Agent-to-Agent Protocol) compliant text analysis agent that follows the A2A protocol specification and uses Google ADK for seamless integration with the A2A ecosystem.

**Author**: Mehdi K.

## 🏗️ Enterprise-Grade Architecture

This project follows enterprise-grade best practices with a well-structured, modular architecture:

```
a2a-server/
├── src/
│   └── a2a_text_analysis_agent/
│       ├── __init__.py                 # Main package exports
│       ├── main.py                     # Application entry point
│       ├── agents/                     # Agent implementations
│       │   └── text_analysis_agent.py  # Main agent implementation
│       ├── protocol/                   # A2A protocol implementation
│       │   └── a2a_types.py          # A2A protocol types
│       ├── schemas/                    # A2A protocol schemas
│       │   └── a2a_schemas.py        # A2A schema classes
│       ├── services/                   # Server and service layer
│       │   └── a2a_server.py         # A2A server configuration
│       └── tools/                      # Text analysis tools
│           ├── __init__.py            # Tool exports
│           ├── grammar_checker.py     # Grammar analysis tool
│           ├── sentiment_analyzer.py  # Sentiment analysis tool
│           ├── statistics_analyzer.py # Text statistics tool
│           ├── summarizer.py          # Text summarization tool
│           ├── paraphraser.py         # Text paraphrasing tool
│           └── entity_extractor.py    # Entity extraction tool
├── tests/                              # Comprehensive test suite
│   ├── unit/                          # Unit tests
│   │   └── test_text_analysis_agent.py
│   └── integration/                   # Integration tests
│       └── test_a2a_integration.py
├── main.py                            # Main entry point
├── pyproject.toml                     # Project configuration (dependencies & metadata)
├── Dockerfile                         # Container configuration
├── docker-compose.yml                 # Docker Compose setup
├── .env.example                       # Environment variables template
├── .gitignore                         # Git ignore rules
├── .flake8                            # Flake8 configuration
├── run_tests.py                       # Test runner
├── start.sh                           # Docker startup script
├── remove-image.sh                    # Docker cleanup script
├── Makefile                           # Development commands
├── README-A2A.md                      # This file
├── README-PROJECT-STRUCTURE.md        # Project structure documentation
└── CONTRIBUTING.md                    # Development guidelines
```

## 🚀 Features

### Core Capabilities
- **Grammar Checking**: Identifies grammar issues and provides improvement suggestions
- **Text Summarization**: Creates concise summaries of longer texts
- **Sentiment Analysis**: Determines emotional tone and sentiment with confidence scoring
- **Text Statistics**: Provides detailed metrics including word count, reading time, and structure analysis
- **Text Paraphrasing**: Rewrites text in different styles (formal, casual, academic, simple)
- **Entity Extraction**: Identifies and categorizes named entities like people, organizations, locations, dates

### A2A Protocol Compliance
- ✅ Follows A2A protocol specification
- ✅ Uses Google ADK for seamless integration
- ✅ Proper agent card format with skills and capabilities
- ✅ Standardized message handling
- ✅ Independent from backend dependencies

## 🛠️ Installation & Development

### Modern Python Packaging
This project follows modern Python packaging standards:
- **`pyproject.toml`**: Single source of truth for project metadata and dependencies
- **No `requirements.txt`**: Using modern PEP 517/518 compliant packaging
- **`uv`**: Modern, fast Python package manager (10-100x faster than pip)

### Prerequisites
- Python 3.12+
- `uv` (modern Python package manager) - [Install here](https://docs.astral.sh/uv/getting-started/installation/)
- Docker (optional, for containerized deployment)
- Make (for development commands)

### Quick Start (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd a2a-server

# Complete development setup
make dev-setup

# Or step by step:
make setup          # Create virtual environment
make install-dev    # Install development dependencies
make env-setup      # Set up environment variables
```

### Or Manual Installation
```bash
# Clone the repository
git clone <repository-url>
cd a2a-server

# Set up development environment with uv
uv venv
uv pip install -e ".[dev]"

# Or install production dependencies only
uv pip install -e .
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t a2a-text-analysis-agent .
docker run -p 10002:10002 a2a-text-analysis-agent
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file based on `.env.example`:

```bash
# A2A Server Configuration
A2A_SERVER_HOST=0.0.0.0
A2A_SERVER_PORT=10002

# Agent URL (used in agent card)
A2A_AGENT_URL=http://host.docker.internal:10002/

# Logging Configuration
LOG_LEVEL=debug
```

### Docker Configuration
The `docker-compose.yml` includes proper networking configuration for A2A integration.

## 🧪 Testing & Code Quality

### Quick Commands with Makefile
```bash
# Show all available commands
make help

# Run all tests
make test

# Run specific test types
make test-unit
make test-integration
make test-coverage

# Code quality checks
make lint          # Run flake8 linting
make format        # Format code with black and isort
make check         # Run all code quality checks
make type-check    # Run mypy type checking
make security      # Run security checks with bandit

# Complete QA pipeline
make qa            # Run all quality checks and tests
```

> 📖 **For detailed development workflow and command explanations, see [CONTRIBUTING.md](CONTRIBUTING.md)**

### Or Manual Testing Commands
```bash
# Run all tests
uv run python run_tests.py

# Run specific test categories
uv run python -m pytest tests/unit/
uv run python -m pytest tests/integration/

# Run with coverage
uv run python -m pytest --cov=src/a2a_text_analysis_agent tests/
```

### Test Structure
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test A2A protocol compliance and communication
- **Schema Tests**: Validate A2A protocol schema compliance

### Code Quality Tools
- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security analysis
- **pytest**: Testing framework

## 📡 API Endpoints

### A2A Protocol Endpoints
- `GET /.well-known/agent.json` - Agent discovery endpoint
- `POST /a2a/execute` - Task execution endpoint
- `POST /a2a/cancel` - Task cancellation endpoint

### Health Check
- `GET /health` - Server health status

## 🔄 A2A Integration

### Agent Discovery
The agent exposes its capabilities via the `/.well-known/agent.json` endpoint:

```json
{
  "name": "Text Analysis Agent",
  "description": "A versatile text analysis agent...",
  "version": "0.1.0",
  "url": "http://host.docker.internal:10002/",
  "skills": [
    {
      "id": "grammar_check",
      "name": "Grammar Checker",
      "description": "Analyzes writing quality...",
      "inputModes": ["text"],
      "outputModes": ["text"]
    }
  ],
  "capabilities": {
    "streaming": true,
    "pushNotifications": false,
    "stateTransitionHistory": false
  }
}
```

### Task Execution
The agent accepts A2A protocol messages and returns structured responses:

```json
{
  "task": "Check the grammar in this text",
  "text": "The cat sleep on the mat."
}
```

## 🏭 Production Deployment

### Docker Compose
```bash
# Production deployment
docker-compose -f docker-compose.yml up -d

# View logs
docker-compose logs -f text-analysis-agent
```

### Kubernetes
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: a2a-text-analysis-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: a2a-text-analysis-agent
  template:
    metadata:
      labels:
        app: a2a-text-analysis-agent
    spec:
      containers:
      - name: a2a-text-analysis-agent
        image: a2a-text-analysis-agent:latest
        ports:
        - containerPort: 10002
        env:
        - name: A2A_SERVER_HOST
          value: "0.0.0.0"
        - name: A2A_SERVER_PORT
          value: "10002"
```

## 🔍 Troubleshooting

### Common Issues

1. **Agent not discovered by master agent**
   - Check network connectivity between containers
   - Verify `host.docker.internal` resolution
   - Ensure agent URL is accessible

2. **A2A protocol errors**
   - Verify agent card format compliance
   - Check skill definitions match A2A specification
   - Validate message format

3. **Docker networking issues**
   - Add `extra_hosts` in docker-compose.yml
   - Use proper network aliases
   - Check DNS resolution

### Debug Mode
Enable debug mode for detailed logging:

```bash
LOG_LEVEL=debug uv run python main.py
```

## 🚀 Extensibility & Multi-Agent Support

This project is designed with extensibility in mind and can be extended to support multiple A2A agents. The modular architecture makes it easy to add new agents with different capabilities.

### Multi-Agent Architecture

The current structure can be extended to support multiple agents by:

1. **Agent Registry**: Implement a central agent registry that manages multiple A2A agents
2. **Load Balancing**: Route requests to appropriate agents based on capabilities
3. **Agent Discovery**: Enhanced discovery mechanism for multiple agents
4. **Shared Infrastructure**: Common services, logging, and monitoring across agents

### Example Multi-Agent Setup

```python
# Future implementation example
class MultiAgentServer:
    def __init__(self):
        self.agents = {
            "text-analysis": TextAnalysisAgent(),
            "image-processing": ImageProcessingAgent(),
            "data-analysis": DataAnalysisAgent(),
            "code-review": CodeReviewAgent()
        }
    
    async def route_request(self, request):
        # Route to appropriate agent based on task type
        agent = self.select_agent(request.task)
        return await agent.execute(request)
```

### Benefits of Multi-Agent Architecture

- **Specialized Capabilities**: Each agent can focus on specific domains
- **Scalability**: Independent scaling of different agent types
- **Fault Isolation**: Issues with one agent don't affect others
- **Resource Optimization**: Efficient resource allocation per agent type
- **Flexible Deployment**: Deploy agents independently or together

### Future Roadmap

- [ ] Multi-agent registry and discovery
- [ ] Load balancing and routing
- [ ] Agent health monitoring
- [ ] Cross-agent communication protocols
- [ ] Unified agent management interface

## 🤝 Contributing

We welcome contributions! Please see our comprehensive [CONTRIBUTING.md](CONTRIBUTING.md) guide for:

- Development workflow and commands
- Code style guidelines
- Testing strategies
- Pull request process
- Release procedures

Quick start:
1. Follow the enterprise-grade structure
2. Add comprehensive tests for new features
3. Update documentation
4. Ensure A2A protocol compliance
5. Use proper dependency injection patterns

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review A2A protocol documentation