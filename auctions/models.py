from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"

class Listings(models.Model):
    creator = models.ForeignKey(User, related_name="creator", on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, related_name="category_id", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description =  models.CharField(max_length=300)
    image = models.URLField(null=True)
    current_bid = models.FloatField(max_length=50)
    listing_time = models.DateField()

    def __str__(self):
        return f"User {self.creator} auctioned '{self.title}' in '{self.category_id}' category at {self.listing_time}"

class Bids(models.Model):
    bidder = models.ForeignKey(User, related_name="bidder", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, related_name="bidded", on_delete=models.CASCADE)
    bid = models.FloatField(max_length=10)
    bid_time = models.DateField()

    def __str__(self):
        return f"User {self.bidder} bidded ${self.bid} in '{self.listing.title}' of {self.listing.creator} at {self.bid_time}"

class Comments(models.Model):
    commenter = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, related_name="commented", on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    comment_time = models.DateField()

    def __str__(self):
        return f"User {self.commenter} commented '{self.comment}' in {self.listing} at {self.comment_time}"

class Watchlist(models.Model):
    watcher = models.ForeignKey(User, related_name="watcher", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, related_name="listing", on_delete=models.CASCADE)
    current_bid = models.ForeignKey(Bids, related_name="current_bid", on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.watcher} is watching {self.listing}. Highest bid is {self.current_bid}"