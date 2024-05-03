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
    class Meta:
        model = Feature
        fields = '__all__'



class EducationVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationVideos
        fields = '__all__'


#We have done this in this serializer to get the details of a product instead of using the get_absolute_url function in the model file. We have also sent a text for the serializer in the view, which you can see
class EducationSerializer(serializers.ModelSerializer):
    videos = EducationVideoSerializer(many=True, read_only=True)#nested serializers
    
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['absolute_url', 'videos']
    absolute_url = serializers.SerializerMethodField()
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('product:detail_education', args=[obj.slug]))


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
