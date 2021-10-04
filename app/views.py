import logging

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    title='Unsplash'
    return render(request, 'app/index.html', {'title': title})


def health(request):
    try:
        return HttpResponse("OK.")
    except Exception as err:
        logging.error(err)
        raise
