# Generated by Django 3.2.4 on 2021-06-15 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210615_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='valuacion',
        ),
    ]