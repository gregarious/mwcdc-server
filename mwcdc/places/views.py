from rest_framework import viewsets
from places.models import Place
from places.serializers import PlaceSerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
