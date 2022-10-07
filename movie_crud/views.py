from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def main(request):
    reviews = Review.objects.all().order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "movie_crud/main.html", context)


def index(request):
    reviews = Review.objects.all().order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "movie_crud/index.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_crud:main")
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "movie_crud/create.html", context)


def detail(request, pk):
    review_detail = Review.objects.get(id=pk)
    context = {
        "review_detail": review_detail,
    }
    return render(request, "movie_crud/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    review_form = ReviewForm(instance=review)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("movie_crud:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {"review_form": review_form}
    return render(request, "movie_crud/update.html", context)


def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect("movie_crud:index")
