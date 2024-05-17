from rest_framework import serializers
from .models import Writer,Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'
        
class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Writer
        fields='__all__'
        