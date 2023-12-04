from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.

def auction(request):
    auctions = Auction.objects.all()
    context = {
        'auctions': auctions,
    }
    return render(request, "auctions/auction.html", context)


def create_auction(request):
    form = AuctionForm(data = request.POST or None, files = request.FILES or None)
    item_form = ItemForm(data=request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        auction_obj = form.save(commit=False)
        auction_obj.created_by = request.user
        auction_obj.save()

        item_obj = item_form.save(commit=False)
        item_obj.auction = auction_obj
        item_obj.save()  

        messages.success(request, "Auction created!!")
        return redirect('/auctions/auction')
    else:
        
        messages.error(request, "There was an issue with the form submission. Please check the information provided and try again.")
  
    context = {
        'form': form,
        'item_form': item_form,
    }
    return render(request, "auctions/create_auction.html", context)

    

def delete_auction(request, pk):
    auction = Auction.objects.get(id=pk)
    auction.delete()
    messages.success(request, "Auction successfully deleted")
    return redirect('/auctions/auction')
    
