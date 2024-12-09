from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User

# Crseate your models here.
class Profile(models.Model):
    account = models.ForeignKey(User, on_delete = models.CASCADE)
    image_url = models.CharField(max_length=4092,null=True, blank = True)

class Rating(models.Model):
    ratee = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True, related_name="Ratee")
    rater = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True, related_name="Rater")
    #comment = models.TextField(max_length=256, null = True, blank = True)
    value = models.FloatField(default=1.0)
    def __str__(self):
        return f"{self.rater} for {self.ratee}: {self.value}"

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True)
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=4092,null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.item_name}"
    
class Offer(models.Model):
    offer_title = models.CharField(max_length = 100)
    offer_desc = models.TextField(max_length = 500)
    offer_item = models.ForeignKey(Item, on_delete=models.CASCADE, null = True)
    offer_image_url = models.CharField(max_length= 500, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fthenounproject.com%2Fbrowse%2Ficons%2Fterm%2Fimage-default%2F&psig=AOvVaw0AmbHrPZZfAhJINI2MKJQP&ust=1730758995426000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPDKxOqZwYkDFQAAAAAdAAAAABAI")
    date_offered = models.DateTimeField(default = tz.now)
    is_directed = models.BooleanField(default = False)
    directed_offer_id = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)

    # added
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    class OfferStatus(models.TextChoices):
        CLOSED = 'CLOSED'
        PENDING = 'PENDING'
        STANDBY = 'STANDBY'

    offer_status = models.CharField(
        max_length = 20,
        choices = OfferStatus.choices,
        default = OfferStatus.STANDBY,
    )

class Auction(models.Model):
    auction_title = models.CharField(max_length = 100)
    auction_description = models.TextField(max_length = 500)

    is_deleted = models.BooleanField(default = False)

    start_date = models.DateTimeField(default = tz.now)
    end_date = models.DateTimeField(default = tz.now)

    minimum_bid = models.DecimalField(default = 0.0, max_digits = 10, decimal_places=2)
    highest_bid = models.DecimalField(default = 0.0, max_digits = 10, decimal_places=2)
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