from celery import shared_task
from .models import Event
from core.models import City
import random
from django.utils import timezone

@shared_task
def fetch_events(city_id):
    city = City.objects.get(id=city_id)
    Event.objects.create(
        title=f"Event in {city.name} #{random.randint(1,1000)}",
        description="Sample event fetched automatically",
        city=city,
        event_date=timezone.now(),
        location="City Center"
    )