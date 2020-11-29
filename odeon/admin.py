from django.contrib import admin
from .models import User, Subject, Announcement, Bookmark

# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Announcement)
admin.site.register(Bookmark)