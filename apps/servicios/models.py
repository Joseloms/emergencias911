#encoding:utf-8
from django.db import models

SECTOR = (
    ('PUBLICO', 'PUBLICO'),
    ('PRIVADO', 'PRIVADO'),
)

NIVEL = (
    ('NINGUNO', 'NINGUNO'),
    ('PRIMERO', 'PRIMERO'),
    ('SEGUNDO', 'SEGUNDO'),
    ('TERCERO', 'TERCERO'),
)

TIPO = (
    ('SALUD', 'SALUD'),
    ('SEGURIDAD', 'SEGURIDAD'),
    ('BOMBEROS', 'BOMBEROS'),
    ('TRANSITO', 'TRANSITO'),
)


class TipoVehiculo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Descripción', unique=True)
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    class Meta:
        verbose_name = 'Tipo Vehiculo'
        verbose_name_plural = 'Tipos de Vehiculos'

    def __str__(self):
        return '{}'.format(self.name)


class DispositivoGPS(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    imei = models.IntegerField(unique=True, verbose_name='Número de IMEI')
    nro_sim = models.IntegerField(unique=True, verbose_name='Número de SIM')
    lat = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    lng = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    time = models.DateTimeField(verbose_name='Tiempo', null=True)
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, verbose_name='Descripción')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    nro_motor = models.CharField(max_length=100, verbose_name='N° Motor')
    nro_chasis = models.CharField(max_length=100, verbose_name='N° Chasis')
    sector = models.CharField(max_length=20, choices=SECTOR, verbose_name='Sector')
    tipo_id = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, verbose_name='Tipo Vehiculo', null=False)
    gps_id = models.OneToOneField(DispositivoGPS, on_delete=models.CASCADE, verbose_name='GPS', null=True)
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return '{}'.format(self.name)


class CentroEmergencia(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=150, verbose_name='Dirección')
    telefono = models.CharField(max_length=30, verbose_name='Teléfono')
    lat = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    lng = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    sector = models.CharField(max_length=10, choices=SECTOR, verbose_name='Sector')
    nivel = models.CharField(max_length=10, choices=NIVEL, verbose_name='Nivel')
    tipo = models.CharField(max_length=20, choices=TIPO, verbose_name='Tipo')
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    class Meta:
        verbose_name = 'Centro de emergencia'
        verbose_name_plural = 'Centros de emergencias'

    def __str__(self):
        return '{}'.format(self.name)
