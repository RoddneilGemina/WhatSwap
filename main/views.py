from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item, Auction
from .forms import ItemForm, AddItemForm, CreateAuctionForm, AuctionUpdateForm
from .forms import UserUpdateForm

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    items = Item.objects.all()
    return render(request,"trading/browse.html",{'items' : items})

def auction_browse(request):
    auctionitems = Auction.objects.all()
    return render(request,"auctions/browse.html", {'auctionitems' : auctionitems})


# def auction_create(request):
#     if request.method == 'POST':
#         form = CreateAuctionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('auctions')
#     else: 
#         form = CreateAuctionForm()
#     return render(request, "auctions/create_auction.html",{'form':form})
def auction_create(request):
    if request.method == "POST":
        auction = Auction()
        form = CreateAuctionForm(request.POST, user=request.user)
        auction.auction_title = request.POST.get('auction_title')
        auction.auction_description = request.POST.get('auction_description')
        
        auction.start_date = request.POST.get('start_date')
        auction.end_date = request.POST.get('end_date')

        auction.minimum_bid = request.POST.get('minimum_bid')
        auction.auction_item = Item.objects.get(pk=int(request.POST.get('auction_item_id')))
        auction.save()
        return redirect('auction_browse')
    form = CreateAuctionForm(user=request.user)
    return render(request, "auctions/create_auction.html",{"form":form})

def auction_item(request,pk):
    auction = get_object_or_404(Auction, pk=pk)
    return render(request,"auctions/auction.html",{'auction':auction})

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
    if request.method == 'POST':
        print("DELETE AAA")
        if request.POST.get('is_deleting')=="true":
            print("DELETE BBB")
            request.user.delete()
            return redirect('landing_page')
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
            item.image_url = form.cleaned_data['image_url']
            item.owner = User.objects.get(id=int(form.cleaned_data['owner']))
            item.save()
            return redirect('inventory')
    else: 
        form = AddItemForm()
    return render(request, "profile/add_item.html",{'form':form})

def view_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request,"profile/view_item.html",{'item':item})

def update_account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile/update.html', {
        'user_form': user_form
    })

def auction_update(request,pk):
    if request.method == 'POST':
        auction = Auction.objects.get(pk=int(pk))
        auction_form = AuctionUpdateForm(request.POST, instance=auction)
        auction.auction_title = request.POST.get('auction_title')
        auction.auction_description = request.POST.get('auction_description')
        
        auction.start_date = request.POST.get('start_date')
        auction.end_date = request.POST.get('end_date')

        auction.minimum_bid = request.POST.get('minimum_bid')
        auction.save()
        messages.success(request, 'Your auction has been updated!')
        return redirect(f'/auctions/auction_item/{pk}')
    else:
        auction = Auction.objects.get(pk=int(pk))
        auction_form = AuctionUpdateForm(instance=auction)
    return render(request, 'auctions/update_auction.html', {
        'auction': auction
    })