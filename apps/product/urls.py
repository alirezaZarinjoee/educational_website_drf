from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'filter_viewset', FilterViewset)
# router.register(r'educational_groups', EducationalGroupViewSet)
# router.register(r'teacher',TeacherViewSet)
# router.register(r'feature', FeatureViewSet)
# router.register(r'education', EducationViewSet)
# router.register(r'education_feature', EducationFeatureViewSet)
# router.register(r'Education_videos', EducationVideosViewSet)
# router.register(r'feature_value', FeatureValueViewSet)

router = DefaultRouter()
router.register(r'filter_viewset', FilterViewset, basename='filter_viewset')
router.register(r'educational_groups', EducationalGroupViewSet, basename='educational_groups')
router.register(r'teacher',TeacherViewSet, basename='teacher')
router.register(r'feature', FeatureViewSet, basename='feature')
router.register(r'education', EducationViewSet, basename='education')
router.register(r'education_feature', EducationFeatureViewSet, basename='education_feature')
router.register(r'Education_videos', EducationVideosViewSet, basename='Education_videos')
router.register(r'feature_value', FeatureValueViewSet, basename='feature_value')



app_name='product'
urlpatterns = [
    path('', include(router.urls)),
    path('cheapest_education/',GetCheapestEducation.as_view(),name='cheapest_education'),
    path('last_education/',GetLastEducation.as_view(),name='last_education'),
    path('popular_group_educations/',GetPopularGroupEducation.as_view(),name='popular_group_educations'),
    path('detail_education/<slug:slug>/',GetDetailEducation.as_view(),name='detail_education'),
    path('related_education/<slug:slug>/',GetRelatedEducation.as_view(),name='related_education'),
    path('list_of_group_education/',GetListOfEducationGroup.as_view(),name='list_of_group_education'),
    path('education_of_groups/<slug:slug>/',GetEducationOfGroups.as_view(),name='education_of_groups'),
    path('filter_by_group/',FilterByGroup.as_view(),name='filter_by_group'),
]
