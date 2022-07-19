from django.urls import path, include
from .views import (
        users_page_view, user_delete_view, user_delete_all_view, user_delete_page_view,
        user_creation_view , user_unlock_page_view, user_unlock_view,
        user_unlock_all_view, make_admin_view, revoke_admin_view, user_update_page_view,
        car_manufacturer_page_view, car_manufacturer_create_view, car_manufacturer_delete_view,
        car_manufacturer_requests_page_view
    )


urlpatterns = [
    # User list views
    path('admin-users/', users_page_view, name='admin-users'),
    # Account delete views
    path('admin-user-delete', user_delete_page_view, name='admin-user-delete'),
    path('admin-user-delete-action/<int:id>/', user_delete_view, name='admin-user-delete-action'),
    path('admin-user-delete-all-action/', user_delete_all_view, name='admin-user-delete-all-action'),
    # Account unlock views
    path('admin-user-unlock/', user_unlock_page_view, name='admin-user-unlock'),
    path('admin-user-unlock-action/<int:id>/', user_unlock_view, name='admin-user-unlock-action'),
    path('admin-user-unlock-all-action/', user_unlock_all_view, name='admin-user-unlock-all-action'),
    # Account creation view
    path('admin-user-creation/', user_creation_view, name='admin-user-creation'),
    # Account update view 
    path('admin-user-update/<int:id>/', user_update_page_view, name='admin-user-update'),
    # Admin right adder
    path('make-admin/<int:id>/', make_admin_view, name='make-admin'),
    # Admin right revoker
    path('revoke-admin/<int:id>/', revoke_admin_view, name='revoke-admin'),
    # Car database actions
    path('manufacturers-list/', car_manufacturer_page_view, name='manufacturers-list'),
    path('manufacturer-creation/', car_manufacturer_create_view, name='manufacturer-creation'),
    path('manufacturer-deletion/<int:pk>/', car_manufacturer_delete_view, name='manufacturer-deletion'),
    # Manufacturer request actions
    path('manufacturer-requests/', car_manufacturer_requests_page_view, name='manufacturer-requests'),
]