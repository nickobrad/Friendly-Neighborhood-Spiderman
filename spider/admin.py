from django.contrib import admin
from .models import Business, Profile, Neighbourhood, Post

# Register your models here
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Post)
