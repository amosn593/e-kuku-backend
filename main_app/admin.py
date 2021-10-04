from django.contrib import admin
from .models import *


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class SubcountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class PoultryAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'title', 'category', 'county', 'subcounty', 'description', 'location', 'business_name',
                    'contact', 'price', 'date_posted', 'approved')


admin.site.register(County, CountyAdmin)
admin.site.register(Subcounty, SubcountyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Poultry, PoultryAdmin)
