import urllib
import json
import time
from decimal import Decimal
from places.models import Place
# TODO: create and handle exceptions

ZERO = Decimal(0.0)

def geocode_address(street_address, suffix=''):
	if suffix:
		address = "%s, %s" % (street_address, suffix)
	else:
		address = street_address

	options = {'address': address,
				'sensor': 'false'}
	request_url = "http://maps.googleapis.com/maps/api/geocode/json" + '?' + urllib.urlencode(options)

	resp = json.load(urllib.urlopen(request_url))
	results = resp.get('results')

	if not results:
		print 'invalid json: no results'
		return None

	if len(results) == 0:
		print 'no results'
	elif len(results) > 1:
		print 'ambiguous results'
	else:
		location = results[0].get('geometry', {}).get('location', {})
		if location:
			return (location.get('lat', 0.0), location.get('lng', 0.0))
		else:
			print 'invalid json: no location'

	return None

def is_geocoded(place): 
	return not(place.latitude == ZERO or \
		   	   place.longitude == ZERO or \
		   	   place.latitude is None or \
		       place.longitude is None)

def geocode_all():
	for place in Place.objects.all():
		if not is_geocoded(place) and place.street_address:
			coords = geocode_address(place.street_address, 'Pittsburgh, PA 15211')
			# delay to prevent throttling
			time.sleep(0.5)
			if coords:
				place.latitude = coords[0]
				place.longitude = coords[1]
				place.save()
			print '%s: %s' % (place.name, str(coords))

