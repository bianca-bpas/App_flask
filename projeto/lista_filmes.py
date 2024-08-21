import requests
import json

def resultado_filmes(tipo):
    if tipo == 'Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key=d1a651ea93a961f4e2245821f429e7b6'
    elif tipo == 'Animação':
        url = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=16&api_key=d1a651ea93a961f4e2245821f429e7b6'
    elif tipo == '2010':
        url = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2010&sort_by=popularity.desc&api_key=d1a651ea93a961f4e2245821f429e7b6'

    response = requests.get(url)

    dados = response.json()
    return dados['results']

