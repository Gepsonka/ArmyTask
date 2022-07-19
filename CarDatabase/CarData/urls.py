from django.contrib import admin
from django.urls import path, include
from .views import (home_view, car_base_view, car_add_to_favourites_view, create_manufacturer_request_view,
                    create_car_type_view
                    )


urlpatterns = [
    path('home/', home_view, name='home'),
    path('car-query/', car_base_view, name='car-query'),
    path('car-add-favourite/<int:pk>/', car_add_to_favourites_view, name='car-add-favourite'),
    path('car-request-new-manufacturer/', create_manufacturer_request_view, name='request-new-manufacturer'),
    path('car-create-new-type/', create_car_type_view, name='car-create-new-type'),
]
