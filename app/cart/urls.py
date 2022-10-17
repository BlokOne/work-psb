from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.Cart_Detail.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.cart_add, name='cart_add'),
    path('remove/<int:pk>', views.cart_remove, name='cart_remove'),
    path('checkout', views.Checkout.as_view(), name='checkout')
]