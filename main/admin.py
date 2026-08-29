from django.contrib import admin

from .models import Author, Game, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("review_title", "game", "author")

    list_filter = ("game", "author")

    search_fields = ["review_title", "game__game_title"]
    search_help_text = "Search review title or game title"


admin.site.register([Game, Author])
