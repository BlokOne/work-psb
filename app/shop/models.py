from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Наименование товара', max_length=100)
    configurations = models.TextField(verbose_name='Описание конфигурации')
    price = models.IntegerField(verbose_name='Цена')
    total = models.IntegerField(verbose_name='Старая цена', blank=True)
    count = models.BooleanField(verbose_name='В наличии')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.title