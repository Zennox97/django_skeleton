# urls.py -- maps the urls of app
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
