from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer,CommentSerializerAdmin
from rest_framework import permissions,status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


#------------------for panel admin---------------------

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializerAdmin
    # permission_classes=[permissions.IsAdminUser]


#--------------post comment in DB----------------------

# class CommentPost(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer=CommentSerializer(data=request.data)
#         user=request.user
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class CommentPost(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Pass the current user to the save method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
