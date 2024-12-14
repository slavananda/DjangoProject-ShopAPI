from rest_framework.generics import ListAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.prefetch_related('subcategories')
    serializer_class = CategorySerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.select_related('subcategory__parent_category')
    serializer_class = ProductSerializer
from django.shortcuts import render

# Create your views here.
