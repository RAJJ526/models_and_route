from django.contrib import admin
from django.urls import path
from my_app2 import views

urlpatterns = [
    path('home', views.home),
    path('home2', views.home2),
]
