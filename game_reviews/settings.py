import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment parser
# If running locally without Docker, read .env file
# Docker Compose environment variables take priority inside containers
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": "5432",
    }
}

INSTALLED_APPS = [
    # Local apps (placed first to override core templates)
    "main",
    "users",
    # Core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "game_reviews.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "game_reviews.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Required for Django admin to work correctly
# TODO: Switch static files logic to Nginx container
STATIC_URL = "static/"

AUTH_USER_MODEL = "users.CustomUser"
LOGIN_REDIRECT_URL = "main:hub"
LOGOUT_REDIRECT_URL = "main:hub"

# Required for password reset emails to determine site domain name
SITE_ID = 1
# Sender email address in outgoing emails
DEFAULT_FROM_EMAIL = "noreply@example.com"
# Print emails to terminal during local runs
# TODO: Move connection parameters to .env when switching to Celery
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
