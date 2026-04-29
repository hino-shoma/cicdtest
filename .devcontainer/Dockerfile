FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency metadata first for better build cache
COPY pyproject.toml ./

# Install only third-party dependencies (no local package install)
RUN uv sync --no-dev --no-install-project

# Copy source code
COPY . .

CMD ["uv", "run", "python", "main.py"]
