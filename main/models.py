from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuctionItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    owner = models.CharField(max_length = 50)
    minimum_bid = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank = True)
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=512,null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(name = "Rating",default=1.0,min=1.0,max=5.0)
    
