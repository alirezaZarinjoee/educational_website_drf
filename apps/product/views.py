from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Q,Count,Min,Max
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from . filters import EducationFilter
from apps.comment.serializers import CommentSerializerAdmin


def media_admin(request):
    return {'media_url':settings.MEDIA_URL}



#=======================for panel admin======================

class EducationalGroupViewSet(viewsets.ModelViewSet):
    queryset = EducationalGroup.objects.all()
    serializer_class = EducationalGroupSerializer
    # permission_classes = [permissions.IsAdminUser]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAdminUser]
    

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    # permission_classes=[permissions.IsAdminUser]
    

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes=[permissions.IsAdminUser]
    

class EducationFeatureViewSet(viewsets.ModelViewSet):
    queryset = EducationFeature.objects.all()
    serializer_class = EducationFeatureSerializer
    # permission_classes=[permissions.IsAdminUser]
    
    
class EducationVideosViewSet(viewsets.ModelViewSet):
    queryset=EducationVideos.objects.all()
    serializer_class=EducationVideoSerializer
    # permission_classes=[permissions.IsAdminUser]
    
    
class FeatureValueViewSet(viewsets.ModelViewSet):
    queryset=FeatureValue.objects.all()
    serializer_class=FeatureValueSerializer
    # permission_classes=[permissions.IsAdminUser]
    

#=======================for educations=============================

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
#------------------------------detail education---------------------------------------------

class GetDetailEducation(APIView):
    def get(self, request, *args, **kwargs):
        education = get_object_or_404(Education, slug=kwargs['slug'])
        serializer = EducationSerializer(education, context={'request': request})
        if education.is_active:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
#------------------------------detail education and videos---------------------------------------------
class GetVideosEducation(APIView):
    def get(self, request, *args, **kwargs):
        education = get_object_or_404(Education, slug=kwargs['slug'])
        if education.is_active and education.purchased_by_user(request.user):
            serializer = EducationSerializer(education, context={'request': request})
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

#--------------------------------related education------------------------------------------------------
class GetRelatedEducation(APIView):
    def get(self,request,*args,**kwargs):
        education = get_object_or_404(Education, slug=kwargs['slug'])
        related_list=[]
        for group in education.group.all():
            related_list.extend(Education.objects.filter(Q(is_active=True) & Q(group=group) & ~Q(id=education.id)))
        seralizer=EducationSerializer(related_list,many=True,context={'request': request})
        return Response(data=seralizer.data,status=status.HTTP_200_OK)
#---------------------------------list educationa group--------------------------------------------------
class GetListOfEducationGroup(APIView):
    def get(self,request,*args,**kwargs):
        groups=EducationalGroup.objects.filter(Q(is_active=True))\
                    .annotate(count=Count('educations_of_group'))\
                    .order_by('-count')
        serializer=EducationalGroupSerializer(groups,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
#----------------------------------educations of groups-----------------------------------------------------
class GetEducationOfGroups(APIView):
    def get(self,request,*args,**kwargs):
        group=get_object_or_404(EducationalGroup,slug=kwargs['slug'])
        list_of_educations_group=Education.objects.filter(Q(is_active=True) & Q(group=group))\
                                                                .order_by('-published_date')
        serializer=EducationSerializer(list_of_educations_group,many=True,context={'request': request})
        return Response(data=serializer.data,status=status.HTTP_200_OK)
#--------------------show comments of education-------------------------------
class GetCommentsOfEducation(APIView):
    def get(self,request,*args,**kwargs):
        education_id=kwargs['education_id']
        try:
            education=Education.objects.get(id=education_id)
        except Education.DoesNotExist:
            return Response({'message':'DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)
        
        comments = education.comments.filter(Q(is_active=True))
        serializer = CommentSerializerAdmin(comments, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)


            
         

#=======================for filtering==============================

#--------------------------list group for filtering by group---------------------------------
class FilterByGroup(APIView):
    def get(self,request,*args,**kwargs):
        education_groups=EducationalGroup.objects.annotate(count=Count('educations_of_group'))\
                                                        .filter(Q(is_active=True) & ~Q(count=0))\
                                                        .order_by('-count')
        serializer=EducationalGroupSerializer(education_groups,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
#--------------------------get min and max price of educations---------------------------------
class GetMinAndMaxPrice(APIView):
    def get(self,request,*args,**kwargs):
        educations=Education.objects.filter(Q(is_active=True))
        min_max_price=educations.aggregate(min_price=Min('price'),max_price=Max('price'))
        return Response(min_max_price)
#---------------------------get list teacher---------------------------------------------------
class GetTeachers(APIView):
    def get(self,request):
        teachers=Teacher.objects.filter(Q(is_active=True)).order_by('name','family')
        seirlizer=TeacherSerializerNameFamily(teachers,many=True)
        return Response(data=seirlizer.data,status=status.HTTP_200_OK)
#--------------------------get feature names---------------------------------------------------
class GetFeatureValue(APIView):
    def get(self,request):
        feature_value=FeatureValue.objects.all()
        serializer=FeatureValueSerializer(feature_value,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
#--------------------------------------------------------------------
class FilterViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EducationFilter




