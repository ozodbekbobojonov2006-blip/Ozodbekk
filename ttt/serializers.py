from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    aloo=serializers.SerializerMethodField()
    def get_aloo(self, obj):
        return (tag.name for tag in obj.tags.all())

    class Meta:
        model = Product
        fields =['id','name','price','description', 'category', 'aloo']


class ProductPostSerilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'all'
