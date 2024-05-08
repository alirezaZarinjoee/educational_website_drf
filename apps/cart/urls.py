from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    
    path('get_cart/',views.GetCart.as_view(),name='get_cart'),
    path('add_and_delete_cart/<slug:slug>/',views.AddAndDeleteCart.as_view(),name='add_cart'),
    path('total_price/',views.GetTotalPrice.as_view(),name='total_price'),
]
