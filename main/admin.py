from django.contrib import admin

from .models import Fan, Game, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "author", "created_at")

    list_filter = ("created_at",)

    search_fields = ["title", "game__title"]
    search_help_text = "Search review title or game title"


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ("user", "game", "fan_since")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")
