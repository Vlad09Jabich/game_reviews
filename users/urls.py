from django.urls import path

from . import views  # noqa: F401

app_name = "users"

urlpatterns = [path("register/", views.register_view, name="register")]
