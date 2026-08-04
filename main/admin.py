from django.contrib import admin

from .models import Author, Game, Review


class ReviewInLine(admin.StackedInline):
    model = Review.author.through
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    filter_horizontal = ("author",)


admin.site.register(
    [
        Game,
    ]
)
