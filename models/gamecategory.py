from django.db import models

class GameCategory(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_categories")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="game_categories")