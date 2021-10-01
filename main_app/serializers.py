from rest_framework import serializers
from .models import Category, County, Subcounty, Poultry


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
        fields = ('id', 'title', 'price', 'category', 'views', 'description', 'slug', 'date_posted', 'image',
                  'get_image', 'get_county', 'get_subcounty', 'location', 'business_name', 'contact', 'get_absolute_url')


class PoultryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poultry
        fields = ('title', 'price', 'category', 'description',
                  'image', 'county', 'subcounty', 'location', 'business_name', 'contact')
