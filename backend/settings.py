"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    "social",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "djoser",
    "blog",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static-backend/"

MEDIA_URL = "/media/"

STATIC_ROOT = Path.joinpath(BASE_DIR, "static/")
MEDIA_ROOT = Path.joinpath(BASE_DIR, "media/")

# AWS
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", None)
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", None)

AWS_S3_SIGNATURE_VERSION = env.str("AWS_S3_SIGNATURE_VERSION", default="s3v4")
AWS_QUERYSTRING_AUTH = env.bool("AWS_QUERYSTRING_AUTH", default=True)
AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", None)  # "public-read" for public buckets

USE_AWS_FOR_MEDIA = env.bool("USE_AWS_FOR_MEDIA", False)
USE_AWS_FOR_STATIC = env.bool("USE_AWS_FOR_STATIC", False)

if USE_AWS_FOR_MEDIA:
    DEFAULT_FILE_STORAGE = "commons.storages.S3MediaStorage"

if USE_AWS_FOR_STATIC:
    STATICFILES_STORAGE = "commons.storages.S3StaticStorage"

AWS_S3_STATIC_BUCKET_NAME = env.str("AWS_S3_STATIC_BUCKET_NAME")
AWS_S3_MEDIA_BUCKET_NAME = env.str("AWS_S3_MEDIA_BUCKET_NAME")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "social.UserModel"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

DJOSER = {
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {
        "current_user": "social.serializers.CustomUserSerializer",
        "user": "social.serializers.CustomUserListSerializer",
        "user_create": "social.serializers.CustomUserCreateSerializer",
    },
    "HIDE_USERS": False,
}
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

# To allow requests from different ip
CORS_ORIGIN_ALLOW_ALL = True
