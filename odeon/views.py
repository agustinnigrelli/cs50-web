from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime

from .models import User, Subject, Announcement, Bookmark

@login_required
def index(request):
    
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

    return render(request, "odeon/publish.html", {
        "subjects": Subject.objects.all()

    })