from django.contrib import admin

# Register your models here.
from vpn.models import UserProfile

#class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ['user_id', 'username', 'email', 'password', 'sex', 'joined_date', 'last_login', 'user_level', 'status']

admin.site.register(UserProfile)
