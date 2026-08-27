from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.hub_view, name="hub"),
    path("reviews/", views.index_view, name="index"),
    path("reviews/<int:review_id>/", views.detail_view, name="detail"),
    path("become_author/", views.become_author_view, name="become_author"),
    path("write_review/", views.write_review_view, name="write_review"),
]
