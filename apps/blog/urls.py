from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'order', views.OrderViewSet, basename='order')


app_name='blog'
urlpatterns = [
    path('', include(router.urls)),

]
