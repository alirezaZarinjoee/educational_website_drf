from rest_framework import serializers
from .models import Coupon,DiscountBasket,DiscountBasketDetails
from apps.product.serializers import EducationSerializer


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'


class DiscountBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiscountBasket
        fields='__all__'
        


class DiscountBasketDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountBasketDetails
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['discount_basket'] = DiscountBasketSerializer(read_only=True)
        self.fields['education'] = EducationSerializer(read_only=True)
        return super(DiscountBasketDetailsSerializer, self).to_representation(instance)



# class DiscountBasketDetailsSerializer(serializers.ModelSerializer):
#     discount_basket = serializers.PrimaryKeyRelatedField(queryset=DiscountBasket.objects.all())
    
#     class Meta:
#         model = DiscountBasketDetails
#         fields = ['discount_basket', 'education']
        
#     def create(self, validated_data):
#         discount_basket = validated_data.pop('discount_basket')
#         discount_basket_details = DiscountBasketDetails.objects.create(discount_basket=discount_basket, **validated_data)
#         return discount_basket_details
