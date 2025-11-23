from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'humidity', 'updated_at')
    list_filter = ('city', 'updated_at')