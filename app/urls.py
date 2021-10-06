from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nyc', views.nyc, name='nyc'),
    path('architecture', views.architecture, name='architecture'),
    path('health', views.health, name='index')
]
