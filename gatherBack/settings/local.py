from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'bfln5b58115gaybdjfkh',  
    'HOST': 'bfln5b58115gaybdjfkh-mysql.services.clever-cloud.com',
    'PORT': '3306',
    'USER': 'uyu1zafyclfvdpxv',
    'PASSWORD': 'h31vJ0MClEXLmer2de4J',
}
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'