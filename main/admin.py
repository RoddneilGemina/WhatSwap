from django.contrib import admin
from .models import Item
from .models import Auction
from .models import Rating
from .models import Offer
from .models import Profile
from .models import Bid

# Register your models here.
admin.site.register(Item)
admin.site.register(Auction)
admin.site.register(Rating)
admin.site.register(Offer)
admin.site.register(Bid)
admin.site.register(Profile)