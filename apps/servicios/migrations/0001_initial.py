# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroEmergencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=30, verbose_name='Teléfono')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Latitud')),
                ('log', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Longitud')),
                ('sector', models.CharField(choices=[('PUBLICO', 'PUBLICO'), ('PRIVADO', 'PRIVADO')], max_length=10, verbose_name='Sector')),
                ('nivel', models.CharField(choices=[('0', 'NINGUNO'), ('1', 'PRIMERO'), ('2', 'SEGUNDO'), ('3', 'TERCERO')], max_length=10, verbose_name='Nivel')),
                ('tipo', models.CharField(choices=[('CS', 'CENTRO SALUD'), ('PO', 'POLICIA'), ('BO', 'BOMBEROS'), ('TR', 'TRANSITO')], max_length=10, verbose_name='Tipo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Centro de emergencia',
                'verbose_name_plural': 'Centros de emergencias',
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo Vehiculo',
                'verbose_name_plural': 'Tipos de Vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Descripción')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('nro_motor', models.CharField(max_length=100, verbose_name='N° Motor')),
                ('nro_chasis', models.CharField(max_length=100, verbose_name='N° Chasis')),
                ('sector', models.CharField(choices=[('PUBLICO', 'PUBLICO'), ('PRIVADO', 'PRIVADO')], max_length=20, verbose_name='Sector')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.TipoVehiculo', verbose_name='Tipo Vehiculo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
        ),
    ]
