from django.contrib import admin
from django.contrib.admin.helpers import AdminForm

from shop.models import Product

@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'configurations', 'price', 'total')
    search_fields = ['title']
    list_filter = ['price', 'total']