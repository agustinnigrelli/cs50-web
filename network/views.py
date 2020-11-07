from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Followlist, Posts, Comments


def index(request):

    return render(request, "network/index.html", {
        "posts": Posts.objects.all().order_by('-timestamp')
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def post(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        body = request.POST.get("postbody")

        posts = Posts(user=user, body=body)
        posts.save()

    return redirect("index")

def edit(request):
    if request.method == "POST":
        post = Posts.objects.get(pk=request.POST["post_id"])
        edited_body = request.POST.get("editbody")

        post.body = edited_body
        post.save()
    
    return redirect("index")

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Posts.objects.filter(pk=user_id)
    followlist = Followlist.objects.get(pk=request.user.id)
    
    if not user_id in followlist.following:
        not_following = True

    return render(request, "network/profile.html", {
      "user": user,
      "posts": posts,
      "not_following": not_following
    })
