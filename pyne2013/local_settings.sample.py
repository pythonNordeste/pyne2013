from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = STATICFILES_STORAGE