"""
Django settings for globe_gazette project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
import dj_database_url
import cloudinary
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

# Set an e-mail to be sent error logs for deployed version
ADMINS = [('Mariam', 'mar.ayoub98@gmail.com')]

""" Email settings for sending error logs """
# Code adapted from Django docs and from:
#https://stackoverflow.com/questions/73008500/how-can-i-send-emails-with-django-to-my-gmail-account

# Allows smtp to send emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Set gmail as the email host
EMAIL_HOST = 'smtp.mail.yahoo.com'
# Allow secure connection with smtp
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
# Set the email port to match the above var
EMAIL_PORT = 465
# Username for SMTP server
EMAIL_HOST_USER = 'mariam.ayoub13@yahoo.co.uk'
# Password for email host
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# Override default email sender
SERVER_EMAIL = 'mariam.ayoub13@yahoo.co.uk'
DEFAULT_FROM_EMAIL = 'mariam.ayoub13@yahoo.co.uk'


ALLOWED_HOSTS = [
    '8000-mariam138-globetrotters-1mhio5zxo6c.ws.codeinstitute-ide.net',
    '.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

if os.path.isfile('env.py'):
    import env

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# use sqlite3 database for testing
if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

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

# Cloudinary config
cloudinary.config(
    cloud_name = os.environ.get("CLOUD_NAME"),
    api_key = os.environ.get("CLOUDINARY_API_KEY"),
    api_secret = os.environ.get("CLOUDINARY_API_SECRET")
)

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
        ]
    }
}
