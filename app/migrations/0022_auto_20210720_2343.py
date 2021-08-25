# Generated by Django 3.2.4 on 2021-07-21 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_obra_restauracion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='restauracion',
        ),
        migrations.AddField(
            model_name='obra',
            name='restauracion',
            field=models.ForeignKey(blank=True, help_text='Restauraciones de obra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_obra_related', to='app.restauracion', verbose_name='Restauración'),
        ),
    ]
