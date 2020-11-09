import os
import environ


env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # < Per Whitenoise, to disable built in
    'django.contrib.staticfiles',
]
THIRD_APPS = [
    'rest_framework',
    'drf_yasg',
    # 'rest_framework.authtoken',
    # 'rest_auth'
]
LOCAL_APPS = [
    'api',
    'investors',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    #add whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CACHES = {
#     'default':{
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'dataflair_cache',
#     }
# }

# Key in `CACHES` dict
# CACHE_MIDDLEWARE_ALIAS = 'default'
#
# # Additional prefix for cache keys
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
#
# # Cache key TTL in seconds
# CACHE_MIDDLEWARE_SECONDS = 0

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = True


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add dist to
        'DIRS': [os.path.join(BASE_DIR, 'dist')],
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

WSGI_APPLICATION = 'config.wsgi.application'
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


DATABASES = {
    'default': env.db()
}

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


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = False
USE_TZ = False


# When Vue Builds, path will be `/static/css/...` so we will have Django Serve
# In Production, it's recommended use an alternative approach such as:
# http://whitenoise.evans.io/en/stable/django.html?highlight=django


STATIC_URL = '/static/'
# Place static in the same location as webpack build files
# STATIC_ROOT = os.path.join(BASE_DIR, 'dist', 'static')
# STATICFILES_DIRS = []
# DEFAULT_FILE_STORAGE = os.path.join(BASE_DIR, 'dist')

STATIC_ROOT = os.path.join(BASE_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)
##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Insert Whitenoise Middleware at top but below Security Middleware
# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware',)
# http://whitenoise.evans.io/en/stable/django.html#make-sure-staticfiles-is-configured-correctly


##########
# API #
##########

API_URL = env.str('API_URL')

# # Fake PyMySQL's version and install as MySQLdb add to __init__
# # https://adamj.eu/tech/2020/02/04/how-to-use-pymysql-with-django/
# import pymysql
# pymysql.version_info = (1, 4, 2, "final", 0)
# pymysql.install_as_MySQLdb()
