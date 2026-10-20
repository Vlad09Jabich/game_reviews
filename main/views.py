from django.shortcuts import render


# TODO: Refactor models logic
def hub_view(request):
    return render(
        request,
        "main/hub.html",
    )
