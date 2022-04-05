from rest_framework import viewsets
from athlete.api import serializers
from athlete import models


class AthleteViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.AthleteSerializer
    queryset = models.Athlete.objects.all()
