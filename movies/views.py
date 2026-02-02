from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Movie, Review, Category
from .forms import ReviewForm, CommentForm


def movie_list(request):
    category_id = request.GET.get("category")
    query = request.GET.get("q")

    movies = Movie.objects.all()

    if category_id:
        movies = movies.filter(category_id=category_id)

    if query:
        movies = movies.filter(title__icontains=query)

    categories = Category.objects.all()

    return render(request, "movies/list.html", {
        "movies": movies,
        "categories": categories
    })


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    review_form = ReviewForm()
    comment_form = CommentForm()
    return render(request, "movies/detail.html", {
        "movie": movie,
        "review_form": review_form,
        "comment_form": comment_form
    })


@login_required
def add_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if Review.objects.filter(movie=movie, user=request.user).exists():
        return redirect("movie_detail", pk=pk)

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.movie = movie
        review.save()

    return redirect("movie_detail", pk=pk)


@login_required
def add_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()

    return redirect("movie_detail", pk=review.movie.id)


# 🔹 РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "registration/signup.html", {
        "form": form
    })
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
