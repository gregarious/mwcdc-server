from mwcdc.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

# disable the browsable API
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	)
}
