from rest_framework import viewsets
from .models import WeatherData
from .serializers import WeatherSerializer

class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherData.objects.all().order_by('-updated_at')
    serializer_class = WeatherSerializer