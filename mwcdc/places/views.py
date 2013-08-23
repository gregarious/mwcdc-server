from django.db.models import Q

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from places.models import Place
from places.serializers import PlaceSerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class SearchPlaces(APIView):
    def get(self, request, format=None):
        # super naive right now. Will add better search backend later
        query = request.GET.get('q', '')
        places = []
        if query:
            places = Place.objects.filter(
                Q(name__icontains=query) |
                Q(address__icontains=query) |
                Q(description__icontains=query)
            )

        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
