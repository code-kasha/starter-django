from .configuration import *

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = True

SECRET_KEY = "django-insecure-110laacax3v+q=6hd)3s3d$-je1qe6nbxu=83wtv93-(s2pu$="

STATIC_URL = "static/"
