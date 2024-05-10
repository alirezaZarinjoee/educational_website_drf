from django.shortcuts import render
from .models import Coupon,DiscountBasket,DiscountBasketDetails
from .serializers import CouponSerializer,DiscountBasketSerializer,DiscountBasketDetailsSerializer
from rest_framework import viewsets,permissions


#--------------for panel admin----------------
class CouponViewSet(viewsets.ModelViewSet):
    queryset=Coupon.objects.all()
    serializer_class=CouponSerializer
    # permission_classes=[permissions.IsAdminUser]
    
class DiscountBasketViewSet(viewsets.ModelViewSet):
    queryset=DiscountBasket.objects.all()
    serializer_class=DiscountBasketSerializer
    # permission_classes=[permissions.IsAdminUser]
    
class DiscountBasketDetailsViewSet(viewsets.ModelViewSet):
    queryset=DiscountBasketDetails.objects.all()
    serializer_class=DiscountBasketDetailsSerializer
    # permission_classes=[permissions.IsAdminUser]
