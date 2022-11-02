# Generated by Django 3.2.5 on 2022-11-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_addproduct'),
        ('payment', '0005_auto_20221025_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='В ведите текст который получит пользователь при покупки')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_items', to='payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_add_items', to='shop.addproduct')),
            ],
        ),
    ]
