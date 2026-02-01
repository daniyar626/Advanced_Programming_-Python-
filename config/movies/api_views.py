from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Movie


@csrf_exempt
def api_movies(request):
    # GET — список фильмов
    if request.method == "GET":
        movies = Movie.objects.all()
        data = []

        for movie in movies:
            data.append({
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "category": movie.category.name,
            })

        return JsonResponse(data, safe=False)

    # POST — создать фильм
    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        movie = Movie.objects.create(
            title=body["title"],
            description=body["description"],
            category_id=body["category_id"],
        )

        return JsonResponse({
            "message": "Movie created",
            "id": movie.id
        }, status=201)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def api_movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)

    # GET — один фильм
    if request.method == "GET":
        return JsonResponse({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "category": movie.category.name
        })

    # PUT — обновить
    if request.method == "PUT":
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        movie.title = body.get("title", movie.title)
        movie.description = body.get("description", movie.description)
        movie.category_id = body.get("category_id", movie.category_id)
        movie.save()

        return JsonResponse({"message": "Movie updated"})

    # DELETE — удалить
    if request.method == "DELETE":
        movie.delete()
        return JsonResponse({"message": "Movie deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
