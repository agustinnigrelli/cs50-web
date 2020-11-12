from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Followlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='followed')

    def __str__(self):
        return f"{self.user} is following: {self.following}"

class Likelist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='liker')
    likes = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user} likes {self.likes}"

class Posts(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    body = models.TextField(blank=False, max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} posted {self.body} at {self.timestamp}"

    def serialize(self):
        return {
            "user": self.user,
            "body": self.body,
            "timestamp": self.timestamp
        }

class Comments(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented {self.body} on {self.post} at {self.timestamp}"

