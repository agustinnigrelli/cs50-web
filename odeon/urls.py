from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("publish", views.publish, name="publish"),
    path("delete", views.delete, name="delete"),
    path("tutors", views.tutors, name="tutors"),
    path("students", views.students, name="students"),
    path("bookmark", views.bookmark, name="bookmark")
]