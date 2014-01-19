import urllib
import json
import time
from decimal import Decimal
from places.models import Place

import logging
logger = logging.getLogger(__name__)

ZERO = Decimal(0.0)

def geocode_address(address_string):
	'''
	Contacts the Google Geocoding API and returns a tuple of
	(latitude, longitude) if the address can be geocoded. Returns
	None otherwise.
	'''
	options = {'address': address_string,
				'sensor': 'false'}
	request_url = "http://maps.googleapis.com/maps/api/geocode/json" + '?' + urllib.urlencode(options)

	resp = json.load(urllib.urlopen(request_url))
	results = resp.get('results')

	if not results:
		logger.warning('Invalid API response for "%s": no results key' % address_string)
		return None

	if len(results) == 0:
		logger.info('No results found for "%s"' % address_string)
	elif len(results) > 1:
		logger.info('Ambiguous results for "%s"' % address_string)
	else:
		location = results[0].get('geometry', {}).get('location', {})
		if location:
			return (location.get('lat', 0.0), location.get('lng', 0.0))
		else:
			logger.info('Invalid API for "%s": no location key' % address_string)

	return None

def is_geocoded(place): 
	'''
	Returns True if latitude or longitude is None or 0.
	'''
	return not(place.latitude == ZERO or \
		   	   place.longitude == ZERO or \
		   	   place.latitude is None or \
		       place.longitude is None)

def geocode_all():
	'''
	Run through all places and attempt to geocode any instances with no lat/lng.
	'''
	for place in Place.objects.all():
		if not is_geocoded(place) and place.street_address:
			coords = geocode_address(place.street_address + ', Pittsburgh, PA 15211')
			# delay to prevent throttling
			time.sleep(0.5)
			if coords:
				place.latitude = coords[0]
				place.longitude = coords[1]
				place.save()
			logger.debug('%s: %s' % (place.name, str(coords)))
