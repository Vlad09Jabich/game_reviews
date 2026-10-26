from django.shortcuts import get_object_or_404, redirect, render

from users.services import check_user_permission

from .forms import ReviewCreationForm
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


def create_review_view(request):

    if not check_user_permission(request.user.id, "write_reviews"):
        return redirect("users:verify_account")

    if request.method == "POST":
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()

            return redirect("users:profile")

    else:
        form = ReviewCreationForm()

    context = {"form": form}
    return render(request, "reviews/create_review.html", context)
