from django.contrib import admin
from .models import *


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class SubcountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class PoultryAdmin(admin.ModelAdmin):
    list_display = ('id',  'title', 'category', 'county', 'subcounty', 'description', 'location', 'business_name',
                    'contact', 'price', 'date_posted', 'sponsored', 'approved')
    search_fields = ('title', 'county', 'subcounty',
                     'business_name', 'location', 'price')


admin.site.register(County, CountyAdmin)
admin.site.register(Subcounty, SubcountyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Poultry, PoultryAdmin)
