from django.contrib.auth import logout
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


def profile_view(request):
    return render(request, "users/profile.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        # from django.http import HttpResponse
        # return HttpResponse("")
        return redirect("main:hub")

    else:
        return render(request, "registration/logged_out.html")
