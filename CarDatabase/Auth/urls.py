from re import template
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import registration_view


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name = 'Auth/templates/login.html'), name = 'login'),
    path("logout/", auth_views.LogoutView.as_view(template_name = "Auth/templates/logout.html"), name = 'logout'),
    path("register/", registration_view, name = "register" ),
    
]