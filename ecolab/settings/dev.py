from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True	

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x3#n9*02e@!k+ae@yjmavv#ir46h(one$c$(0$-)gavop@31_z'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
