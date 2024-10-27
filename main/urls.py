from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('trades/', views.trade_browse, name='trade_browse'),
    path('auctions/', views.auction_browse, name='auction_browse'),
    path('auctions/auction_create/', views.auction_create, name='auction_create'),
    path('trades/trade_create/', views.trade_create, name ='trade_create'),
    path('trades/trade_item/<int:pk>/', views.trade_item, name="trade_item"),
    path('profile/', views.profile, name ='profile'),
    path('profile/add_item/', views.add_item, name ='add_item'),
    path('profile/inventory/', views.inventory, name ='inventory'),
]