from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("register/", views.Register, name="register"),
    path('shop/', views.Shops.as_view(), name="shop"),
    path('shop/<int:pk>', views.ShopDetail.as_view(), name='detail'),
    path('support/', views.Support.as_view(), name='support')
]
