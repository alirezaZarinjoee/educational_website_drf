from django.shortcuts import render
from .models import Writer,Blog
from .serializers import BlogSerializer,WriterSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions
from rest_framework.views import APIView
# Create your views here.

#----------for panel admin--------------------
class WriterViewSet(viewsets.ModelViewSet):
    queryset=Writer.objects.all()
    serializer_class=WriterSerializer
    # permission_classes=[permissions.IsAdminUser]
    
class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    # permission_classes=[permissions.IsAdminUser]
    

#-------------get bloge-----------------
class GetBlog(APIView):
    def get(self,request):
        blogs=Blog.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#--------------get detail blog----------
class DetailBlog(APIView):
    def get(self,request,*args,**kwargs):
        blog_id=kwargs['blog_id']
        try:
            blog=Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response(None,status=status.HTTP_400_BAD_REQUEST)
        
        serializer=BlogSerializer(blog)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        


