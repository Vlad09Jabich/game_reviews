from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "reviews"
urlpatterns = [
    path("reviews/", RedirectView.as_view(url="all/", permanent=True)),
    path("reviews/all/", views.all_reviews_view, name="all_reviews"),
    path("reviews/<int:review_id>/", views.review_detail_view, name="review_detail"),
    path("reviews/create", views.create_review_view, name="create_review"),
    path("", views.main_page_view, name="main_page"),
]
