from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("<int:review_id>/", views.detail_view, name="detail"),
]
