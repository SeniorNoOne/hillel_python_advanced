# Local settings should be based on base settings
from .base import *

# Enabling debug mode since local settings are used for development purposes
DEBUG = True

# Enabling debug toolbar
if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

# For dev using lightweight DB such as SQLite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Postgres basic config with persistent connection, health check and isolation level
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'testtest',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': None,
        'CONN_HEALTH_CHECKS': True,
        'OPTIONS': {
            'isolation_level': IsolationLevel.REPEATABLE_READ,
        }
    }
}

# Postgres configuration with connection puller
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'testtest',
        'HOST': 'localhost',
        'PORT': '6432',
        'CONN_MAX_AGE': None,
        'CONN_HEALTH_CHECKS': True,
        'OPTIONS': {
            'isolation_level': IsolationLevel.SERIALIZABLE,
        }
    }
}

# Caching should be changed to LocMemCache for django-pytest
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Using console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
