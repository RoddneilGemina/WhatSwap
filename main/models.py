from django.db import models

# Create your models here.
class AuctionItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    owner = models.CharField(max_length = 50)
    minimum_bid = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
