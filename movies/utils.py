import requests

TMDB_API_KEY = '1f8cfbd7e214356d5ab236b766c6ba47' # Replace with your TMDB API key
BASE_URL = "https://api.themoviedb.org/3/"

def get_tmdb_data(endpoint, params=None):
    if params is None:
        params = {}
    params['1f8cfbd7e214356d5ab236b766c6ba47'] = TMDB_API_KEY
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

def get_popular_movies():
    return get_tmdb_data('movie/popular')

def get_upcoming_movies():
    return get_tmdb_data('movie/upcoming')

def get_top_rated_movies():
    return get_tmdb_data('movie/top_rated')

def search_movies(query):
    return get_tmdb_data('search/movie', {'query': query})
