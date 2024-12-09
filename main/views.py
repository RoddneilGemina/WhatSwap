from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item, Auction, Offer, Rating
from .forms import ItemForm, AddItemForm, CreateAuctionForm, AuctionUpdateForm, OfferForm
from .forms import UserUpdateForm
import copy

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def trade_browse(request):
    offers = Offer.objects.all()
    return render(request,"trading/browse.html",{'offers' : offers})

def auction_browse(request):
    auctionitems = Auction.objects.filter(is_deleted = False)
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

    if request.method == 'POST':
        if request.POST.get('isDeleting') == 'true':
            auction.is_deleted = True
            auction.save()

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

def profile(request,pk):
    user_get = get_object_or_404(User,pk=pk)
    ratings = Rating.objects.filter(ratee=user_get)
    # ratings = Rating.objects.all()
    # for i in ratings:
    #     i.delete()
    if request.method == 'POST':
        if request.POST.get('is_deleting')=="true":
            request.user.delete()
            return redirect('landing_page')
        if request.POST.get('is_rating')=="true":
            rating = Rating()
            rating.ratee = get_object_or_404(User,pk=int(request.POST.get('ratee_id')))
            rating.rater = get_object_or_404(User,pk=int(request.POST.get('rater_id')))
            rating.value = float((request.POST.get('rating_value')))
            rating.save()
            return redirect(f"/profile/{pk}")
        if request.POST.get('rating_operation')=='true':
            if request.POST.get('rating_update_id') != None:
                rating = get_object_or_404(Rating,pk=int(request.POST.get('rating_update_id')))
                print(f"update rating {rating}") #INCOMPLETE
            elif request.POST.get('rating_delete_id') != None:
                rating = get_object_or_404(Rating,pk=int(request.POST.get('rating_delete_id')))
                rating.delete()
            return redirect(f"/profile/{pk}")
    return render(request,"profile/my_profile.html",{"user_get":user_get,"ratings":ratings})

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
    if request.method == 'POST':
        if request.POST.get('item_update_id') != None:
            print("UPDATE ITEM") # INCOMPLETE
        if request.POST.get('item_delete_id') != None:
            item.delete()
            print("DELETED ITEM")
            return redirect('/profile/inventory')
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
def trade_create(request,pk):
    item = get_object_or_404(Item, id = pk)
    if request.method == 'POST':
        #form = OfferForm(request.POST)
        #if form.is_valid():
        offer = Offer() 
        offer.offer_title = request.POST.get('offer_title') #form.cleaned_data['offer_title']
        offer.offer_desc = request.POST.get('offer_desc') #form.cleaned_data['offer_desc']
        offer.offer_item = item
        offer.author = request.user
        offer.save()
        return redirect('trade_browse')
    else: 
        form = OfferForm()
    return render(request, "trading/trade_create.html",{'item': item})

def directed_select_item(request,pk):
    target = Offer.objects.get(pk = pk)
    doffers = Offer.objects.filter(directed_offer_id = target)
    ritems = Item.objects.filter(owner=request.user.id)
    ditems = []
    items = []
    for d in doffers:
        ditems.append(d.offer_item)
    for i in ritems:
        if i not in ditems:
            items.append(i)
    if request.method == "POST":
        doffer = Offer()
        ditem = Item.objects.get(pk=int(request.POST.get('item')))
        doffer.offer_title = ditem.item_name
        doffer.offer_item = ditem
        doffer.is_directed = True
        doffer.directed_offer_id = target
        doffer.author = request.user
        doffer.save()
        return redirect('trade_info', pk)
    return render(request,"trading/directed_select_item.html",{'items':items, 'target': target})

def select_item(request):
    offers = Offer.objects.filter(author=request.user)
    ritems = Item.objects.filter(owner=request.user.id)
    ditems = []
    items = []
    for d in offers:
        ditems.append(d.offer_item)
    for i in ritems:
        if i not in ditems:
            items.append(i)
    for o in offers:
        if o.offer_status == 'CLOSED' and o.offer_item.owner == request.user.id:
            items.append(o.offer_item)

    return render(request,"trading/select_item.html",{'items':items})

def trade_info(request,pk):
    offer = get_object_or_404(Offer, pk=pk)
    doffers = Offer.objects.filter(directed_offer_id = offer)
    if request.method == "POST":
        if request.POST.get('is_deleting')=="true":
            offer.delete()
            return redirect('trade_browse')
        elif request.POST.get('is_accepted')=="true":
            itemA = offer.directed_offer_id.offer_item
            itemB = offer.offer_item
            
            temp = copy.deepcopy(itemA)
            itemA.owner = itemB.owner
            itemB.owner = temp.owner

            itemA.save()
            itemB.save()
            
            offer.directed_offer_id.offer_status = 'CLOSED'
            offer.offer_status = 'CLOSED'
            offer.save()
            offer.directed_offer_id.save()
            return redirect('trade_browse')
        elif request.POST.get('is_accepted')=="false":
            offer.delete()
            return redirect('trade_browse')
    return render(request,"trading/trade_info.html",{'offer':offer,'doffers':doffers})

def trade_update(request,pk):
    if request.method == 'POST':
        offer = Offer.objects.get(pk=int(pk))
        offer.offer_title = request.POST.get('offer_title')
        offer.offer_desc = request.POST.get('offer_desc')
        offer.save()
        messages.success(request, 'Your offer has been updated!')
        return redirect(f'/trades/trade_info/{pk}')
    else:
        offer = Offer.objects.get(pk=int(pk))
    return render(request, 'trading/trade_update.html', {
        'offer': offer
    })