from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'writer', views.WriterViewSet, basename='writer')
router.register(r'blog', views.BlogViewSet, basename='blog')


app_name='blog'
urlpatterns = [
    path('', include(router.urls)),
    path('get_blog/',views.GetBlog.as_view(),name='get_glog'),
    path('detail_blog/<slug:slug>/',views.DetailBlog.as_view(),name='detail_blog'),

]
