from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.page, name="page"),
    path("entry/", views.entry, name="entry"),
    path("edit/", views.edit, name="edit"),
    path("random_page/", views.random_page, name="random_page"),
]
