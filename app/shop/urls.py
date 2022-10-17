from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('shop/', views.Shops.as_view(), name="shop"),
    path('support/', views.Support.as_view(), name='support')
]
