from .base import *

DEPLOYMENT = 'DEV'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rango_db',
        'USER': 'yogesh',
        'PASSWORD': os.environ['PG_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
