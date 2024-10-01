from django.shortcuts import render
from .models import Item

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    items = Item.objects.all()
    return render(request,"trading/browse/browse.html",{'items' : items})
