"""
Django settings for xoma163site project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

from secrets.secrets import secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets['django']['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MAIN_PROTOCOL = 'https'
MAIN_DOMAIN = "xoma163.xyz"
MAIN_SITE = f'{MAIN_PROTOCOL}://{MAIN_DOMAIN}'
ALLOWED_HOSTS = [
    # ips
    '192.168.1.10', '85.113.60.5',
    # old site
    'xoma163.site', 'api.xoma163.site', 'www.xoma163.site', 'birds.xoma163.site',
    # new site
    'xoma163.xyz', 'api.xoma163.xyz', 'www.xoma163.xyz', 'birds.xoma163.xyz',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_hosts',
    'static_autocollect',

    'apps.API_VK',
    'apps.birds',
    'apps.service',
    'apps.games',
    'apps.web'
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]
DEFAULT_HOST = 'www'
ROOT_HOSTCONF = 'xoma163site.hosts'
ROOT_URLCONF = 'xoma163site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')), ],
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
WSGI_APPLICATION = 'xoma163site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets['db']['NAME'],
        'USER': secrets['db']['USER'],
        'PASSWORD': secrets['db']['PASSWORD'],
        'HOST': secrets['db']['HOST'],
        'PORT': secrets['db']['PORT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_L10N = True

# Чтобы в базе время хранилось со смещением таймзоны
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Правильные права для загружаемых файлов
FILE_UPLOAD_PERMISSIONS = 0o644

APPEND_SLASH = True

from time import sleep


def sprint(text):
    print(text)
    sleep(0.0000000001)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)-12s --> %(funcName)-20s --> %(lineno)-4d  %(levelname)-8s %(message)s',
        },
        'simple': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'commands': {
            'format': '%(asctime)s %(message)s',
            # 'datefmt': '%d.%m.%Y %H:%M:%S'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'commands.log'),
            'formatter': 'commands',
        },
    },
    'loggers': {
        'commands': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True
