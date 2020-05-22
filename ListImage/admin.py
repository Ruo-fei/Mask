from django.contrib import admin
from .models import Post, PostMask

# Register your models here.
admin.site.register(Post)
admin.site.register(PostMask)