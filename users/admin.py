from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserAdminChangeForm, CustomUserAdminCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    filter_horizontal = ["fan", "user_permissions", "groups"]

    list_display = [
        "username",
        "email",
        "nickname",
        "is_staff",
        "is_superuser",
        "is_active",
    ]

    list_filter = ["is_staff", "is_superuser"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "password",
                ]
            },
        ),
        (
            "Personal information",
            {
                "fields": [
                    "email",
                    "nickname",
                    "fan",
                ]
            },
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
    ]

    add_fieldsets = [
        (
            "Requered information",
            {
                "fields": ["username", "nickname", "email", "password1", "password2"],
            },
        ),
        (
            "Optional information",
            {
                "fields": ["fan"],
            },
        ),
        (
            "Permission information",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
    ]
