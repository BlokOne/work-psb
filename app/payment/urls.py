from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('success/', views.order_create, name='order_success'),
]
