from rest_framework import serializers
from .models import CartItem
from apps.product.serializers import EducationSerializer

class CartItemSerializer(serializers.ModelSerializer):
    education=EducationSerializer()
    class Meta:
        model=CartItem
        fields='__all__'