# Generated by Django 3.2.5 on 2022-11-01 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20221101_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add_product',
        ),
        migrations.AddField(
            model_name='addproduct',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_products', to='shop.product'),
        ),
    ]
