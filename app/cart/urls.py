from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('bug/', views.Cart_Detail.as_view(), name='cart_detail'),
    path('add/<str:id>/<str:optional>', views.cart_add, name='cart_add'),
    path('remove/<str:id>/<str:optional>', views.cart_remove, name='cart_remove'),
    path('checkout', views.Checkout.as_view(), name='checkout')
]