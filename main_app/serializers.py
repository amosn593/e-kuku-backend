from rest_framework import serializers
from .models import *


class CountySerializer(serializers.Serializer):
    class Meta:
        model: County
        Fields: '__all__'
        
class SubcountySerializer(serializers.Serializer):
    class Meta:
        model: Subcounty
        Fields: '__all__'
        
class CategorySerializer(serializers.Serializer):
    class Meta:
        model: Category
        Fields: '__all__'
        
class PoultrySerializer(serializers.Serializer):
    class Meta:
        model: Poultry
        Fields: '__all__'
