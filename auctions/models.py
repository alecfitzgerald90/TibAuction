from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

    
# Setting the different choices for items and ships
ITEM_CHOICES = [
    ('gun', 'Gun'), ('hull', 'Hull'), 
    ('storage', 'Storage'), ('shield', 'Shield'), 
    ('engine', 'Engine'), ('special', 'Special'), 
    ('fighter drone', 'Fighter Drone'), 
    ('repair drone', 'Repair Drone'), 
    ('harvester', 'Harverster')
]
RARITY_CHOICES = [
    ('uncommon', 'Uncommon'),
    ('rare', 'Rare'),
    ('ultra rare', 'Ultra Rare'),
    ('elite', 'Elite'),
    ('legendary', 'Legendary'),
    ('ultimate', 'Ultimate')
]
RANK_CHOICES = [
    ('i', 'I'),('ii', 'II'),('iii', 'III'),('iv', 'IV'),
    ('v', 'V'),('vi', 'VI'),('vii', 'VII'),('viii', 'VIII'),('ix', 'IX'),
    ('x', 'X'),('xi', 'XI'),('xii', 'XII'),('xiii', 'XIII'),('xiv', 'XIV'),
    ('xv', 'XV'),('xvi', 'XVI'),('xvii', 'XVII'),('xviii', 'XVIII'),('xix', 'XIX'),
    ('xx', 'XX'),('xxi', 'XXI'),('xxii', 'XXII'),('xxiii', 'XXIII'),('xxiv', 'XXIV'),
    ('xxv', 'XXV'),('xxvi', 'XXVI'),('xxvii', 'XXVII'),('xxviii', 'XXVIII'),('xxix', 'XXIX'),
    ('xxx', 'XXX')
]
FACTION_CHOICES = [
    ('human', 'Human'),
    ('pirate', 'Pirate'),
    ('heteroclite', 'Heteroclite'),
    ('wyrd', 'Wyrd'),
    ('precursor', 'Precursor')
]
ELITE_RANK_CHOICES = [
    ('i', 'I'),('ii', 'II'),('iii', 'III'),('iv', 'IV'),
    ('v', 'V')
]

# Status model 
class AuctionStatus(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    # Set to return status name
    def __str__(self):
        return self.name
    
# Item model 
class Item(models.Model):
    item_type = models.CharField(max_length=100, choices=ITEM_CHOICES, blank=True, null=True)
    item_faction = models.CharField(max_length=100, choices=FACTION_CHOICES, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_rarity = models.CharField(max_length=15, choices=RARITY_CHOICES, blank=True, null=True)
    item_rank = models.CharField(max_length=15, choices=RANK_CHOICES, blank=True, null=True)
    item_quality = models.IntegerField()
    item_durability = models.IntegerField()
    item_image = models.ImageField()

class Ship(models.Model):
    ship_type = models.CharField(max_length=100, blank=True, null=True)
    ship_faction = models.CharField(max_length=100, choices=FACTION_CHOICES, blank=True, null=True)
    ship_name = models.CharField(max_length=100, blank=True, null=True)
    ship_elite_ranks = models.CharField(max_length=100, choices=ELITE_RANK_CHOICES, blank=True, null=True)
    ship_durability = models.IntegerField()
    ship_image = models.ImageField()

# Auction model
class Auction(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    starting_bid = models.FloatField()
    buyout = models.FloatField()
    reserve_price = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    # FKs
    status = models.ForeignKey(AuctionStatus, on_delete=models.CASCADE, related_name='auction_status')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='auction_item') # For now, an auction can have 1 and only 1 item OR....
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name='auction_ship')                                 # ... 1 and only one ship
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # set auction to return as it's title
    def __str__(self):
        return self.title
        
class Bid(models.Model):
    bid_amount = models.FloatField()
    time_of_bid = models.DateTimeField(auto_now_add=True)

    # FKs
    auction_bid = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bid_auction')
    item_bid = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bid_item')
    ship_bid = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name='bid_ship')
    user_bid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid_user')