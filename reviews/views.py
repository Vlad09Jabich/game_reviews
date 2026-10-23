from django.shortcuts import get_object_or_404, render

from .models import Review


def all_reviews_view(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "reviews/all_reviews.html", context)


def review_detail_view(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "reviews/review_detail.html", context)


def main_page_view(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "reviews/main_page.html", context)
