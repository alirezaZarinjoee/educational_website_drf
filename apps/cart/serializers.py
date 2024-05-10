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
    #If the field is directly in our model, we do not use the option (many=true).
    #But if we use related_name in another class and want to use that related_name as a nested serializer, we must change the many option to true.
    #Also, if we want only the front-end user to see the data and not change it, we must set the read_only option to true.
    class Meta:
        model=OrderDetail
        fields='__all__'

    def to_representation(self, instance):
        self.fields['education'] = EducationSerializer(read_only=True)
        return super(OrderDetailSerializer, self).to_representation(instance)
    
    
class OrderDetailGetSerializer(serializers.ModelSerializer):
    education=EducationSerializer(read_only=True)
    class Meta:
        model=OrderDetail
        fields='__all__'
        