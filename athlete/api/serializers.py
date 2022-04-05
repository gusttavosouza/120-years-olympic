from rest_framework import serializers;
from athlete import models;

class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Athlete
    fields = '__all__'