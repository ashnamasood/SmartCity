from django.db import models
from core.models import City

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city.name} - {self.temperature}°C"