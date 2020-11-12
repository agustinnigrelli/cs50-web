from django.contrib import admin
from .models import User, Followlist, Likelist, Posts, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Followlist)
admin.site.register(Likelist)
admin.site.register(Posts)
admin.site.register(Comments)