# Generated by Django 5.0.2 on 2024-02-18 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.brands', verbose_name='Brandni tanlang'),
            preserve_default=False,
        ),
    ]
