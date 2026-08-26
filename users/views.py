from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


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


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("main:hub")

    return render(request, "registration/logged_out.html")
