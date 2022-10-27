from django.contrib import admin
from django.contrib.admin.helpers import AdminForm

from shop.models import Product, Country

@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'configurations', 'price', 'total', 'country')
    search_fields = ['title']
    list_filter = ['price', 'total']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']