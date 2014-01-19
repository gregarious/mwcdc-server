from places.serializers import PlaceSyncingSerializer

import collections
import logging
import json
import urllib2
import re
import HTMLParser

from copy import copy

logger = logging.getLogger(__name__)

class SerializedObjectSyncer(object):
	def __init__(self, serializer_class):
		self.serializer_class = serializer_class
		self.model_class = self.serializer_class.Meta.model

	def create_object(self, data):
		'''
		Create a new model from the `data` dict.
		'''
		obj = self.serializer_class().restore_object(data)
		obj.save()

	def merge_fields(self, obj, data):
		'''
		Ensures each declared field of the object contains the cooresponding
		value from the data dict.
		'''
		was_changed = False

		serialized_model = self.serializer_class(obj).data
		for field, value in serialized_model.items():
			if field == 'zip_code':
				continue
			if field not in data:
				logger.warning(u'Data has no `%s` attribute!' % field)
			elif value != data.get(field):
				if not value.startswith('http'):
					logger.debug('Merging on id %s: field `%s` value %s to %s'  % (str(obj.id), field, str(value), str(data.get(field))))
				obj.__setattr__(field, data.get(field))
				was_changed = True

		if was_changed:
			obj.save()

	def transform_fields(self, data):
		'''
		Transforms keys and values to be compatable with local 
		model/serializers.
		'''
		data = copy(data)
		if 'content' in data:
			data['description'] = data.pop('content')

		if 'category' in data:
			category_dict = data.pop('category')
			data['category_id'] = int(category_dict['id'])
			data['category_label'] = category_dict['label']

		# strip out the id/username from a full FB url
		if 'fb_id' in data:
			match = re.match('(.+\/)?(\w+)(\?.*)?', data['fb_id'])
			if match:
				data['fb_id'] = match.group(2)

		if 'hours' in data:
			data['hours'] = unicode(data['hours'])

		if 'image_url' in data:
			# TODO: add image copying
			# if None or False, make it blank string
			if data['image_url']:
				data['external_image_url'] = data['image_url']
			else:
				data['external_image_url'] = ''
			
		return data

	def filter_fields(self, data, valid_fields):
		'''
		Return data with all key/values removed with keys not present
		in valid_fields.
		'''
		filtered_data = dict()
		for k, v in data.items():
			if k in valid_fields:
				filtered_data[k] = v
		return filtered_data

	def sync_objects_with_data(self, data):
		'''
		Compare the object in `data` with a stored object with the same
		id, merging all values. If no such object is found, a new one 
		is created.

		`data` can be either a single data dict, or a list of them.
		'''
		if not isinstance(data, collections.Sequence):
			data = [data]

		model_fields = self.model_class._meta.get_all_field_names()

		for data_dict in data:
			data_id = data_dict.get('id')
			if data_id is not None:
				data_dict = self.transform_fields(data_dict)
				data_dict = self.filter_fields(data_dict, model_fields)
				# either get and merge the object, or create a new one
				try:
					obj = self.model_class.objects.get(id=data_id)
				except self.model_class.DoesNotExist:
					self.create_object(data_dict)
				else:
					self.merge_fields(obj, data_dict)
			else:
				logger.error('`id` not found in incoming data.')


syncer = SerializedObjectSyncer(PlaceSyncingSerializer)

def pull_data():
	'''
	Pulls data from external API and returns list or dict of it.
	'''
	parser = HTMLParser.HTMLParser()
	try:
		f = urllib2.urlopen('http://mwcdc.org/app/places.php')
		raw = f.read()
	except urllib2.URLError as e:
		logging.error(u'Problem contacting server: %s' % unicode(e.reason))
		return []
	finally:
		f.close()
	
	# server response is currently HTML -- could have some undesired HTML encodings
	try:
		decoded_raw = parser.unescape(raw)
	except HTMLParser.HTMLParseError:
		decoded_raw = raw
	data_maps = json.loads(decoded_raw)
	
	# strip out md5 code
	data_maps.pop('md5')

	# data will come in as a map with id keys. we only want a list of the value dicts
	return list(data_maps.values())

def sync_all():
	data = pull_data()
	syncer.sync_objects_with_data(data)
