from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="ID de Usuario")
    nombre = models.CharField(
        max_length=255, null=False, verbose_name="Nombre de Usuario"
    )
    apellidos = models.CharField(
        max_length=255, null=False, verbose_name="Apellidos de Usuario"
    )
    correo = models.CharField(
        max_length=255, null=False, verbose_name="Correo de Usuario"
    )
    direccion = models.CharField(
        max_length=255, null=False, verbose_name="Direccion de Usuario"
    )
    telefono = models.CharField(
        max_length=255, null=False, verbose_name="Telefono de Usuario"
    )
    comuna = models.CharField(
        max_length=255, null=False, verbose_name="Comuna de Usuario"
    )
    provincia = models.CharField(
        max_length=255, null=True, verbose_name="Provincia de Usuario"
    )
    region = models.CharField(
        max_length=255, null=False, verbose_name="Region de Usuario"
    )
    rut = models.CharField(max_length=255, null=False, verbose_name="Rut de Usuario")
    isSuscrito = models.BooleanField(default=False, verbose_name="Isuscrito de Usuario")
    fechaSuscrito = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Fecha Suscrito de Usuario"
    )
    isAdmin = models.BooleanField(default=False, verbose_name="Isadmin de Usuario")