from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import PlayerRegistrationForm, OwnerRegistrationForm

User = get_user_model()


def login_view(request):
    """Authenticate user by email and redirect based on role."""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.role == User.Role.ADMIN:
                return redirect('admin_dashboard')
            elif user.role == User.Role.OWNER:
                return redirect('owner_home')
            else:
                return redirect('player_home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'playerlogin.html')


@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')


def register_player(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = PlayerRegistrationForm()
    return render(request, 'playerregistration.html', {'form': form})


def register_owner(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Owner account created successfully! Please log in.')
            return redirect('login')
    else:
        form = OwnerRegistrationForm()
    return render(request, 'ownerregistration.html', {'form': form})


def admin_login(request):
    """Separate login page for admin users."""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.role == 'admin':
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials.')

    return render(request, 'adminlogin.html')
