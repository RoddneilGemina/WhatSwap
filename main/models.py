from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    account = models.ForeignKey(User, on_delete = models.CASCADE)
    # rating = models.FloatField(name = "Rating",default=1.0,min=1.0,max=5.0)
    
class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True)
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=512,null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.item_name}"

class Auction(models.Model):
    auction_title = models.CharField(max_length = 100)
    auction_description = models.TextField(max_length = 500)

    start_date = models.DateTimeField(default = tz.now)
    end_date = models.DateTimeField(default = tz.now)

    minimum_bid = models.FloatField(default = 0.0)
    highest_bid = models.FloatField(default = 0.0)
    highest_bidder_id = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

    class AuctionStatus(models.TextChoices):
        NOT_STARTED = 'NOT STARTED'
        ONGOING = 'ONGOING'
        FINISHED = 'FINISHED'
        CANCELLED = 'CANCELLED'

    auction_status = models.CharField(
        max_length = 20,
        choices = AuctionStatus.choices,
        default = AuctionStatus.NOT_STARTED,
    )

    auction_item_id = models.ForeignKey(Item, on_delete = models.CASCADE)