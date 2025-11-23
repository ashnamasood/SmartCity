from django.db import models
from core.models import City

class TrafficData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    congestion_level = models.CharField(max_length=20, choices=[
        ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('unknown', 'Unknown')
    ], default='unknown')
    average_speed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} - {self.congestion_level}"