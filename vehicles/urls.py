from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, health

router = DefaultRouter()
router.register(r'vehicles',VehicleViewSet,basename='vehicle')

urlpatterns = [
    path('health/',health),
    path('',include(router.urls)),
]