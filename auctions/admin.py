from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Auction)
admin.site.register(AuctionStatus)
admin.site.register(Item)
admin.site.register(Ship)
admin.site.register(Bid)