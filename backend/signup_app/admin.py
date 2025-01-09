from django.contrib import admin

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # שדות להצגה ברשימה


# Register your models here.
