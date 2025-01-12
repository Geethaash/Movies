import requests

TMDB_API_KEY = '1f8cfbd7e214356d5ab236b766c6ba47'
TMDB_BASE_URL = 'https://api.themoviedb.org/3/'

def popular_movies():
    url = f"{'https://api.themoviedb.org/3/'}movie/popular?api_key={'1f8cfbd7e214356d5ab236b766c6ba47'}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return data

def top_rated_movies():  # Similarly, ensure correct name here
    url = f"{'https://api.themoviedb.org/3/'}movie/top_rated?api_key={'fbd7e214356d5ab236b766c6ba47'}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return data
   
