from places.models import Place
from places.serializers import PlaceSyncingSerializer

import logging
logger = logging.getLogger(__name__)

def merge_fields(data, model):
	'''
	Compare incoming `data` dict with existing `model`, overwriting fields in
	model if they don't match.
	'''
	was_changed = False

	# use serialized model for comparison: Serializer knows which
	# fields to compare
	serialized_model = PlaceSyncingSerializer(model).data
	for field, value in serialized_model.items():
		if not data.has_key(field):
			logger.warning('data has no `%s` attribute!' % unicode(field))
		elif value != data.get(field):
			model.__setattr__(field, data.get(field))
			was_changed = True

	if was_changed:
		model.save()

def create_place(data):
	'''
	Create a new model from the `data` dict.
	'''
	model = PlaceSyncingSerializer().restore_object(data)
	model.save()

def compare_object(data):
	data_id = data.get('id')
	if data_id is not None:
		try:
			place = Place.objects.get(id=data_id)
		except:
			create_place(data)
		else:
			merge_fields(data, place)
	else:
		logger.warning('`id` not found in incoming data.')

def compare_objects(data_list):
	'''
	Cycle through the list of data dicts in `data_list`, comparing data
	to models by `id`. If differences exist, overwrite the models. If no
	corresponding model exists, create a new one from the data.
	'''
	for data_dict in data_list:
		compare_object(data_dict)

def pull_data(place_id=None):
	'''
	Pulls data from external API and returns list or dict of it.

	If `place_id` is provided, individual Place resource will be accessed
	and individual dict will be returned. If omitted, entire collection will
	be requested and a list of dicts will be returned.
	'''
	if place_id is None:
		return []
	else:
		return {}

def sync_all():
	data = pull_data()
	compare_objects(data)

def sync_one(place_id):
	data = pull_data(place_id)
	compare_object(data)
