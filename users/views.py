from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserLoginForm


class CustomLoginView(auth_views.LoginView):
    authentication_form = CustomUserLoginForm
    redirect_authenticated_user = True


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy("users:password_change_done")


class CustomPasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("users:password_reset_complete")


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("users:login")

    else:
        form = CustomUserCreationForm()

    context = {"form": form}
    return render(request, "users/register.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("main:hub")

    return render(request, "registration/logged_out.html")
