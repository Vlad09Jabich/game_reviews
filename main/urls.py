from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.hub, name="hub"),
    path("reviews/", views.index, name="index"),
    path("reviews/<int:review_id>/", views.detail, name="detail"),
    path("become_author/", views.become_author_view, name="become_author"),
]
