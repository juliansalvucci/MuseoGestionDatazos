# Generated by Django 3.2.4 on 2021-06-12 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restauracion',
            name='precio',
            field=models.DecimalField(decimal_places=2, help_text='precio de la reparación', max_digits=10, verbose_name='Precio de la reparación'),
        ),
    ]
