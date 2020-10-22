from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime

from .models import User, Categories, Listings, Bids, Comments, Watchlist

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        creator = User.objects.get(pk=request.user.id)
        category_id = Categories.objects.get(pk=request.POST["select_category"])
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.POST.get("image")
        starting_bid = float(request.POST.get("starting_bid"))
        activity = "open"
        listing_time = datetime.datetime.now()

        listings = Listings(creator=creator, category_id=category_id, title=title, description=description, image=image, current_bid=starting_bid, activity=activity, listing_time=listing_time)
        listings.save()
        
        return redirect("index")


    return render(request, "auctions/create.html", {
        "categories": Categories.objects.all()
        })

def listing(request, listing_id):

    listing = Listings.objects.get(pk=listing_id)

    if listing.activity == "closed":
        bids = Bids.objects.get(bid=listing.current_bid)
        
        return render(request, "auctions/listing.html", {
            "listing": Listings.objects.get(pk=listing_id),
            "comments": Comments.objects.filter(listing=listing_id),
            "bids" : bids
            })

    if request.user == listing.creator:
        return render(request, "auctions/listing.html", {
            "listing": Listings.objects.get(pk=listing_id),
            "comments": Comments.objects.filter(listing=listing_id),
            "owner" : "yes"
            })
    else:
        return render(request, "auctions/listing.html", {
            "listing": Listings.objects.get(pk=listing_id),
            "comments": Comments.objects.filter(listing=listing_id),
            "owner" : "no"
            })

def bid(request):
    if request.method == "POST":

        bidder = User.objects.get(pk=request.user.id)
        listing = Listings.objects.get(pk=request.POST["bid_listing_id"])
        new_bid = request.POST.get("new_bid")
        bid_time = datetime.datetime.now()
        
        if float(new_bid) > float(listing.current_bid):
            bids = Bids(bidder=bidder, listing=listing, bid=new_bid, bid_time=bid_time)
            bids.save()

            listing.current_bid = new_bid
            listing.save()

            return redirect("listing", listing_id=listing.id)
        else:
            messages.error(request, "Bid must be higher than the current price. Please make a new bid")
            return render(request, "auctions/listing.html", {
        "listing": Listings.objects.get(pk=request.POST["bid_listing_id"]),
        "comments": Comments.objects.filter(listing=request.POST["bid_listing_id"])
        })          

def comment(request):
    if request.method == "POST":
        commenter = User.objects.get(pk=request.user.id)
        listing = Listings.objects.get(pk=request.POST["com_listing_id"])
        comment = request.POST.get("comment")
        comment_time = datetime.datetime.now()

        comments = Comments(commenter=commenter, listing=listing, comment=comment, comment_time=comment_time)
        comments.save()

    return redirect("listing", listing_id=listing.id)

def watchlist(request):
    if request.method == "POST":
        add = request.POST.get("add")
        remove = request.POST.get("remove")

        if add:
            if Watchlist.objects.filter(watcher=request.user.id, listing=request.POST["add_listing_id"]):
                messages.error(request, "This listing is already in your watchlist")
                return render(request, "auctions/listing.html", {
                    "listing": Listings.objects.get(pk=request.POST["add_listing_id"]),
                    "comments": Comments.objects.filter(listing=request.POST["add_listing_id"])
                    })   
        
            else:
                watcher = User.objects.get(pk=request.user.id)
                listing = Listings.objects.get(pk=request.POST["add_listing_id"])

                watchlist = Watchlist(watcher=watcher, listing=listing)
                watchlist.save()
        
        if remove:
            Watchlist.objects.get(watcher=request.user.id, listing=request.POST["remove_listing_id"]).delete()   

    return render(request, "auctions/watchlist.html", {
        "items" : Watchlist.objects.filter(watcher=request.user.id)
        })

def categories(request):

    return render(request, "auctions/categories.html", {
        "categories" : Categories.objects.all()
    })

def category(request, category_id):

    return render(request, "auctions/categories/category.html", {
        "listings" : Listings.objects.filter(category_id=category_id),
        "category" : Categories.objects.get(pk=category_id)
    })

def close(request):

    if request.method == "POST":
        
        listing = Listings.objects.get(pk=request.POST["close_listing_id"])
        listing.activity = request.POST.get("close")
        listing.save()
    
    return redirect("listing", listing_id=listing.id)
        

            