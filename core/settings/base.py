import os
from pathlib import Path
from .env_reader import env
from .jazzmin import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PRODUCTION = env("PRODUCTION", default=False, cast=bool)

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THEME_APPS = ["jazzmin"]

LIBRARY_APPS = [
    "modeltranslation",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "debug_toolbar",
    'drf_spectacular',
    'drf_yasg'
]

LOCAL_APPS = [
    "apps.common.apps.CommonConfig",
    "apps.geolocation.apps.GeolocationConfig",
    "apps.event.apps.EventConfig",
    "apps.vacancy.apps.VacancyConfig",
    "apps.feedback.apps.FeedbackConfig"
]

INSTALLED_APPS = [*THEME_APPS, *DJANGO_APPS, *LIBRARY_APPS, *LOCAL_APPS]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = [
    ("ru", gettext("Русский")),
    ("en", gettext("English")),
    ("ky", gettext("Кыргызча")),
]

LOCALE_PATHS = [
    f"{BASE_DIR}/common/locale",
    f"{BASE_DIR}/feedback/locale",
    f"{BASE_DIR}/geolocation/locale",
    f"{BASE_DIR}/event/locale",
    f"{BASE_DIR}/vacancy/locale",
    f"{BASE_DIR}/core/locale",
]

STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATE_INPUT_FORMATS = [
    "%d.%m.%Y",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M:%S",
    "DATE_FORMAT": "%d.%m.%Y",
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,  # TODO: надо определится с пагинацией
}

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_CONNECTION_RETRY = False
CELERY_BROKER_TRANSPORT_OPTION = {"visibility_timeout": 3600}
CELERY_TIMEZONE = "Asia/Bishkek"

X_FRAME_OPTIONS = "SAMEORIGIN"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379',
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "pretty": {
            "format": "\033[1;36m{levelname}\033[0m \033[1;34m{asctime}\033[0m \033[1m{module}\033[0m {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "pretty",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

if not PRODUCTION:
    from .local import *
else:
    from .production import *

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
