from django.shortcuts import render

from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # return redirect("users:login")
            from django.http import HttpResponse

            return HttpResponse("Вы успешно зарегистрировались!")

    else:
        form = CustomUserCreationForm()

    context = {"form": form}
    return render(request, "users/register.html", context)
