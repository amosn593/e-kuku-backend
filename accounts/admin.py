from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'user_name', 'date_joined',
                    'is_active', 'is_staff', 'is_superuser')


admin.site.register(UserAccount, UserAdmin)
