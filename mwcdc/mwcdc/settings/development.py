from mwcdc.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOGGING['loggers'].update({
    'places': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
})
