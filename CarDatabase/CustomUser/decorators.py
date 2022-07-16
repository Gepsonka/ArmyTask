from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import messages
from django.shortcuts import  redirect




def admin_user_required(redirect_url_name, message='Log in as admin first!'):
    """
    Decorator for view. Checks if the user is admin, if not redirects the user
    to redirect_url_name url and sends a message.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_superuser:
                messages.error(request, message)
                return redirect(redirect_url_name)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator