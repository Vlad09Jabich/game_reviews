from django.conf import settings
from django.db import models


class Game(models.Model):
    game_title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.game_title


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Review(models.Model):
    review_title = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def __str__(self):
        return self.review_title
