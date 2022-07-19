from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import messages
from django.shortcuts import  redirect


# Custom view access decorators

def admin_required(redirect_url_name, message='Not permitted!'):
    """
    Decorator for view. Checks if the user is admin, if not redirects the user
    to redirect_url_name url and sends a message.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_superuser:
                if message:
                    messages.error(request, message)
                return redirect(redirect_url_name)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def not_admin_required(redirect_url_name, message='Admins cannot go there.'):
    """
    Decorator for view. Checks if the user is admin, if he is then redirects the user
    to redirect_url_name url and sends a message.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_superuser:
                if message:
                    messages.warning(request, message)
                return redirect(redirect_url_name)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def not_logged_in_required(redirect_url_name, message='Cannot access page as a logged in user.'):
    """
    Decorator for view. Checks if the user is authenticated, if not redirects the user
    to redirect_url_name url.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if message:
                    messages.warning(request, message)
                return redirect(redirect_url_name)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator