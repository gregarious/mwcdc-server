from skyline.models import InterestPoint, Viewpoint, InterestPointMapping
from rest_framework import serializers

class InterestPointMappingSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='interest_point.id')

    name = serializers.Field(source='interest_point.name')
    address = serializers.Field(source='interest_point.address')
    description = serializers.Field(source='interest_point.description')
    image = serializers.ImageField(source='interest_point.image')

    class Meta:
        model = InterestPointMapping

class ViewpointSerializer(serializers.ModelSerializer):
    interest_points = InterestPointMappingSerializer(source="interestpointmapping_set", many=True)
    class Meta:
        model = Viewpoint
        depth = 1
