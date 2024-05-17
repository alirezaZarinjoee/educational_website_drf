from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


app_name='cart'
urlpatterns = [
    path('', include(router.urls)),

]
