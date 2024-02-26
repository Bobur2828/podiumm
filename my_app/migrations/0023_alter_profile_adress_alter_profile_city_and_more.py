# Generated by Django 5.0.2 on 2024-02-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0022_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, choices=[('TAS', 'Toshkent shahri'), ('AND', 'Andijon viloyati'), ('NAM', 'Namangan viloyati'), ('SAM', 'Samarqand viloyati'), ('FAR', "Farg'ona viloyati"), ('SUR', 'Surxondaryo viloyati'), ('JIZ', 'Jizzax viloyati'), ('KAS', 'Qashqadaryo viloyati'), ('NAV', 'Navoiy viloyati'), ('XOR', 'Xorazm viloyati'), ('KAR', 'Karakalpakistan Respublikasi'), ('SIR', 'Sirdaryo viloyati'), ('BUK', 'Buxoro viloyati')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('UZ', "O'zbekiston"), ('KG', "Qirg'iziston"), ('KZ', "Qozog'iston"), ('TJ', 'Tojikiston'), ('TM', 'Turkmaniston'), ('AF', "Afg'oniston")], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
