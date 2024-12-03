from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "dev_db"),
        'USER': os.getenv("POSTGRES_USER", "dev_user"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "dev_password"),
        'HOST': os.getenv("POSTGRES_HOST", "db"),
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
    }
}
