from celery import shared_task
from weather.tasks import fetch_weather
from traffic.tasks import fetch_traffic
from events.tasks import fetch_events
from core.models import City

@shared_task
def update_all_cities():
    for city in City.objects.all():
        fetch_weather.delay(city.id)
        fetch_traffic.delay(city.id)
        fetch_events.delay(city.id)