from django.db import models


class Game(models.Model):
    game_title = models.CharField(max_length=50)

    def __str__(self):
        return self.game_title


class Review(models.Model):
    review_title = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_content = models.TextField()

    def __str__(self):
        return self.review_title