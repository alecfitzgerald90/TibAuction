from django.urls import path, include
from . import views
from .views import *

app_name = 'auctions'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),

    path('auction', views.auction, name='auction'),
    path('create_auction/', views.create_auction, name='create_auction'),
    path('delete_auction/<pk>/', views.delete_auction, name='delete_auction'),
]