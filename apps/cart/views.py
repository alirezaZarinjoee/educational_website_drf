from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer,OrderSerializer,OrderDetailSerializer
from apps.account.models import CustomUser,Customer
from .models import CartItem,Order,OrderDetail
from apps.product.models import Education
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import viewsets,permissions

#---------------for panel admin--------------------------
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes=[permissions.IsAdminUser]


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset=OrderDetail.objects.all()
    serializer_class=OrderDetailSerializer
    # permission_classes=[permissions.IsAdminUser]


#-------------------------------get all item in cart---------------------------------------------------------------
class GetCart(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        try:
            cart_items = CartItem.objects.filter(user=request.user)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart items not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(cart_items, many=True,context={'request': request})#Because we used absolute URLs for educations, wherever educations have even the smallest role, we must send the request in the context in the serializer.
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#--------------------------add and delete in cart---------------------------------------------------------------------
class AddAndDeleteCart(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
            item = get_object_or_404(Education, slug=kwargs['slug'])

            # Find an existing cart item for the user and the specified item
            cart_item, _ = CartItem.objects.get_or_create(user=request.user, education=item)

            if item.is_active!=True:
                return Response({'error': 'This education does not exist at the moment'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the cart item
            cart_item.save()
            serializer = CartItemSerializer(cart_item,context={'request': request})#Because we used absolute URLs for educations, wherever educations have even the smallest role, we must send the request in the context in the serializer.
            return Response({'message': 'Given item quantity increased in cart', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self,request,*args,**kwargs):
        item = get_object_or_404(Education, slug=kwargs['slug'])
        
        try:
            cart_item = CartItem.objects.get(user=request.user,education=item)
        except CartItem.DoesNotExist:
            return Response({'message': 'There is no such item'}, status=status.HTTP_404_NOT_FOUND)
            
        cart_item.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_200_OK)
        
#----------------Get the price of all items in the shopping cart in Rials---------------------------
class GetTotalPrice(APIView):
    def get(self,request,*args,**kwargs):
        #Getting the list of items in the cart for the current user
        educations_of_user_in_cart=CartItem.objects.filter(Q(user=request.user))
        
        if educations_of_user_in_cart:
            tax=0.05
            sum=0
            for price in educations_of_user_in_cart:
                sum+=price.education.price
            total_price=((sum*tax)+sum)*10 #The price is in Rials
            
            return Response({'message':'The price is in Rials','total_price': total_price}, status=status.HTTP_200_OK)
        return Response({'message':'There is no item in the shopping cart'},status=status.HTTP_404_NOT_FOUND)
#-----------------Continue the process of purchasing and creating an order--------------------------
class CreateOrder(APIView):
    def post(self,request,*args,**kwargs):
        
        user=request.user
        customer, created = Customer.objects.get_or_create(user=user)
        
        order=Order.objects.create(customer=customer)
        
        list_of_item_in_cart=CartItem.objects.filter(Q(user=user))
        if list_of_item_in_cart:
            for item in list_of_item_in_cart:
                OrderDetail.objects.create(
                    order=order,
                    education=item.education,
                    price=item.education.price)
            
            return Response({
                        'message':'Your educations are displayed as an invoice for final payment','redirect': '/cart/final/'},
                        headers={'Location': '/cart/final/'},
                        status=status.HTTP_200_OK)

        else:
            return Response({'message':'There are no items in your shopping cart'},status=status.HTTP_400_BAD_REQUEST)
              
