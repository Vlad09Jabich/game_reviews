FROM python:3.12-slim AS base

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev\
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv==0.11.13

ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app

COPY uv.lock pyproject.toml ./


FROM base AS dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid 1000 -m -s /bin/bash appuser \
    && echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && chown -R appuser:appuser /usr/local

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project


FROM base AS prod
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --frozen --no-install-project

RUN apt-get purge -y --auto-remove gcc

COPY . .