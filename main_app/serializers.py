from rest_framework import serializers
from .models import *


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


class SubcountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcounty
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PoultrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poultry
        fields = "__all__"
