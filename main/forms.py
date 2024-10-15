from django import forms 

class ItemForm(forms.Form):
    item_name = forms.CharField(label = 'Item Name', max_length=50)
    item_desc = forms.CharField(label = 'Description', max_length=1000)
    