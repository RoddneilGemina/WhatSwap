from django.shortcuts import render
from .models import Item, AuctionItem

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    items = Item.objects.all()
    return render(request,"trading/browse/browse.html",{'items' : items})

def auction_browse(request):
    auctionitems = AuctionItem.objects.all()
    return render(request,"auctions/browse.html")

def trade_create(request):
    return render(request, "trading/create_trade/create_trade.html")
