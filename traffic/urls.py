from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrafficViewSet

router = DefaultRouter()
router.register(r'', TrafficViewSet)

urlpatterns = [
    path('', include(router.urls)),
]