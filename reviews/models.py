from django.conf import settings
from django.db import models


class Game(models.Model):
    title = models.CharField(unique=True, max_length=100)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    title = models.CharField(max_length=100)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="review_set",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Fan(models.Model):
    """A user can be a fan only of one game."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="fans",
    )
    fan_since = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "game"],
                name="unique_user_game_fan",
            )
        ]

    def __str__(self):
        return f"{self.user.username} fans {self.game.title}"
