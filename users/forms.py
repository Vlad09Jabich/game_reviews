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

        fields = ("email", "username")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO: Refactor all this html code
        for field_name, field in self.fields.items():
            if field_name == "username":
                field.widget.attrs.update({"placeholder": "Your unique username"})
            elif field_name == "email":
                field.widget.attrs.update({"placeholder": "Your email"})
            elif field_name == "password1":
                field.widget.attrs.update({"placeholder": "Your password"})
            elif field_name == "password2":
                field.widget.attrs.update({"placeholder": "Confirm your password"})


class CustomUserLoginForm(AuthenticationForm):
    """Cleaned, lowercase email field used as the login identifier."""

    username = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "placeholder": "Your password"}
        ),
    )

    def clean_username(self):
        email = self.cleaned_data.get("username")
        if email:
            email = email.strip().lower()
        return email


class CustomUserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("role", "username", "email")


class CustomUserAdminChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "role",
            "username",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
        )
