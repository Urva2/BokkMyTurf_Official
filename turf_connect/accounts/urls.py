from django.urls import path
from . import views

urlpatterns = [
    path('player-register/', views.register_player, name='register_player'),
    path('owner-register/', views.register_owner, name='register_owner'),
    path('login/', views.login_view, name='login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', views.logout_view, name='logout'),
]
