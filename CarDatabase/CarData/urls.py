from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('home/', home_view, name='home'),
    
    path('car-query/', car_base_view, name='car-query'),
    path('car-create-new-type/', create_car_type_view, name='car-create-new-type'),
    # Requests
    path('car-request-new-manufacturer/', create_manufacturer_request_view, name='request-new-manufacturer'),
    path('car-request-manufacturer-delete/', car_create_manufacturer_delete_request_view, name='car-request-manufacturer-delete'),
    # Favourite car views
    path('car-favourite-cars-list/', car_favourite_car_list_view, name='car-favourite-cars-list'),
    path('car-add-favourite/<int:pk>/', car_add_to_favourites_view, name='car-add-favourite'),
    path('car-add-favourites-separately/', car_add_to_favourites_separate_view, name='car-add-favourites-separately'),
    path('car-delete-from-favourites/<int:pk>/', car_delete_car_from_favourites_view, name='car-delete-from-favourites'),
    path('car-favourite-car-update-page/<int:pk>/', car_favourite_car_update_page_view, name='car-favourite-car-update-page'),
    # Fav car image operations 
    path('car-upload-image/<int:pk>/', car_upload_image_view, name='car-upload-image'),
    path('car-delete-image/<int:pk>/', car_image_delete_view, name='car-delete-image'),
]
