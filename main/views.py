from django.shortcuts import get_object_or_404, render

from .models import Review


def index(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "main/index.html", context)


def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "main/detail.html", context)