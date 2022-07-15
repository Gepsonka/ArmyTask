from re import template
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import registration_view, login_view, request_account_retrieve_view


urlpatterns = [
    path("login/", login_view, name = 'login'),
    path("logout/", auth_views.LogoutView.as_view(template_name = "Auth/templates/logout.html"), name = 'logout'),
    path("register/", registration_view, name = "register" ),
    path("retrieve-account/", request_account_retrieve_view, name="retrieve-account"),
    
]