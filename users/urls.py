from django.urls import path, include
from . import views
from .views import *
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),

    # Registration page
    # path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<pk>/', views.profile_detail, name='profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('reset_password/', views.reset_password, name='reset_password'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]