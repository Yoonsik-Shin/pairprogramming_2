from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def main(request):
    return render(request, "movie_crud/main.html")

def index(request):
    reviews = Review.objects.all().order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "movie_crud/index.html", context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_crud:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'movie_crud/create.html', context)