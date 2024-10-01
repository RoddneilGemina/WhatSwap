from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
