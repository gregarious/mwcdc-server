from mwcdc.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

# disable the browsable API
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	)
}

STATIC_ROOT = os.path.join(
				os.path.dirname(	# mwcdc (Webfaction webapp root)
					os.path.dirname(	# mwcdc-server (repo)
						os.path.dirname(	# mwcdc (project)
							os.path.dirname(	# mwcdc (app)
								os.path.dirname(	# settings
									os.path.abspath(__file__)))))),
				'mwcdc-server_assets/static/')

MEDIA_ROOT = os.path.join(
				os.path.dirname(	# mwcdc (Webfaction webapp root)
					os.path.dirname(	# mwcdc-server (repo)
						os.path.dirname(	# mwcdc (project)
							os.path.dirname(	# mwcdc (app)
								os.path.dirname(	# settings
									os.path.abspath(__file__)))))),
				'mwcdc-server_assets/media/')

ALLOWED_HOSTS = ['mwcdc.scenable.com']
