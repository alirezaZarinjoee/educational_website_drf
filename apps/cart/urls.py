from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'order_detail',views.OrderDetailViewSet, basename='order_detail')

app_name='cart'
urlpatterns = [
    path('', include(router.urls)),
    path('get_cart/',views.GetCart.as_view(),name='get_cart'),
    path('add_and_delete_cart/<slug:slug>/',views.AddAndDeleteCart.as_view(),name='add_cart'),
    path('total_price/',views.GetTotalPrice.as_view(),name='total_price'),
    path('create_order/',views.CreateOrder.as_view(),name='create_order'),
]
