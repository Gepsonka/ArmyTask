from django.urls import path, include
from .views import users_page_view, user_delete_view, user_creation_view


urlpatterns = [
    path('admin-users/', users_page_view, name='admin-users'),
    path('admin-user-delete/<int:id>/', user_delete_view, name='admin-user-delete'),
    path('admin-user-creation/', user_creation_view, name='admin-user-creation'),
    
]