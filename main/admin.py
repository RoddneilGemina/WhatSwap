from django.contrib import admin
from .models import Item
from .models import Auction
from .models import Offer

# Register your models here.
admin.site.register(Item)
admin.site.register(Auction)
admin.site.register(Offer)