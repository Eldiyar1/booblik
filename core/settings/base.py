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

THEME_APPS = ["modeltranslation", "jazzmin"]

LIBRARY_APPS = [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "debug_toolbar",
    'drf_spectacular',
    'django_summernote',
]

LOCAL_APPS = [
    "apps.common.apps.CommonConfig",
    "apps.filial.apps.FilialConfig",
    "apps.event.apps.EventConfig",
    "apps.vacancy.apps.VacancyConfig",
    "apps.feedback.apps.FeedbackConfig",
    "apps.menu.apps.MenuConfig"
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
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'width': '100%',
        'height': '480',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    },
}

LANGUAGE_CODE = 'ru'

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = [
    ("ru", gettext("Русский")),
    ("ky", gettext("Кыргызча")),
    ("en", gettext("English")),
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
CELERY_BEAT_SCHEDULER = env('CELERY_BEAT_SCHEDULER')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_CONNECTION_RETRY = False
CELERY_BROKER_TRANSPORT_OPTION = {"visibility_timeout": 3600}
CELERY_TIMEZONE = "Asia/Bishkek"

X_FRAME_OPTIONS = "SAMEORIGIN"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379',
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
