# Generated by Django 3.2.4 on 2021-06-12 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Descripción de la obra', verbose_name='descripción')),
                ('nombre', models.CharField(help_text='Nombre de la obra', max_length=200, verbose_name='Nombre de Obra')),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Descripción de la obra', verbose_name='descripción')),
                ('nombre', models.CharField(help_text='Nombre del estilo aplicado', max_length=200, verbose_name='Nombre del estilo')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Descripción de la obra', verbose_name='descripción')),
                ('nombre', models.CharField(help_text='Nombre de la obra', max_length=200, verbose_name='Nombre de Obra')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRestauracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Descripción', verbose_name='Descripción del tipo de restauracion')),
                ('nombre', models.CharField(help_text='nombre tipo', max_length=200, verbose_name='Nombre de tipo de restauración')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(help_text='Apellido restaurador', max_length=200, verbose_name='Apellido')),
                ('nombre', models.CharField(help_text='Nombre restaurador', max_length=200, verbose_name='Nombre')),
                ('domicilio', models.CharField(help_text='Domicilio del restaurador', max_length=200, verbose_name='Domicilio')),
                ('email', models.EmailField(help_text='Nombre restaurador', max_length=200, verbose_name='E-mail')),
                ('telefono', models.PositiveBigIntegerField(help_text='Teléfono de restaurador', verbose_name='Teléfono')),
                ('especialidad', models.ForeignKey(help_text='Especialidad derestaurador', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_restaurador_related', to='app.especialidad', verbose_name='Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Restauracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Descripción de la obra', verbose_name='descripción')),
                ('fecha_reingreso', models.DateField(help_text='fecha de primer ingreso de la obra', verbose_name='fecha de reingreso ingreso')),
                ('fecha_salida', models.DateField(help_text='fecha de salida de la obra', verbose_name='fecha de salida')),
                ('precio', models.FloatField(help_text='precio de la reparación', verbose_name='Precio de la reparación')),
                ('restaurador', models.ForeignKey(help_text='restaurador que realizó la restauración', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_restauracion_related', to='app.restaurador', verbose_name='Restaurador')),
                ('tipo_restauracion', models.ForeignKey(help_text='Tipo de restauración aplicada', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_restauracion_related', to='app.tiporestauracion', verbose_name='Tipo de restauración')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la obra', max_length=200, verbose_name='Nombre de Obra')),
                ('peso', models.IntegerField(help_text='peso en kg', verbose_name='peso')),
                ('valuacion', models.IntegerField(help_text='valuación en pesos', verbose_name='valuación')),
                ('alto', models.IntegerField(help_text='alto de la obra', verbose_name='alto')),
                ('ancho', models.IntegerField(help_text='ancho de la obra', verbose_name='ancho')),
                ('descripcion', models.TextField(help_text='Descripción de la obra', verbose_name='descripción')),
                ('fecha_creacion', models.DateField(help_text='fecha de creación de la obra', verbose_name='fecha de creación')),
                ('fecha_primer_ingreso', models.DateField(help_text='fecha de primer ingreso de la obra', verbose_name='fecha de primer ingreso')),
                ('estilo', models.ForeignKey(help_text='Estilo de reparación', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_obra_related', to='app.estilo', verbose_name='Estilo')),
                ('restauración', models.ForeignKey(blank=True, help_text='Restauraciones de obra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_obra_related', to='app.restauracion', verbose_name='Restauración')),
                ('tecnica', models.ForeignKey(help_text='Tecnica empleada para la reparación', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_obra_related', to='app.tecnica', verbose_name='Tecnica')),
            ],
        ),
        migrations.AddField(
            model_name='especialidad',
            name='estilo',
            field=models.ForeignKey(help_text='Estilo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Estilo', to='app.estilo', verbose_name='Estilo'),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='tecnica',
            field=models.ForeignKey(help_text='Técnica', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnica', to='app.tecnica', verbose_name='Tecnica'),
        ),
    ]
