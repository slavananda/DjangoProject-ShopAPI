from rest_framework import serializers
from catalog.serializers import ProductSerializer
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']

    def get_items(self, obj):
        items = CartItem.objects.filter(cart=obj)
        return CartItemSerializer(items, many=True).data

    def get_total_price(self, obj):
        items = CartItem.objects.filter(cart=obj)
        return sum(item.product.price * item.quantity for item in items)
