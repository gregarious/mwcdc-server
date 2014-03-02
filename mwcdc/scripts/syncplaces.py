#!/usr/bin/env python
from wsgi import *
from mwcdc.places.sync import sync_all

sync_all()
