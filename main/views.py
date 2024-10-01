from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,"landing/landing.html")

def auction_browse(request):
    return render(request,"auctions/browse.html")