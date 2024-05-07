from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('list_product_in_cart/',views.GetItemOfCart.as_view(),name='list_product_in_cart'),
]
