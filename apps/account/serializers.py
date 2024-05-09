from rest_framework import serializers
from .models import CustomUser,Customer
from rest_framework.exceptions import ValidationError


class CustomUserSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(write_only=True)
    #note: write_only for hide password in postman
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'repassword']
        extra_kwargs = {'password': {'write_only': True}}
        #note: extra_kwargs for add options to fields
        

    def validate(self, data):
        if data['password'] != data['repassword']:
            raise ValidationError("Password and repassword are not the same")
        return data

    def create(self, validated_data):
        del validated_data['repassword']
        return CustomUser.objects.creat_user(**validated_data)
        
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'