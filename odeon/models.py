from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    image = models.URLField(null=True)

    def __str__(self):
        return f"{self.subject}"

class Announcement(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, related_name="subject_id", on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    body =  models.CharField(max_length=300)
    price = models.FloatField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    activity = models.CharField(max_length=10, default="Open")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user} published '{self.title}' in '{self.subject_id}' category at {self.timestamp}"

class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name="watcher", on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, related_name="announcement", on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user} bookmarked {self.announcement}"
