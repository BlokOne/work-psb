from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('delete/', views.order_delete, name='order_delete'),
    path('success/', views.order_success, name='order_success'),
]
