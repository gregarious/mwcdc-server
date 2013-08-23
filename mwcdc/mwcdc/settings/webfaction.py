import os

# can't get apache SetEnv to stick. Manually set env here.
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'mwcdc.settings.development'
os.environ['SECRET_KEY'] = 'f9g*qtz(tnvd+@cer7f+ks*rr^l#+!7@sb0207b69a009o64'
os.environ['DATABASE_URL'] = 'postgres://gregarious_mwcdc:gregarious_mwcdc@localhost/gregarious_mwcdc'
