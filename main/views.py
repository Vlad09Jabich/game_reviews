from django.shortcuts import get_object_or_404, render

from .models import Review


# TODO: Refactor models logic
def hub_view(request):
    return render(
        request,
        "main/hub.html",
    )


def index_view(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "main/index.html", context)


def detail_view(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "main/detail.html", context)
