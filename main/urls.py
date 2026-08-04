from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    # ex: /
    path("", views.hub, name="hub"),
    # ex: /rewiws/
    path("reviews/", views.index, name="index"),
    # ex reviews/2/
    path("reviews/<int:review_id>/", views.detail, name="detail"),
]
