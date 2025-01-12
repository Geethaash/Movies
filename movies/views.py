from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from . import utils


def homepage(request):
    return HttpResponse("Welcome to the Movie App!")


# Fetch popular movies
@api_view(['GET'])
def get_popular(request):
    try:
        data = utils.get_popular_movies()
        return Response(data)
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)

# Fetch upcoming movies
@api_view(['GET'])
def get_upcoming(request):
    try:
        data = utils.get_upcoming_movies()
        return Response(data)
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)

# Fetch top-rated movies
@api_view(['GET'])
def get_top_rated(request):
    try:
        data = utils.get_top_rated_movies()
        return Response(data)
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)

# Search movies by title
@api_view(['GET'])
def search_movies(request):
    query = request.query_params.get('query', '')
    if not query:
        return Response({"error": "Query parameter is required"}, status=400)
    try:
        data = utils.search_movies(query)
        return Response(data)
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)

# Generate insights (e.g., top movies by rating)
@api_view(['GET'])
def top_movies_by_rating(request):
    try:
        data = utils.get_top_rated_movies()
        sorted_data = sorted(data['results'], key=lambda x: x['vote_average'], reverse=True)
        return Response(sorted_data[:10])  # Return top 10 rated movies
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)
    
class MoviePagination(PageNumberPagination):
    page_size = 20  # Number of results per page
    page_size_query_param = 'page_size'
    max_page_size = 100

# Fetch popular movies with pagination
@api_view(['GET'])
def get_popular(request):
    paginator = MoviePagination()
    try:
        data = utils.get_popular_movies()
        paginated_data = paginator.paginate_queryset(data['results'], request)
        return paginator.get_paginated_response(paginated_data)
    except request.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)
