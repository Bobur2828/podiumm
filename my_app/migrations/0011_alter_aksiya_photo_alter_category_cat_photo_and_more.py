# Generated by Django 5.0.2 on 2024-02-18 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aksiya',
            name='photo',
            field=models.ImageField(upload_to='aksiya/photo', verbose_name='Aksiya uchun foto kiriting 370x240 olchamda'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='category/photo', verbose_name='Categoriya uchun foto 370x240 olchamda'),
        ),
        migrations.AlterField(
            model_name='product',
            name='articul',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.category', verbose_name='Kategoriyani tanlang'),
        ),
        migrations.AlterField(
            model_name='product',
            name='max_content',
            field=models.TextField(max_length=1500, verbose_name='Mahsulotga batafsil tarif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_content',
            field=models.TextField(max_length=300, verbose_name='Mahsulotga qisqacha tarif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo1',
            field=models.ImageField(upload_to='product/photo', verbose_name='slide uchun foto kiriting 370x240 olchamda'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/photo', verbose_name='Tovar fotosini kiriting'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/photo', verbose_name='Tovar fotosini kiriting'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/photo', verbose_name='Tovar fotosini kiriting'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo5',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/photo', verbose_name='Tovar fotosini kiriting'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=10, verbose_name='Narxni belgilang'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='my_app.size', verbose_name="O'lchamni tanlang"),
        ),
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(upload_to='slider/photo', verbose_name='Slide uchun foto kiriting 1920x753 olchamda'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='photo1',
            field=models.ImageField(upload_to='slider/photo', verbose_name='Kichik banner uchun foto kiriting 1170x250 olchamda'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title1',
            field=models.CharField(max_length=100, verbose_name='Ikkinchi qatorni kiriting'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title2',
            field=models.CharField(max_length=100, verbose_name='Uchinchi qatorni kiriting'),
        ),
    ]