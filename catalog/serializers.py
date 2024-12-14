from rest_framework import serializers
from .models import Category, Subcategory, Product

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'image', 'parent_category']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'subcategories']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='subcategory.parent_category')
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'thumbnail', 'category', 'subcategory', 'price']
