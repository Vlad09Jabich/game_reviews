from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path(
        "login/",
        views.CustomLoginView.as_view(),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),
    path(
        "password_change/",
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
