from django.contrib import admin
from .models import Image, Profile, Comment

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal =('likes',)

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
