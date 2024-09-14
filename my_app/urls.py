from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('index', views.index),
    path('index2', views.index2),
]
