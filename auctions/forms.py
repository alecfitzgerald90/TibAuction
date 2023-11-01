from django import forms
from .models import *


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = [
            'title',
            'starting_bid',
            'buyout',
            'reserve_price',
            'start_time',
            'end_time',
        ]
        widgets = {
            'starting_bid': forms.NumberInput(attrs={'min': '1.00'}),
            'buyout': forms.NumberInput(attrs={'min': '1.00'}),
            'reserve_price': forms.NumberInput(attrs={'min': '1.00'}),
            'start_time': forms.TextInput(attrs={'class': 'date-picker'}),
            'end_time': forms.TextInput(attrs={'class': 'date-picker'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['starting_bid'].label = 'Starting Bid'
        self.fields['reserve_price'].label = 'Reserve Price'
        self.fields['buyout'].label = 'Buyout Price'
        self.fields['start_time'].label = 'Auction Start Time'
        self.fields['end_time'].label = 'Auction End Time'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_type',
            'item_faction',
            'item_name',
            'item_rarity',
            'item_rank',
            'item_quality',
            'item_durability',
            'item_image',
        ]
        widgets = {
            'item_quality': forms.NumberInput(attrs={'min': '1', 'max': '240'}),
            'item_durability': forms.NumberInput(attrs={'min': '1', 'max': '100'})
        }