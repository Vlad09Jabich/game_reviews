from django.shortcuts import get_object_or_404, render

from .decorators import time_it
from .models import Review


@time_it
def hub(request):
    return render(request, "main/hub.html")


@time_it
def index(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "main/index.html", context)


@time_it
def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "main/detail.html", context)
