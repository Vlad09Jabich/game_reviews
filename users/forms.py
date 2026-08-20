from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-register form-control",
                "placeholder": "Your nickname",
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input-register form-control",
                "placeholder": "Your email",
            }
        ),
    )

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
