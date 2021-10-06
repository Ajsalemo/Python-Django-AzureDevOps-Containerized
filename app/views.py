import logging

import requests
from django.http import HttpResponse
from django.shortcuts import render
from unsplash.env import UNSPLASH_API_ACCESS_KEY, UNSPLASH_API_PREFIX


def index(request):
    search_unsplash_photos = requests.get(
        f'{UNSPLASH_API_PREFIX}/search/photos?query="new york city"', headers={'Authorization': f'Client-ID {UNSPLASH_API_ACCESS_KEY}'})
    search_photos_json = search_unsplash_photos.json()
    return render(request, 'app/index.html', {'search_photos_json': search_photos_json['results']})


def nyc(request):
    search_nyc_photos = requests.get(
        f'{UNSPLASH_API_PREFIX}/search/photos?query="nyc"', headers={'Authorization': f'Client-ID {UNSPLASH_API_ACCESS_KEY}'})
    search_nyc_photos_json = search_nyc_photos.json()
    return render(request, 'app/index.html', {'search_photos_json': search_nyc_photos_json['results']})


def architecture(request):
    search_architecture_photos = requests.get(
        f'{UNSPLASH_API_PREFIX}/search/photos?query="architecture"', headers={'Authorization': f'Client-ID {UNSPLASH_API_ACCESS_KEY}'})
    search_architecture_photos_json = search_architecture_photos.json()
    return render(request, 'app/index.html', {'search_photos_json': search_architecture_photos_json['results']})


def health(request):
    try:
        return HttpResponse("OK.")
    except Exception as err:
        logging.error(err)
        raise
