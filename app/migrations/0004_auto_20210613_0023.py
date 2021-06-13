# Generated by Django 3.2.4 on 2021-06-13 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_restauracion_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(help_text='Apellido del artista', max_length=200, verbose_name='Apellido')),
                ('nombre', models.CharField(help_text='Nombre del artista', max_length=200, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='obra',
            name='artista',
            field=models.ForeignKey(blank=True, help_text='Artista creador de la', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_obra_related', to='app.artista', verbose_name='Artista'),
        ),
    ]
