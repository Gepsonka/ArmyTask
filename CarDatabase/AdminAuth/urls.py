from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import admin_login_view

urlpatterns = [
    path("admin-login/", admin_login_view, name='admin-login'),
    
]