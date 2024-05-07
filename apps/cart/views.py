from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from .serializers import CartItemSerializer
from apps.account.models import CustomUser
from .models import CartItem
from apps.product.models import Education

#----------------------------------------------------------------------------------------------
class GetCart(APIView):
    def get(self,request):
        try:
            cart_items = CartItem.objects.filter(user=request.user)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart items not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(cart_items, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#-----------------------------------------------------------------------------------------------
class AddCart(APIView):
    def post(self,request,*args,**kwargs):
            item = get_object_or_404(Education, slug=kwargs['slug'])

            # Find an existing cart item for the user and the specified item
            cart_item, _ = CartItem.objects.get_or_create(user=request.user, education=item)

            if item.is_active!=True:
                return Response({'error': 'This education does not exist at the moment'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the cart item
            cart_item.save()
            serializer = CartItemSerializer(cart_item,context={'request': request})
            return Response({'message': 'Given item quantity increased in cart', 'data': serializer.data}, status=status.HTTP_200_OK)
#-----------------------------------------------------------------------------------------------

        
        
