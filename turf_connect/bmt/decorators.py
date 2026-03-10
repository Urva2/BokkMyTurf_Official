from functools import wraps
from django.shortcuts import redirect


def login_required_custom(view_func):
    """Redirect unauthenticated users to the login page."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def player_required(view_func):
    """Allow only authenticated users with role == 'player'."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.role != 'player':
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


def owner_required(view_func):
    """Allow only authenticated users with role == 'owner'."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.role != 'owner':
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    """Allow only authenticated users with role == 'admin'."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.role != 'admin':
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper
