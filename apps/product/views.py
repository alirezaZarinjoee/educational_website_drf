from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Q,Count
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

#-------for panel admin--------

class EducationalGroupViewSet(viewsets.ModelViewSet):
    queryset = EducationalGroup.objects.all()
    serializer_class = EducationalGroupSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAdminUser]
    

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes=[permissions.IsAdminUser]
    

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes=[permissions.IsAdminUser]
    

class EducationFeatureViewSet(viewsets.ModelViewSet):
    queryset = EducationFeature.objects.all()
    serializer_class = EducationFeatureSerializer
    permission_classes=[permissions.IsAdminUser]
    
    
class EducationVideosViewSet(viewsets.ModelViewSet):
    queryset=EducationVideos.objects.all()
    serializer_class=EducationVideoSerializer
    permission_classes=[permissions.IsAdminUser]
    
#------------------------------cheapest educations-----------------------------------------------
class GetCheapestEducation(APIView):
    def get(self,request,*args,**kwargs):
        cheapest_education=Education.objects.filter(Q(is_active=True)).order_by('price')[:3]
        serializer=EducationSerializer(cheapest_education,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
#-------------------------------last educations----------------------------------------------
class GetLastEducation(APIView):
    def get(self,request):
        last_educations=Education.objects.filter(Q(is_active=True)).order_by('-published_date')[:3]
        serailizer=EducationSerializer(last_educations,many=True)
        return Response(data=serailizer.data,status=status.HTTP_200_OK)
#------------------------------popular group educations---------------------------------------
class GetPopularGroupEducation(APIView):
    def get(self,request):
        popular_group_educations=EducationalGroup.objects.filter(Q(is_active=True))\
                                        .annotate(count=Count('educations_of_group'))\
                                        .order_by('-count')[:3]
        serailizer=EducationalGroupSerializer(popular_group_educations,many=True)
        return Response(data=serailizer.data,status=status.HTTP_200_OK)
#------------------------------detail education and videos---------------------------------------------
class GetDetailEducation(APIView):
    def get(self, request, *args, **kwargs):
        education = get_object_or_404(Education, slug=kwargs['slug'])
        serializer = EducationSerializer(education, context={'request': request})
        if education.is_active:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
#------------------------------------------------------------------------------------------------------
