from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from athlete.api import viewsets as athleteviewsets

route = routers.DefaultRouter()

route.register(r'athlete', athleteviewsets.AthleteViewSet, basename="Books")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
