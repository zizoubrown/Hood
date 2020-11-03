from django.contrib import admin
from .models import Profile, Neighborhood, Post, Business

admin.site.site_header = "Hood Admin"
admin.site.site_title = "Hood Admin Area"
admin.site.index_title = "Welcome to Hood admin"

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)
