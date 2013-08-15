# Django settings for q4wine project.

import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('brezerk', 'brezerk@gmail.com'),
)

MANAGERS = ADMINS

# DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_NAME = 'q4wine'             # Or path to database file if using sqlite3.
# DATABASE_USER = 'q4wine'             # Not used with sqlite3.
# DATABASE_PASSWORD = 'LJgfuF&_33fGG'         # Not used with sqlite3.
# DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DATABASES = {
    'default': {
        'NAME': 'q4wine',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'q4wine',
        'PASSWORD': 'f0rm07h3rru$$14'
    },
    'apidb': {
        'NAME': 'appdb',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'appdb',
        'PASSWORD': 'f0rm07h3rru$$14'
    }
#    'apidb': {
#        'NAME': 'q4wine',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'q4wine',
#        'PASSWORD': 'q4wineololo'
#    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_ROOT + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
STATIC_ROOT = '/adminmedia/'
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lx9i@a_e9#7g&fpce)dvh@-cm)t9&kby^9285=z5r!@$ihpue9'

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
#)

TEMPLATE_LOADERS = (
	('django.template.loaders.cached.Loader', (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	)),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'q4wine.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.markup',
    'news',
    'docs',
    'xmlexport',
    'rss'
)
