import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Exists, OuterRef, Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime

from .models import User, Subject, Announcement, Bookmark


@login_required
def index(request):
    
    if not Announcement.objects.filter(user=request.user):
        announcements = "None"
    else:
        announcements = Announcement.objects.filter(user=request.user)

    return render(request, "odeon/index.html", {
        "announcements": announcements
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
            return render(request, "odeon/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "odeon/login.html")


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
            return render(request, "odeon/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "odeon/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "odeon/register.html")


def search(request):

    if request.method == "POST":
        q = request.POST.get("q")

        if not q or q == "":
            founded = "None"
        
        else:
            founded = Announcement.objects.filter(
                Q(user__username__contains=q) | 
                Q(title__contains=q) | 
                Q(body__contains=q)
            ).annotate(
                is_bookmarked=Exists(Bookmark.objects.filter(announcement=OuterRef('pk'), user=request.user))
            ).order_by("-timestamp")
        
        return render(request, "odeon/search.html", {
            "founded": founded
        })

@login_required
def password(request):
    
    if request.method == "POST":

        user = User.objects.get(pk=request.user.id)
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        newpasswordcon = request.POST.get("newpasswordcon")
        print(user.password)
        if oldpassword == user.password:

            if newpassword == newpasswordcon:
                user.password = newpassword
                user.save()
                return render(request, "odeon/password.html", {
                "message": "Password changed succesfully."
                })

            else:
                return render(request, "odeon/password.html", {
                "message": "Passwords don't match."
                })
        
        else:
            return render(request, "odeon/password.html", {
                "message": "Wrong password."
            })


    return render(request, "odeon/password.html")

@login_required
def publish(request):
    
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        subject_id = Subject.objects.get(subject=request.POST["subject"])
        role = request.POST.get("role")
        title = request.POST.get("title")
        body = request.POST.get("body")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if role == "tutor":
            price = request.POST.get("price")
        else:
            price = None
        
        announcement = Announcement(user=user, subject_id=subject_id, role=role, title=title, body=body, price=price, email=email, phone=phone)
        announcement.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "odeon/publish.html", {
        "subjects": Subject.objects.all()

    })

def delete(request):

    if request.method == "POST":
        announcement_id = request.POST.get("announcement_id")
    
    Announcement.objects.get(pk=announcement_id).delete()

    return HttpResponseRedirect(reverse("index"))

@login_required
def tutors(request):
    
    announcements = Announcement.objects.filter(role="tutor").annotate(
        is_bookmarked=Exists(Bookmark.objects.filter(announcement=OuterRef('pk'), user=request.user))
        ).order_by("-timestamp")

    return render(request, "odeon/tutors.html", {
        "announcements": announcements
    })

@login_required
def students(request):
    
    announcements = Announcement.objects.filter(role="student").annotate(
        is_bookmarked=Exists(Bookmark.objects.filter(announcement=OuterRef('pk'), user=request.user))
        ).order_by("-timestamp")
    
    return render(request, "odeon/students.html", {
        "announcements": announcements
    })

def bookmark(request):

    if request.method == "POST":

        data = json.loads(request.body)
        user = User.objects.get(pk=request.user.id)
        announcement = Announcement.objects.get(pk=data["announcement_id"])

        # If the post is not in user's Bookmarks create a row
        if not Bookmark.objects.filter(user=user, announcement=announcement):
            
            bookmark = Bookmark(user=user, announcement=announcement)
            bookmark.save()
        
        # If it's already there delete the row
        else:

            Bookmark.objects.get(user=user, announcement=announcement).delete()
   
    return JsonResponse({}, safe=False)
    

def unbookmark(request):

    if request.method == "POST":
        
        announcement_id = request.POST.get("announcement_id")

        Bookmark.objects.get(announcement=announcement_id).delete()

    return HttpResponseRedirect(reverse("bookmarks"))


def bookmarks(request):

    return render(request, "odeon/bookmarks.html", {
        "items" : Bookmark.objects.filter(user=request.user.id)
        })