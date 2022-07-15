from django.contrib import admin
from django.urls import path, include
from .views import home_view


urlpatterns = [
    path('home/', home_view, name='home'),
]
