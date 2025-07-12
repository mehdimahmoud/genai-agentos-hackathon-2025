# Stage 1: Build dependencies with uv
FROM python:3.12-slim AS builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY pyproject.toml* uv.lock* ./
COPY README-A2A.md ./
RUN uv sync --frozen

# Stage 2: Runtime image
FROM python:3.12-slim AS runtime

WORKDIR /app

# Create non-root user for security
RUN groupadd --system --gid 1001 app_group && \
    useradd --system --uid 1001 --gid 1001 app_user && \
    chown -R app_user:app_group /app

USER app_user

# Copy the entire app directory from builder stage (including the virtual environment)
COPY --from=builder --chown=app_user:app_group /app /app
ENV PATH="/app/.venv/bin:$PATH"

# Copy application files (excluding .venv to preserve the one from builder stage)
COPY --chown=app_user:app_group . /app

# Expose port using environment variable (defaults to 10002)
EXPOSE ${A2A_SERVER_PORT:-10002}

# Create a startup script to handle environment variables
RUN echo '#!/bin/bash\nuvicorn main:app --log-level info --host ${A2A_SERVER_HOST:-0.0.0.0} --port ${A2A_SERVER_PORT:-10002}' > /app/start.sh && \
    chmod +x /app/start.sh

# Start the application
CMD ["/app/start.sh"] 