from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('trades/', views.trade_browse, name='trade_browse'),
    path('auctions/', views.auction_browse, name='auction_browse') 
]