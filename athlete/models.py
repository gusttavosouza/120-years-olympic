from django.db import models


class Athlete(models.Model):
    id_athlete = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    Sex = models.CharField(max_length=1, )
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Team = models.CharField(max_length=100)
    NOC = models.CharField(max_length=4)
    Games = models.CharField(max_length=255)
    Year = models.IntegerField()
    Season = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Sport = models.CharField(max_length=255)
    Event = models.CharField(max_length=255)
    Medal = models.CharField(max_length=255)
    Create_at = models.DateField(auto_now_add=True)
