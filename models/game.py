from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=75)
    designer = models.CharField(max_length=75)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    time_of_play = models.IntegerField()
    recommended_age = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)