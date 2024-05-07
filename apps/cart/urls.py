from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    
    path('get_cart/',views.GetCart.as_view(),name='get_cart'),
    path('add_cart/<slug:slug>/',views.AddCart.as_view(),name='add_cart'),
]
