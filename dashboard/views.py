from rest_framework.decorators import api_view
from rest_framework.response import Response
from weather.models import WeatherData
from traffic.models import TrafficData
from events.models import Event
from weather.serializers import WeatherSerializer
from traffic.serializers import TrafficSerializer
from events.serializers import EventSerializer

@api_view(['GET'])
def dashboard_data(request, city_id):
    weather = WeatherData.objects.filter(city_id=city_id).first()
    traffic = TrafficData.objects.filter(city_id=city_id).first()
    events = Event.objects.filter(city_id=city_id).order_by('-event_date')[:10]

    return Response({
        'weather': WeatherSerializer(weather).data if weather else None,
        'traffic': TrafficSerializer(traffic).data if traffic else None,
        'events': EventSerializer(events, many=True).data
    })