from django.contrib import admin

from .models import Game, Review

admin.site.register([Review, Game])
