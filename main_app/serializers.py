from rest_framework import serializers
from .models import *


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


class SubcountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcounty
        fields = ('id', 'name', 'county', 'get_county')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PoultrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poultry
        fields = ('id', 'title', 'price', 'category', 'views', 'description', 'slug', 'date_posted', 'get_image',
                  'get_thumbnail', 'get_county', 'get_subcounty', 'location', 'contact', 'get_absolute_url')
