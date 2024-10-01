from django.db import models

# Create your models here.
class AuctionItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    owner = models.CharField(max_length = 50)
