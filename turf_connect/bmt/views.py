from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

User = get_user_model()


@login_required(login_url='login')
def player_home(request):
    if request.user.role != 'player':
        return HttpResponseForbidden("Access denied.")
    return render(request, 'playerdashboard.html')


@login_required(login_url='login')
def owner_home(request):
    if request.user.role != 'owner':
        return HttpResponseForbidden("Access denied.")
    return render(request, 'ownerdashboard.html')


@login_required(login_url='login')
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Access denied.")
    return render(request, 'admindashboard.html')
