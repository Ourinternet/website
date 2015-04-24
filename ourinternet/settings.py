"""
Django settings for ourinternet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'ourinternet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'storages',
    'robots',
    'structure',
    'commission',
    'tweet_cache',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ourinternet.middleware.XUACompatibleMiddleWare',
)

ROOT_URLCONF = 'ourinternet.urls'

WSGI_APPLICATION = 'ourinternet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SERVER_TIMEZONE = 'US/Eastern'

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_OATH_ACCESS_TOKEN = ''
TWITTER_OATH_ACCESS_TOKEN_SECRET = ''
TWITTER_USER = ''

GA_SITE_ID = 'UA-XXXXX-X'
GA_SITE_URL = 'yoursite.org'

RAVEN_CONFIG = {}

CONTACT_FORM_RECIPIENT_LIST = []

VIDEO_BASE_URL = ''

X_UA_COMPATIBLE = {
    'IE': 'edge',
    'chrome': '1',
}

EXTRA_INSTALLED_APPS = ()
try:
    from secure_settings import *
except ImportError:
    pass

try:
    from local_settings import *
except ImportError:
    pass

INSTALLED_APPS = INSTALLED_APPS + EXTRA_INSTALLED_APPS


