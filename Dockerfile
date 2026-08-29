FROM python:3.12-slim

RUN pip install uv
ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN useradd --create-home appuser
WORKDIR /home/appuser/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY uv.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-install-project

RUN apt-get purge -y --auto-remove gcc libc6-dev

COPY . .

RUN chown -R appuser:appuser /home/appuser/app
USER appuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]