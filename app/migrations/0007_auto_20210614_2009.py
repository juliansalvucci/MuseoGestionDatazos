# Generated by Django 3.2.4 on 2021-06-14 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_restaurador_domicilio'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurador',
            name='calle',
            field=models.CharField(max_length=200, null=True, verbose_name='Calle'),
        ),
        migrations.AddField(
            model_name='restaurador',
            name='numero',
            field=models.IntegerField(null=True, verbose_name='Numero'),
        ),
    ]
