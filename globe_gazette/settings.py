"""
Django settings for globe_gazette project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import cloudinary.api
import cloudinary.uploader
import os
import sys
import dj_database_url
import cloudinary
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.contrib.messages import constants as messages
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# configures use of whitenoise for hosting static files on heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# Initialisation of Sentry SDK
# Adapted from the Sentry docs:
# https://docs.sentry.io/platforms/python/integrations/django/
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    profiles_sample_rate=1.0,
)

ALLOWED_HOSTS = [
    '8000-mariam138-globetrotters-1mhio5zxo6c.ws.codeinstitute-ide.net',
    '.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    # Overrides Django's static file handling in development
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'blog',
    'cloudinary',
    'allauth',
    'allauth.account',
    'profile_page',
    'django_summernote',
    'crispy_forms',
    'crispy_bootstrap5',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'globe_gazette.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'globe_gazette.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.path.isfile('env.py'):
    import env

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# use sqlite3 database for testing
# if 'test' in sys.argv:
#     DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# use sqlite3 database for testing
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

# List of trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://*.herokuapp.com",
    "https://*.ws.codeinstitute-ide.net",
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# allow styling of django messages using bootstrap classes
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
    messages.ERROR: 'alert-danger',
    messages.WARNING: 'alert-warning',
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

""" Cloudinary Settings"""
# Cloudinary storage
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


""" Django AllAuth custom settings"""
# email not actually required for sign up but is required in form validation
# prevents an email being sent out to verify
# code adapted from:
# https://dev.to/gajesh/the-complete-django-allauth-guide-la3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
# redirects user to home page once registered
ACCOUNT_SIGNUP_REDIRECT_URL = "/"

""" Django Custom Settings"""
# redirect user to index once logged in
LOGIN_REDIRECT_URL = "/"

""" Crispy Forms """
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

""" Summernote Settings"""
# Allow summernote to use Bootstrap5 theme
SUMMERNOTE_THEME = 'bs5'
# Customisation of Summernote widget
SUMMERNOTE_CONFIG = {
    # Allow iframe to show in admin and on website
    'iframe': False,
    # Set width at 100% to stop page overflow
    'summernote': {
        'width': '100%',
        # Customise toolbar to only allow text editing
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']]
        ],
        'disable_attachment': False,
    }
}
