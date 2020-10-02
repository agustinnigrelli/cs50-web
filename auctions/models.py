from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"

class Listings(models.Model):
    user_id = models.ForeignKey(User, related_name="auctioner", on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, related_name="category_id", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description =  models.CharField(max_length=300)
    image = models.URLField(null=True)
    auction_time = models.DateField()

    def __str__(self):
        return f"User {self.user_id} auctioned '{self.title}' in '{self.category_id}' category at {self.auction_time}"

class Bids(models.Model):
    user_id = models.ForeignKey(User, related_name="bidder", on_delete=models.CASCADE)
    auction = models.ForeignKey(Listings, related_name="bidded", on_delete=models.CASCADE)
    bid = models.FloatField(max_length=10)
    bid_time = models.DateField()

    def __str__(self):
        return f"User {self.user_id} bidded ${self.bid} in {self.auction} at {self.bid_time}"

class Comments(models.Model):
    user_id = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, related_name="commented", on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    comment_time = models.DateField()

    def __str__(self):
        return f"User {self.user_id} commented '{self.comment}' in {self.listing} at {self.comment_time}"

class Watchlist(models.Model):
    user_id = models.ForeignKey(User, related_name="watcher", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, related_name="listing", on_delete=models.CASCADE)
    current_bid = models.ForeignKey(Bids, related_name="current_bid", on_delete=models.CASCADE)
    current_comments = models.ForeignKey(Comments, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user_id} is watching {self.listing}"