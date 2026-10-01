FROM python:3.12-slim

RUN pip install --no-cache-dir uv==0.5.21
ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY uv.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-install-project --frozen

RUN apt-get purge -y --auto-remove gcc libc6-dev

COPY . .

RUN chown -R appuser:appuser /home/appuser/app
USER 1000

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]