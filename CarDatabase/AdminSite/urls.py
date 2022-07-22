from django.urls import path, include
from .views import *


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
    path('manufacturers-list/', admin_manufacturer_page_view, name='manufacturers-list'),
    path('manufacturer-creation/', admin_manufacturer_create_view, name='manufacturer-creation'),
    path('manufacturer-deletion/<int:pk>/', admin_manufacturer_delete_view, name='manufacturer-deletion'),
    # Manufacturer request actions
    path('manufacturer-requests/', admin_manufacturer_requests_page_view, name='manufacturer-requests'),
    path('manufacturer-request-delete/<int:pk>/', admin_manufacturer_request_delete_view, name='manufacturer-request-delete'),
    path('manufacturer-request-delete-all/', admin_manufacturer_request_delete_all_view, name='manufacturer-request-delete-all'),
    path('manufacturer-request-fulfill/<int:pk>/', admin_accept_new_manufacturer_request_view, name='manufacturer-request-fulfill'),
    path('manufacturer-request-fulfill-all/', admin_accept_all_new_manufacturer_request_view, name='manufacturer-request-fulfill-all'),
    path('manufacturer-delete-requests/', admin_manufacturer_delete_request_page_view, name='manufacturer-delete-requests'),
    path('manufacturer-fulfill-delete-request/<int:pk>/', admin_manufacturer_delete_request_fulfill_view, name='manufacturer-fulfill-delete-request'),
    path('manufacturer-delete-delete-request/<int:pk>/', admin_manufacturer_delete_request_delete_view, name='manufacturer-delete-delete-request')
]