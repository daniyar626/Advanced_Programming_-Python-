from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("movie/<int:pk>/review/", views.add_review, name="add_review"),
    path("comment/<int:review_id>/", views.add_comment, name="add_comment"),
    path("signup/", views.signup, name="signup"),

    # API
    path("api/movies/", api_views.api_movies),
    path("api/movies/<int:pk>/", api_views.api_movie_detail),
]
