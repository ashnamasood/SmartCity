from django.contrib import admin
from .models import TrafficData

@admin.register(TrafficData)
class TrafficDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'congestion_level', 'average_speed', 'updated_at')