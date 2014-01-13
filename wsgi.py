'''
wsgi.py settings for Dotcloud
'''

import os
import json
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mwcdc.settings.dotcloud'

# set the $DATABASE_URL from the dotcloud environment file
with open('/home/dotcloud/environment.json') as f:
	env = json.load(f)

os.environ['DATABASE_URL'] = 'postgres://%(user)s:%(password)s@%(host)s:%(port)s/%(name)s' % {
	'name': 'mwcdcserverapp_production',
	'user': env['DOTCLOUD_DB_SQL_LOGIN'],
	'password': env['DOTCLOUD_DB_SQL_PASSWORD'],
	'host': env['DOTCLOUD_DB_SQL_HOST'],
	'port': env['DOTCLOUD_DB_SQL_PORT'],
}


# add primary PYTHONPATH dir to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'mwcdc')))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
