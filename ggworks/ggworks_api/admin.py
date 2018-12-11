from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
  fields = ['user', 'nick_name', 'company', 'photo_path', ]


admin.site.register(UserProfile, UserProfileAdmin)