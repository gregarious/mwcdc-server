#!/usr/bin/env python
from wsgi import *
from django.contrib.auth.models import User
from sys import stderr as err
from django.contrib.auth import authenticate

DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'password'

u, created = User.objects.get_or_create(username=DEFAULT_USERNAME)
if created:
    u.set_password(DEFAULT_PASSWORD)
    u.is_superuser = True
    u.is_staff = True
    u.save()
	
    err.write('Administrator account created with default password. Change it now!\n')
    err.flush()
else:
	if authenticate(username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):
		err.write('Administrator account still has default password. Change it now!\n')
		err.flush()
