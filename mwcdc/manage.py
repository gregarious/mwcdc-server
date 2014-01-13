#!/usr/bin/env python
import os
import sys
import json

if __name__ == "__main__":
	# default to production settings: only dotcloud uses manage.py
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mwcdc.settings.dotcloud')

	# set up the dotcloud environment	
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

	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
