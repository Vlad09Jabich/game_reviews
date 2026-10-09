"""TODO: Refactor to normal display in admin panel.
Refactor entire file to switch all logic from username to email login"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserAdminChangeForm, CustomUserAdminCreationForm
from .models import CustomUser, Permission, Role


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    # filter_horizontal = ["user_permissions", "groups"]

    list_display = [
        "username",
        "email",
        "role",
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
                    "role",
                    "username",
                    "password",
                ]
            },
        ),
        (
            "Personal information",
            {"fields": ["email", "nickname"]},
        ),
        (
            "Permissions",
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


admin.site.register([Permission])


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    filter_horizontal = ["permission"]
