from celery import shared_task
from core.models import City
from .models import TrafficData
import random

@shared_task
def fetch_traffic(city_id):
    city = City.objects.get(id=city_id)
    # Mock data (Google/TomTom needs paid API for real-time traffic)
    levels = ['low', 'medium', 'high']
    TrafficData.objects.update_or_create(
        city=city,
        defaults={
            'congestion_level': random.choice(levels),
            'average_speed': random.randint(20, 60)
        }
    )