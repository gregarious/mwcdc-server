from base import *

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = '/home/dotcloud/volatile/static/'
MEDIA_ROOT = '/home/dotcloud/data/media/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# disable the browsable API
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	)
}

ALLOWED_HOSTS = ['mwcdcappserver-mountwashington.dotcloud.com']
