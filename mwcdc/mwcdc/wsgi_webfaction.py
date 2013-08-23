'''
Copy of wsgi.py with webfaction env variables fixed. Can't get them to
stick with apache SetEnv.

*DON'T* use this for a real deploy.
'''

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mwcdc.settings.webfaction'
os.environ['SECRET_KEY'] = 'f9g*qtz(tnvd+@cer7f+ks*rr^l#+!7@sb0207b69a009o64'
os.environ['DATABASE_URL'] = 'postgres://gregarious_mwcdc:gregarious_mwcdc@localhost/gregarious_mwcdc'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

