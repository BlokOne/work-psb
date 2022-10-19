from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart/', include("cart.urls", namespace='cart')),
    path('payments/', include('payment.urls', namespace='payment')),
    path('', include("shop.urls", namespace='shop'))
]
