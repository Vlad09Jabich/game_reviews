from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ("username", "nickname", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "input-register form-control"})

            if field_name == "username":
                field.widget.attrs.update({"placeholder": "Your unique username"})
            elif field_name == "nickname":
                field.widget.attrs.update({"placeholder": "Your nickname"})
            elif field_name == "email":
                field.widget.attrs.update({"placeholder": "Your email"})
            elif field_name == "password1":
                field.widget.attrs.update({"placeholder": "Your password"})
            elif field_name == "password2":
                field.widget.attrs.update({"placeholder": "Confirm your password"})


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-login form-control",
                "placeholder": "Your username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-login form-control",
                "autocomplete": "current-password",
                "placeholder": "Your password",
            }
        ),
    )


class CustomUserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "nickname", "email")


class CustomUserAdminChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "email",
            "fan",
            "is_active",
            "is_staff",
            "is_superuser",
        )
