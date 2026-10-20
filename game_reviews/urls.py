from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls")),
    path("reviews/", include("reviews.urls")),
    path("", include("main.urls")),
]
