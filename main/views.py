from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Item, AuctionItem
from .forms import ItemForm, AddItemForm

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    items = Item.objects.all()
    return render(request,"trading/browse.html",{'items' : items})

def auction_browse(request):
    auctionitems = AuctionItem.objects.all()
    return render(request,"auctions/browse.html", {'auctionitems' : auctionitems})
    return render(request,"auctions/browse.html")

def auction_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item()
            item.item_name = form.cleaned_data['item_name']
            item.item_desc = form.cleaned_data['item_desc']
            item.save()
            return redirect('../../auctions')
    else: 
        form = ItemForm()
    return render(request, "auctions/create_auction.html",{'form':form})

def trade_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item()
            item.item_name = form.cleaned_data['item_name']
            item.item_desc = form.cleaned_data['item_desc']
            item.save()
            return redirect('../../trades')
    else: 
        form = ItemForm()
    return render(request, "trading/create_trade.html",{'form':form})

def trade_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request,"trading/iteminfo.html",{'item':item})

def profile(request):
    return render(request,"profile/my_profile.html")

def inventory(request):
    items = Item.objects.filter(owner=request.user.id)
    return render(request,"profile/inventory.html",{'items':items})

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = Item()
            item.item_name = form.cleaned_data['item_name']
            item.item_desc = form.cleaned_data['item_desc']
            item.owner = User.objects.get(id=int(form.cleaned_data['owner']))
            item.save()
            return redirect('/profile/')
    else: 
        form = AddItemForm()
    return render(request, "profile/add_item.html",{'form':form})
