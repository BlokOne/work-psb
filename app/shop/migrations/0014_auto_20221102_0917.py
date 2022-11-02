# Generated by Django 3.2.5 on 2022-11-02 06:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20221102_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
