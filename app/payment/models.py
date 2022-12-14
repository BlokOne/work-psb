import uuid

from django.db import models

from shop.models import Product, AddProduct


class Order(models.Model):
    email = models.EmailField()
    invoice_id = models.CharField(verbose_name='Номер заказа', unique=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ #{}'.format(self.invoice_id)

    def get_total_cost(self):
        sum_product = sum(item.get_cost() for item in self.items.all())
        sum_add_product = sum(item.get_cost() for item in self.add_items.all())
        return sum_add_product + sum_product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    text = models.TextField(verbose_name='В ведите текст который получит пользователь при покупки', default="", null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.order)

    def get_cost(self):
        return self.price * self.quantity


class OrderAddItem(models.Model):
    order = models.ForeignKey(Order, related_name='add_items', on_delete=models.CASCADE)
    product = models.ForeignKey(AddProduct, related_name='order_add_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    text = models.TextField(verbose_name='В ведите текст который получит пользователь при покупки', default="", null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.order)

    def get_cost(self):
        return self.price * self.quantity
