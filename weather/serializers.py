from rest_framework import serializers
from .models import WeatherData

class WeatherSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    class Meta:
        model = WeatherData
        fields = ['city_name', 'temperature', 'humidity', 'description', 'icon', 'updated_at']