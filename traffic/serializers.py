from rest_framework import serializers
from .models import TrafficData

class TrafficSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    class Meta:
        model = TrafficData
        fields = ['city_name', 'congestion_level', 'average_speed', 'updated_at']