from django.contrib import admin
from .models import Movie, Category, Review, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)
    search_fields = ("title",)


admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Comment)
