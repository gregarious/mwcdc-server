from places.serializers import PlaceSyncingSerializer

import collections
import logging
import json
import urllib2
import re

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
			if field not in data:
				logger.warning(u'data has no `%s` attribute!' % field)
			elif value != data.get(field):
				obj.__setattr__(field, data.get(field))
				was_changed = True

		if was_changed:
			print 'merge ', obj.id
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

		return data

	def filter_fields(self, data, valid_fields):
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
			print data_dict
			data_id = data_dict.get('id')
			if data_id is not None:
				data_dict = self.transform_fields(data_dict)
				data_dict = self.filter_fields(data_dict, model_fields)
				try:
					obj = self.model_class.objects.get(id=data_id)
				except:
					print 'new ', data_id
					self.create_object(data_dict)
				else:
					self.merge_fields(obj, data_dict)
			else:
				logger.warning('`id` not found in incoming data.')


syncer = SerializedObjectSyncer(PlaceSyncingSerializer)

def pull_data(place_id=None):
	'''
	Pulls data from external API and returns list or dict of it.

	If `place_id` is provided, individual Place resource will be accessed
	and individual dict will be returned. If omitted, entire collection will
	be requested and a list of dicts will be returned.
	'''
	if place_id is not None:
		raise Exception('place_id support is not yet in place')

	try:
		f = urllib2.urlopen('http://testing6.o2dca.com/app/places.php')
		data_maps = json.load(f)
	except URLError as e:
		logging.error(u'problem contacting server: %s' % unicode(e.reason))

	# strip out md5 code
	data_maps.pop('md5')

	# data will come in as a map with id keys. we only want a list of the value dicts
	return list(data_maps.values())

def sync_all():
	data = pull_data()
	syncer.sync_objects_with_data(data)

def sync_one(place_id):
	data = pull_data(place_id)
	syncer.sync_objects_with_data(data)
