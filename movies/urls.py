from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.get_popular, name='get_popular'),
    path('upcoming/', views.get_upcoming, name='get_upcoming'),
    path('top-rated/', views.get_top_rated, name='get_top_rated'),
    path('search/', views.search_movies, name='search_movies'),
    path('top-movies-by-rating/', views.top_movies_by_rating, name='top_movies_by_rating'),
]
