"""
Django settings for bizz_fuzz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# My settings
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_PATH,
)
MEDIA_ROOT = os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'media'])
MEDIA_URL = '/media/'
""" User model
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#auth-custom-user
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-django-s-default-user
"""
AUTH_USER_MODEL = 'bizz_fuzz_app.MyUser'

# Settings for Heroku
"""
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
STATIC_ROOT = 'staticfiles'  # Heroku's tip
#PROJECT_PATH = os.path.dirname(os.path.abspath(__file__)) # Heroku's tip, doesn't work properly
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bf63-8eefra+!82%g_q4msr=h&+kywdjhzuj8-$bgb66sg@fqs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bizz_fuzz_app',
    'export_xls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bizz_fuzz.urls'

WSGI_APPLICATION = 'bizz_fuzz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3nadab0o9fo93',
        'HOST': 'ec2-54-197-241-91.compute-1.amazonaws.com',
        'USER': 'xznmsfargscyiu',
        'PASSWORD': '7CXKNyV0vPIkMHPsvyJ3FNVAK0',
        'PORT': '5432',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
