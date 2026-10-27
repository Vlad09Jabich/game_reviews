FROM python:3.12-slim

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv==0.11.13

ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app

COPY uv.lock pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --frozen --no-install-project

RUN apt-get purge -y --auto-remove gcc

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]