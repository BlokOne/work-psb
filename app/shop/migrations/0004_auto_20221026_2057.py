# Generated by Django 3.2.5 on 2022-10-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20221026_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страны', 'verbose_name_plural': 'Страна'},
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='shop.country', verbose_name='Страна'),
        ),
    ]
