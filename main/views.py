from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item, Auction, Offer
from .forms import ItemForm, AddItemForm, CreateAuctionForm, OfferForm
from .forms import UserUpdateForm

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    offers = Offer.objects.all()
    return render(request,"trading/browse.html",{'offers' : offers})

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
        form = CreateAuctionForm(request.POST)
        auction.auction_title = request.POST.get('auction_title')
        auction.auction_description = request.POST.get('auction_description')
        auction.start_date = request.POST.get('start_date')
        auction.end_date = request.POST.get('end_date')
        auction.minimum_bid = request.POST.get('minimum_bid')
        auction.auction_item_id = Item.objects.get(pk=int(request.POST.get('auction_item_id')))
        auction.save()
        return redirect('auction_browse')
    form = CreateAuctionForm()
    return render(request, "auctions/create_auction.html",{"form":form})

def trade_create(request,pk):
    item = get_object_or_404(Item, id = pk)
    if request.method == 'POST':
        #form = OfferForm(request.POST)
        #if form.is_valid():
        offer = Offer() 
        offer.offer_title = request.POST.get('offer_title') #form.cleaned_data['offer_title']
        offer.offer_desc = request.POST.get('offer_desc') #form.cleaned_data['offer_desc']
        offer.offer_item = item
        offer.save()
        return redirect('trade_browse')
    else: 
        form = OfferForm()
    return render(request, "trading/trade_create.html",{'item': item})

def select_item(request):
    items = Item.objects.filter(owner=request.user.id)
    return render(request,"trading/select_item.html",{'items':items})

def trade_info(request,pk):
    offer = get_object_or_404(Offer, pk=pk)
    return render(request,"trading/trade_info.html",{'offer':offer})

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
            item.image_url = form.cleaned_data['image_url']
            item.owner = User.objects.get(id=int(form.cleaned_data['owner']))
            item.save()
            return redirect('inventory')
    else: 
        form = AddItemForm()
    return render(request, "profile/add_item.html",{'form':form})

def update_account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('update_account')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile/update.html', {
        'user_form': user_form
    })