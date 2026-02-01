from django.contrib import admin
from .models import Movie, Category, Review, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)   # ← ВОТ ОН, ФИЛЬТР
    search_fields = ("title", "description")
    list_select_related = ("category",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "rating")
    list_filter = ("rating",)
    search_fields = ("movie__title", "user__username")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("review", "user")
    search_fields = ("user__username", "review__movie__title")
