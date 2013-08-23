from rest_framework import viewsets
from skyline.models import Viewpoint
from skyline.serializers import ViewpointSerializer

class ViewpointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Viewpoint.objects.all()
    serializer_class = ViewpointSerializer
