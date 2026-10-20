from django.shortcuts import get_object_or_404, render

from .models import Review


def index_view(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "reviews/index.html", context)


def detail_view(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)
