from django.shortcuts import render, redirect
import requests
from .forms import *
from .models import *
# Create your views here.

def auction(request):
    return render(request, "auctions/auction.html")

def create_auction(request):
    form = AuctionForm(data = request.POST or None, files = request.FILES or None)
    item_form = ItemForm(data=request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid() and item_form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.created_by = request.user
            form_obj.title = f'{request.user}"s Auction'
            form_obj.save()

            item_obj = item_form.save(commit=False)
            item_obj.created_by = request.user
            item_obj.save()
        else:
            print(form.errors, item_form.errors)
    else:
        None

    context = {
        'form': form,
        'item_form': item_form,
    }
    return render(request, "auctions/create_auction.html", context)