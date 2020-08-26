from django.contrib import admin
from django.urls import path 
from .views import examonline

urlpatterns = [
    path('',examonline),
]
