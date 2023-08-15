"""
Django settings for bitpoll project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, '_media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
# STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']

TEMPLATE_ALLOWABLE_SETTINGS_VALUES = [
    'ALLOW_CUSTOM_SLUGS',
    'SITE_NAME',
    'DEBUG',
    'DEFAULT_RANDOM_SLUG',
    'BASE_URL',
    'HOME_URL',
    'HOME_URL_NAME',
    'IMPRINT_TEXT',
    'IMPRINT_URL',
    'TIME_ZONE',
    'REGISTER_ENABLED',
    'MAIL_SIGNATURE',
    'GROUP_MANAGEMENT',
    'PUBLIC_POLLS',
    'CALENDAR_ENABLED',
]

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = '/login/'

SITE_NAME = 'Bitpoll'
BASE_URL = 'https://bitpoll.mafiasi.de'

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_simple_csp',
    'markdownify',
    'widget_tweaks',
    'pipeline',
    'bitpoll.poll.apps.BitpollConfig',
    'bitpoll.base',
    'bitpoll.invitations',
    'bitpoll.registration',
    'bitpoll.groups',
    'bitpoll.caldav',
    'django.contrib.admin',
    'friendlytagloader',
    'encrypted_model_fields',
    'django_token_bucket',
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django-simple-csp.middleware.csp.CSPMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
]



STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
]



STATICFILES_STORAGE = 'pipeline.storage.PipelineManifestStorage'

PIPELINE = {
    'STYLESHEETS': {
        'base': {
            'source_filenames': (
                'fontawesome/css/fontawesome.css',
                'fontawesome/css/solid.css',
                'fontawesome/css/v4-shims.css',
                'scss/main.scss',
                'scss/poll.scss'
            ),
            'output_filename': 'css/base.css',
        },
        'base_print': {
            'source_filenames': (
                'css/print.css',
            ),
            'output_filename': 'css/base_print.css',
            'extra_context': {
                'media': 'print',
            },
        },
        'base_screen': {
            'source_filenames': (
                'css/bootstrap.css',
                'css/bootstrap-theme.css',
                # 'css/jquery-range.css',  # this belongs to commented out JS class
                'scss/form.scss',
                'scss/action.scss',
                'scss/slider.scss',
                'scss/timeinput.scss',
                'css/jquery.datetimepicker.css',
            ),
            'output_filename': 'css/base_screen.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'poll_edit': {
            'source_filenames': (
                'scss/calendar.scss',
                'scss/iconpreview.scss',
            ),
            'output_filename': 'css/poll_edit.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'base': {
            'source_filenames': (
                'js/lib/jquery-3.2.1.js',
                'js/lib/bootstrap.js',
            ),
            'output_filename': 'js/base.js',
        },
        'create_poll': {
            'source_filenames': (
                'js/create.js',
                'js/slug.js',
            ),
            'output_filename': 'js/index.js',
        },
        'poll_edit': {
            'source_filenames': (
                'js/poll_edit_universal_choices.js',
                'js/poll_edit_choices.js',
            ),
            'output_filename': 'js/poll_edit.js',
        },
        'base_late': {
            'source_filenames': (
                #'js/lib/jquery-range.min.js',  # TODO: is this needet for the numeric polls?
                'js/lib/moment-with-locales.min.js',
                'js/lib/mousetrap.min.js',
                'js/main.js',
                'js/util.js',
                'js/custom-select.jquery.js',
                'js/common.js',
                'js/slider.js',
                'js/vote.js',
                'js/lib/jquery.datetimepicker.full.min.js',

            ),
            'output_filename': 'js/base_late.js',
        },
    },
    'COMPILERS': (
        'libsasscompiler.LibSassCompiler',
    ),
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',  # TODO
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',  # TODO
}

PIPELINE_ENABLED = False  # todo uglfyer mal ansehen

ROOT_URLCONF = 'bitpoll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bitpoll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'verceldb', 
        'USER': 'default',
        'PASSWORD': '1tPYwrClA8Sg',
        'HOST': 'ep-jolly-heart-14214350-pooler.us-east-1.postgres.vercel-storage.com', 
        'PORT': '5432',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60 * 30,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# User Model

AUTH_USER_MODEL = 'base.BitpollUser'

CSRF_COOKIE_HTTPONLY = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_PRECOMPILER_ROOT = STATIC_ROOT
SASS_PRECISION = 8

ALLOW_CUSTOM_SLUGS = True
DEFAULT_RANDOM_SLUG = 'true'  # this value is an JS true/false

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Url to the Base Homepage and Text on the Link, leave empty to not use this option
HOME_URL = "https://example.com"
HOME_URL_NAME = "Dashboard"

# Test mail functionality by printing mails to console:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# if the imprint URL is not empty use it as an link to the imprint, else use IMPRINT_TEXT
IMPRINT_URL = ""
IMPRINT_TEXT = """
<h1>Impressum</h1>
<p>Text goes here</p>
"""

LOCALE_PATHS = (os.path.join(ROOT_DIR, 'locale'), )

LANGUAGES = (
    ('de', 'Deutsch'),
    ('en', 'English'),
    #('fr', 'Français'),
)

REGISTER_ENABLED = True
GROUP_MANAGEMENT = REGISTER_ENABLED

CSP_REPORT_ONLY = True
CSP_REPORT_URL = ""

MAIL_SIGNATURE = "Bitpoll Team"

TEAM_EMAIL = "mail@example.com"

PUBLIC_POLLS = True

CALENDAR_ENABLED = True
CALENDAR_MAX_TOKENS = 2
CALENDAR_FILL_RATE = 500

#See https://django-markdownify.readthedocs.io/en/latest/settings.html
MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'em',
            'i',
            'li',
            'ol',
            'p',
            'strong',
            'ul',
            'h1',
            'h2',
            'h3',
        ],
        "WHITELIST_ATTRS": [
            'href',
        #    'src',
        #    'alt',
        ],
        "WHITELIST_PROTOCOLS": [
            'https',
        ],
        "WHITELIST_STYLES": [
        #    'color',
        #    'font-weight',
        ],
        "LINKIFY_TEXT": {
            "PARSE_URLS": True,

            # Next key/value-pairs only have effect if "PARSE_URLS" is True
            "PARSE_EMAIL": False,
            "CALLBACKS": [],
            "SKIP_TAGS": [],
        }
    }
}

# The root dir bitpoll appears to be in from the web, as configured in the webserver
URL_PREFIX = ''

ANTI_SPAM_CHALLENGE_TTL = 60 * 60 * 24 * 7  # Defaults to 7 days

from .settings_local import *
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
INSTALLED_APPS += INSTALLED_APPS_LOCAL
PIPELINE.update(PIPELINE_LOCAL)


