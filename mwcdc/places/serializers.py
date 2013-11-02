from places.models import Place
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='external_image_url')
    class Meta:
        model = Place
        exclude = ('image', 'external_image_url',)

class PlaceSyncingSerializer(serializers.ModelSerializer):
	image = serializers.CharField(source='external_image_url')
	class Meta:
		model = Place
		exclude = ('image', 'latitude', 'longitude',)
