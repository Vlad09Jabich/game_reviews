from django.contrib import admin

from .models import Review, Game


admin.site.register([Review, Game])
