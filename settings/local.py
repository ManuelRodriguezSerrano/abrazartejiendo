from .base import *
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bloginfo',
        'USER': 'root',
        'PASSWORD': 'Franco123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}