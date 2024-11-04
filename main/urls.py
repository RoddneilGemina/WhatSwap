from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('trades/', views.trade_browse, name='trade_browse'),
    path('auctions/', views.auction_browse, name='auction_browse'),
    path('auctions/auction_create/', views.auction_create, name='auction_create'),
    path('trades/select_item/', views.select_item, name ='select_item'),
    path('trades/trade_create/<int:pk>/', views.trade_create, name="trade_create"),
    path('trades/trade_info/<int:pk>/', views.trade_info, name="trade_info"),
    path('auctions/auction_item/<int:pk>/', views.auction_item, name="trade_item"),
    path('auctions/auction_update/<int:pk>/', views.auction_update, name="auction_update"),
    path('trades/trade_create/', views.trade_create, name ='trade_create'),
    path('trades/trade_item/<int:pk>/', views.trade_item, name="trade_item"),
    path('profile/', views.profile, name ='profile'),
    path('profile/add_item/', views.add_item, name ='add_item'),
    path('profile/inventory/', views.inventory, name ='inventory'),
    path('profile/update_account/', views.update_account, name ='update_account'),
    path('profile/inventory/<int:pk>',views.view_item, name='view_item')
]