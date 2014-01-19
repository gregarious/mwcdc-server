import urllib2
import json
import logging
import time 

from places.models import Place

logger = logging.getLogger(__name__)

def transform_fb_id(place):
	'''
	Contacts the Facebook Graph API to get the numerical ID from a 
	FB username.
	
	If id is already numerical, it is returned as is.
	'''
	if place.fb_id.isdigit() or len(place.fb_id) == 0:
		return

	# delay to prevent throttling
	time.sleep(1)
	
	url = 'http://graph.facebook.com/%s' % place.fb_id
	try:
		f = urllib2.urlopen(url)
		data = json.load(f)
		f.close()
	except urllib2.URLError as e:
		logging.warning(u'Problem contacting Facebook API for `%s`: %s (%d)' % (place.name, unicode(e.reason), e.code))
		return
	except ValueError:
		logging.warning(u'Invalid response from Facebook API')
		f.close()
		return

	try:
		if data['id']:
			logger.debug('Transformed id from %s to %s'  % (place.fb_id, data['id']))
			place.fb_id = data['id']
			place.fb_id_transformed = True
			place.save()
	except KeyError:
		logging.error(u'Invalid response from Facebook API')


def transform_all_fb_ids():
	for place in Place.objects.exclude(fb_id_transformed=True):
		if place.fb_id and not place.fb_id.isdigit():
			transform_fb_id(place)
