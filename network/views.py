import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .models import User, Followlist, Likelist , Posts, Comments
from django.db.models import Exists, OuterRef


def index(request):

    if request.user.id:
        posts = Posts.objects.all().annotate(
            is_liked=Exists(Likelist.objects.filter(likes=OuterRef('pk'), user=request.user))
            ).order_by('-timestamp')
    else:
        posts = Posts.objects.all().order_by('-timestamp')

    # Paginate the posts un groups of 10
    page_number = request.GET.get('page')
    
    posts = Paginator(posts, 10)
    posts = posts.get_page(page_number)

    return render(request, "network/index.html", {
        "posts": posts
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

    if request.method == "PUT":

        data = json.loads(request.body)

        post = Posts.objects.get(pk=data["post_id"])
        
        post.body = data["editbody"]
        post.save()
    
        return JsonResponse({"message": "Post edited succesfully"}, safe=False)    


def profile(request, user_id):

    followers_count = Followlist.objects.filter(following=user_id).count()
    following_count = Followlist.objects.filter(user=user_id).count()
    
    if request.user.id:
        posts = Posts.objects.filter(user=user_id).annotate(
            is_liked=Exists(Likelist.objects.filter(likes=OuterRef('pk'), user=request.user))
            ).order_by('-timestamp')
        
    else:
        posts = Posts.objects.filter(user=user_id).order_by('-timestamp')

    # Paginate the posts un groups of 10
    page_number = request.GET.get('page')
    
    posts = Paginator(posts, 10)
    posts = posts.get_page(page_number)
    
    # By default assume the target is not being followed
    not_following = "False"
    
    if not Followlist.objects.filter(user=request.user.id, following=user_id):
        not_following = "True"

    return render(request, "network/profile.html", {
      "profile": User.objects.get(pk=user_id),
      "posts": posts,
      "followers": followers_count,
      "following": following_count,
      "not_following": not_following
    })


def follow(request): 

    user = User.objects.get(pk=request.user.id)
    follow = request.POST.get("follow")
    unfollow = request.POST.get("unfollow")

    if request.method == "POST":
        
        if follow:
    
            following = User.objects.get(pk=request.POST["target"])
            followlist =  Followlist(user=user, following=following)
            followlist.save()
        
        if unfollow: 

            Followlist.objects.get(user=user, following=request.POST["target"]).delete()

    return redirect("profile", user_id=request.POST["target"])


@login_required
def following(request):
    
    # Create a list of followed users by the current user
    followlist = Followlist.objects.filter(user=request.user)
    following = []
    for user in followlist:
        following.append(user.following)

    # Filter the post by the users present in the list
    posts = Posts.objects.filter(user__in=following).annotate(
        is_liked=Exists(Likelist.objects.filter(likes=OuterRef('pk'), user=request.user))
    ).order_by('-timestamp')

    # Paginate the posts un groups of 10
    page_number = request.GET.get('page')
    
    posts = Paginator(posts, 10)
    posts = posts.get_page(page_number)

    return render(request, "network/following.html", {
        "posts": posts
    }) 

def like(request):
    
    if request.method == "POST":

        data = json.loads(request.body)
        user = User.objects.get(pk=request.user.id)
        post = Posts.objects.get(pk=data["post_id"])

        # If the post is not in user's likelist. Create a row and add 1 to the count
        if not Likelist.objects.filter(user=user, likes=post):
            
            likelist = Likelist(user=user, likes=post)
            likelist.save()
            post.likecount += 1
            post.save()
        
        # If it's already there. Delete the row and substract 1 to the count
        else:

            Likelist.objects.get(user=user, likes=post).delete()
            post.likecount -= 1
            post.save()

    likes_count = Likelist.objects.filter(likes=data["post_id"]).count()
    return JsonResponse({"likes": likes_count}, safe=False)