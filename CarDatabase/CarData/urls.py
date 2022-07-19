from django.contrib import admin
from django.urls import path, include
from .views import home_view, car_base_view


urlpatterns = [
    path('home/', home_view, name='home'),
    path('car-query/', car_base_view, name='car-query'),
]
