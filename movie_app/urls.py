# movie_app/urls.py
from django.contrib import admin
from django.urls import path, include
from movies import views  # Import the views from the movies app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', include('movies.urls')),
    path('', views.homepage, name='homepage'),  # Add this line for the root URL
]
