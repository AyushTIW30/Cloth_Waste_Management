from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # <-- use the 'home' function you have in views.py
]
