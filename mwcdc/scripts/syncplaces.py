#!/usr/bin/env python
from wsgi import *
from places.sync import sync_all

sync_all()
