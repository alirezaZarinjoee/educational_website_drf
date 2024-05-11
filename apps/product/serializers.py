from rest_framework import serializers
from .models import *
from django.urls import reverse



class EducationalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalGroup
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class FeatureSerializer(serializers.ModelSerializer):
    educational_group=EducationalGroupSerializer(read_only=True)
    class Meta:
        model = Feature
        fields = '__all__'



class EducationVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationVideos
        fields = '__all__'


#We have done this in this serializer to get the details of a product instead of using the get_absolute_url function in the model file. We have also sent a text for the serializer in the view, which you can see
class EducationSerializer(serializers.ModelSerializer):
    videos = EducationVideoSerializer(many=True, read_only=True)
    price_with_discount = serializers.SerializerMethodField()
    price_of_education_by_tax = serializers.SerializerMethodField() 

    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['absolute_url', 'videos', 'price_with_discount', 'price_of_education_by_tax']  # Add the new field here
    absolute_url = serializers.SerializerMethodField()
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('product:detail_education', args=[obj.slug]))

    def get_price_with_discount(self, obj):
        return obj.get_price_by_discount()

    def get_price_of_education_by_tax(self, obj):  
        return obj.price_of_education_by_tax()

    def to_representation(self, instance):
        self.fields['teacher'] = TeacherSerializer(read_only=True)
        self.fields['group'] = EducationalGroupSerializer(read_only=True,many=True)
        self.fields['feature'] = FeatureSerializer(read_only=True,many=True)
        return super(EducationSerializer, self).to_representation(instance)



class EducationFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationFeature
        fields = '__all__'

class FeatureValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureValue
        fields = '__all__'

class EducationFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=EducationFeature
        fields="__all__"
#------------------------

class TeacherSerializerNameFamily(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'family')
        
class FeatureValueSerializer(serializers.ModelSerializer):
    feature_values = EducationFeatureSerializer(many=True, read_only=True)#nested serializers
    
    class Meta:    
        model=FeatureValue
        fields="__all__"
