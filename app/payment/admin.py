from django.contrib import admin
from .models import Order, OrderItem, OrderAddItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAddItemInline(admin.TabularInline):
    model = OrderAddItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline, OrderAddItemInline]


admin.site.register(Order, OrderAdmin)