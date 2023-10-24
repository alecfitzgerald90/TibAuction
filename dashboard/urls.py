from django.urls import path, include
from . import views

app_name = 'dashboard'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
]