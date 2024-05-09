from rest_framework import serializers
from .models import CartItem,Order,OrderDetail
from apps.product.serializers import EducationSerializer

class CartItemSerializer(serializers.ModelSerializer):
    education=EducationSerializer()
    class Meta:
        model=CartItem
        fields='__all__'
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields='__all__'