from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'coupon', views.CouponViewSet, basename='coupon')
router.register(r'discount_basket',views.DiscountBasketViewSet, basename='discount_basket')
router.register(r'discount_basket_details',views.DiscountBasketDetailsViewSet, basename='discount_basket_details')

app_name='discount'
urlpatterns = [
    path('', include(router.urls)),

]
