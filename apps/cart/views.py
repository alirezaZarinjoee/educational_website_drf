from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from .serializers import CartItemSerializer
from apps.account.models import CustomUser
from .models import CartItem

#----------------------------------------------------------------------------------------------
class GetItemOfCart(APIView):
    def get(self,request):
        try:
            cart_items = CartItem.objects.filter(user=request.user)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart items not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
#-----------------------------------------------------------------------------------------------
        
