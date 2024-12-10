from django import forms 
from django.contrib.auth.models import User
from .models import Auction, Item, Offer, Profile

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

# class AddItemForm(forms.Form):
#     item_name = forms.CharField(label = 'Item Name', max_length=50)
#     item_desc = forms.CharField(label = 'Description', max_length=1000)
#     # image_url = forms.URLField(label = 'Image URL',max_length = 4092)
#     owner = forms.CharField(label = 'Owner ID', max_length=10)  
class AddItemForm(forms.Form):
    item_name = forms.CharField(
        label='Item Name',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Item Name',
            'required': 'required',
            'data-validation-required-message': 'Please enter item name',
        })
    )
    item_desc = forms.CharField(
        label='Description',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'resize: none;',
            'rows': 4,
            'id': 'message',
            'placeholder': 'Description',
            'required': 'required',
            'data-validation-required-message': 'Please enter description',
        })
    )
# class CreateAuctionForm(forms.ModelForm):
#     user = forms.CharField(max_length=50)
#     class Meta:
#         model = Auction
#         fields = [
#             'auction_title',
#             'auction_description',
#             'start_date',
#             'end_date',
#             'minimum_bid',
#             'highest_bid',
#             'auction_item_id'
#             ]
#     def __init__(self, *args, **kwargs):
#         # Get the user instance from kwargs
#         user = kwargs.pop('user', None)
#         super(CreateAuctionForm, self).__init__(*args, **kwargs)
#         # Filter the queryset for 'auction_item_id' to include only items associated with the user
#         if user is not None:
#             self.fields['auction_item_id'].queryset = Item.objects.filter(owner=user.pk)

from django import forms
from .models import Auction, Item

class CreateAuctionForm(forms.ModelForm):
    user = forms.CharField(max_length=50, widget=forms.HiddenInput())  # To store user information if required in the form
    auction_item_id = forms.ModelChoiceField(queryset=Item.objects.none(), label="Select an Item")  # Default empty queryset

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
    
    def __init__(self, *args, **kwargs):
        # Get the user instance from kwargs
        user = kwargs.pop('user', None)
        super(CreateAuctionForm, self).__init__(*args, **kwargs)
        
        # Filter the queryset for 'auction_item_id' to include only items associated with the user
        if user is not None:
            self.fields['auction_item_id'].queryset = Item.objects.filter(owner=user)

            # Optional: You can also customize the widget to improve the dropdown display (e.g., adding a CSS class)
            self.fields['auction_item_id'].widget.attrs.update({'class': 'custom-dropdown'})


class AuctionUpdateForm(forms.ModelForm):
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
        fields = ['username','first_name', 'last_name', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }
class AddProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
        labels = {
            'profile_image': 'Profile Image',
        }
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'id_profile_image',
                'accept': 'image/*'
            })
        }