from rest_framework import serializers
from .models import Comment

class CommentSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)#In your code, this field does not exist in the request data and instead you are trying to set it in the save method.
                                                             #To solve this problem, you can define the user field in your serializer as a read_only field. This makes DRF not expect this field to exist in the request data and you can set it in the save method.
    class Meta:
        model=Comment
        fields=['education','user','text','parent']
        