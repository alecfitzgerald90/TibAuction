from django.urls import path, include
from . import views
from .views import *

app_name = 'auctions'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),

    path('auction', views.auction, name='auction'),
    path('create_auction/', views.create_auction, name='create_auction'),
]