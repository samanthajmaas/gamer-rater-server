from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    img = models.CharField(max_length=256)