from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("entry/", views.entry, name="entry"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("random_page/", views.random_page, name="random_page"),
]
