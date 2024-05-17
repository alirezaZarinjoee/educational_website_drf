from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comment', views.CommentViewSet, basename='comment')


app_name='comment'
urlpatterns = [
    path('', include(router.urls)),
    path('add_comment/',views.CommentPost.as_view(),name='add_comment'),
]
