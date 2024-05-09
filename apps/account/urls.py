from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='customer')



app_name='account'
urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.RegisterAPIView.as_view(),name='register'),
    path('verify/',views.VerifyAPIView.as_view(),name='verify_view'),
    path('login/',views.LoginApiView.as_view(),name='login'),
    path('logout/',views.LogoutApiView.as_view(),name='logout'),
    path('change_password/',views.ChangePasswordView.as_view(),name='change_password'),
]
