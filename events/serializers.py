# events/serializers.py
from rest_framework import serializers
from .models import Event
class EventSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    class Meta:
        model = Event
        fields = '__all__'