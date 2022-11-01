from django.contrib import admin
from django.contrib.admin.helpers import AdminForm

from shop.models import *


class AddProductInline(admin.TabularInline):
    model = AddItem
    raw_id_fields = ['product']


@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'configurations', 'price', 'total', 'country')
    search_fields = ['title']
    list_filter = ['price', 'total']
    inlines = [AddProductInline]


@admin.register(AddProduct)
class AddShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'configurations', 'price', 'total')
    search_fields = ['title']
    list_filter = ['price', 'total']
    

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']