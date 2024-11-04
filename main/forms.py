from django import forms 
from django.contrib.auth.models import User
from .models import Auction, Offer

class ItemForm(forms.Form):
    item_name = forms.CharField(label = 'Item Name', max_length=50)
    item_desc = forms.CharField(label = 'Description', max_length=1000)

class OfferForm(forms.Form):
    class Meta:
        model = Offer
        fields = [
        'offer_title'
        'offer_desc'
        'offer_item_name'
        'offer_image_url'
        'offer_owner'
        'date_offered'
        'is_directed'
        'directed_offer_id'
        ]

class AddItemForm(forms.Form):
    item_name = forms.CharField(label = 'Item Name', max_length=50)
    item_desc = forms.CharField(label = 'Description', max_length=1000)
    image_url = forms.URLField(label = 'Image URL',max_length = 4092)
    owner = forms.CharField(label = 'Owner ID', max_length=10)  

class CreateAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = [
            'auction_title',
            'auction_description',
            'start_date',
            'end_date',
            'minimum_bid',
            'highest_bid',
            'auction_item_id'
            ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
