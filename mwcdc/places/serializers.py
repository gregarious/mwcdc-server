from places.models import Place
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

class PlaceSyncingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		exclude = ('image', 'latitude', 'longitude',)
