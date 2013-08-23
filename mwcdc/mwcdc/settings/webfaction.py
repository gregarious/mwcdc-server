from development import *

STATIC_ROOT = '/home/gregarious/webapps/mwcdc_static/static/'
MEDIA_ROOT = '/home/gregarious/webapps/mwcdc_static/media/'

STATIC_URL = '/assets/static/'
MEDIA_URL = '/assets/media/'

LOGGING['loggers']['places']['level'] = 'INFO'
