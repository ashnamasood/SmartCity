from celery import shared_task
import requests
from decouple import config
from core.models import City
from .models import WeatherData

@shared_task
def fetch_weather(city_id):
    city = City.objects.get(id=city_id)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': city.lat,
        'lon': city.lon,
        'appid': config('OPENWEATHER_API_KEY'),
        'units': 'metric'
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        if r.status_code == 200:
            WeatherData.objects.update_or_create(
                city=city,
                defaults={
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            )
    except:
        pass  # Silent fail for demo