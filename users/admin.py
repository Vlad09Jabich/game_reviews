from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserAdminChangeForm, CustomUserAdminCreationForm
from .models import CustomUser, Permission, Role


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    list_display = [
        "username",
        "email",
        "role",
        "nickname",
        "is_active",
        "is_superuser",
        "last_login",
    ]

    list_filter = ["is_active"]

    fieldsets = [
        (
            "Authentication and authorization",
            {"fields": ["email", "password", "role"]},
        ),
        (
            "Personal information",
            {"fields": ["username", "nickname"]},
        ),
        (
            "Raw permissions",
            {"fields": ["is_active", "is_staff", "is_superuser"]},
        ),
    ]

    add_fieldsets = [
        (
            "Requered information",
            {
                "fields": [
                    "username",
                    "nickname",
                    "role",
                    "email",
                    "password1",
                    "password2",
                ],
            },
        ),
        (
            "Permission information",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ]
            },
        ),
    ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    filter_horizontal = ["permission"]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ["codename", "id"]
