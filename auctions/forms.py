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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['starting_bid'].label = 'Starting Bid'
        self.fields['reserve_price'].label = 'Reserve Price'
        self.fields['buyout'].label = 'Buyout Price'
        self.fields['start_time'].label = 'Auction Start Time'
        self.fields['end_time'].label = 'Auction End Time'