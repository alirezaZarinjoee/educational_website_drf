from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'educational_groups', EducationalGroupViewSet)
router.register(r'teacher',TeacherViewSet)
router.register(r'feature', FeatureViewSet)
router.register(r'education', EducationViewSet)
router.register(r'education_feature', EducationFeatureViewSet)
router.register(r'Education_videos', EducationVideosViewSet)

app_name='product'
urlpatterns = [
    path('', include(router.urls)),
    path('cheapest_education/',GetCheapestEducation.as_view(),name='cheapest_education'),
    path('last_education/',GetLastEducation.as_view(),name='last_education'),
    path('popular_group_educations/',GetPopularGroupEducation.as_view(),name='popular_group_educations'),
    path('detail_education/<slug:slug>/',GetDetailEducation.as_view(),name='detail_education'),
    path('related_education/<slug:slug>/',GetRelatedEducation.as_view(),name='related_education'),
]
