from rest_framework import viewsets
from .models import TrafficData
from .serializers import TrafficSerializer

class TrafficViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrafficData.objects.all()
    serializer_class = TrafficSerializer