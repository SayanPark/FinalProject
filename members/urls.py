from django.urls import path
from . import views

urlpatterns = [
    path('Log-in', views.user_login, name='log-in'),
    path('sign-up', views.signup, name='sign-up'),
    path('logout/', views.user_logout, name='user-logout'),
    path('cp/', views.change_pass, name='change-password')
]
