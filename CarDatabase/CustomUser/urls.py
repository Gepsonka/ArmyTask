from django.urls import path, include
from .views import user_request_delete_page_view, user_request_delete


urlpatterns = [
    path('user-delete-request/', user_request_delete_page_view, name='user-delete-request'),
    path('user-delete-request-action/', user_request_delete, name='user-delete-request-action'),

]