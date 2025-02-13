import requests

TMDB_API_KEY = 'TMDB API Key'
TMDB_BASE_URL = 'https://api.themoviedb.org/3/'

def popular_movies():
    url = f"{'https://api.themoviedb.org/3/'}movie/popular?api_key={'TMDB API Key'}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return data

def top_rated_movies():  
    url = f"{'https://api.themoviedb.org/3/'}movie/top_rated?api_key={'TMDB API Key'}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return data
   
