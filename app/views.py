import logging

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def health(request):
    try:
        return HttpResponse("OK.")
    except Exception as err:
        logging.error(err)
        raise
