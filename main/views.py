from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render

from .decorators import time_it
from .forms import WriteReviewForm
from .models import Review


@time_it
def hub_view(request):
    return render(
        request,
        "main/hub.html",
        {"is_author": request.user.groups.filter(name="Authors").exists()},
    )


def index_view(request):
    review_list = Review.objects.all()
    context = {"review_list": review_list}
    return render(request, "main/index.html", context)


def detail_view(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {"review": review}
    return render(request, "main/detail.html", context)


def become_author_view(request):
    if request.user.groups.filter(name="Authors").exists():
        return redirect("main:hub")

    if request.method == "POST":
        request.user.groups.add(Group.objects.get(name="Authors"))
        return redirect("main:hub")

    return render(request, "main/become_author.html")


# @authors_only
def write_review_view(request):
    if not request.user.groups.filter(name="Authors").exists():
        return redirect("main:hub")

    if request.method == "POST":
        form = WriteReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()

            return redirect("main:hub")
    else:
        form = WriteReviewForm()

    context = {"form": form}
    return render(request, "main/write_review.html", context)
