from django.contrib import admin

from .models import Game, Review

# class ReviewInLine(admin.StackedInline):
#    model = Review.author.through
#    extra = 1

# Model author does not exist
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#    inlines = [ReviewInLine]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
    # filter_horizontal = ("author",)


admin.site.register(
    [
        Game,
    ]
)
