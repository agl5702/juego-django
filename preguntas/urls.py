from django.contrib import admin
from django.urls import path
from .views import Juego

urlpatterns = [
    path('',Juego, name='juego')
]
