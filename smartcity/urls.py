from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/weather/', include('weather.urls')),
    path('api/traffic/', include('traffic.urls')),
    path('api/events/', include('events.urls')),
    path('api/dashboard/<int:city_id>/', dashboard_data, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)