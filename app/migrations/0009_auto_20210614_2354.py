# Generated by Django 3.2.4 on 2021-06-15 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_obra_valuacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artista',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='especialidad',
            options={'ordering': ['nombre'], 'verbose_name': ('Especialidad',), 'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AlterModelOptions(
            name='obra',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='restauracion',
            options={'verbose_name': ('Restauración',), 'verbose_name_plural': 'Restauraciones'},
        ),
        migrations.AlterModelOptions(
            name='restaurador',
            options={'ordering': ['nombre'], 'verbose_name': 'Restaurador', 'verbose_name_plural': 'Restauradores'},
        ),
        migrations.AlterModelOptions(
            name='tiporestauracion',
            options={'ordering': ['nombre'], 'verbose_name': ('Tipo de restauración',), 'verbose_name_plural': 'Tipo de restauraciones'},
        ),
    ]
