from functools import total_ordering
from pydoc import cli
from tabnanny import verbose
from django.db import models
from rest_Auth.models import Usuario
from rest_Producto.models import Producto


class EstadoVenta(models.Model):
    idEstadoVenta = models.AutoField(primary_key=True, verbose_name="id estado")
    nombreEstadoVenta = models.CharField(max_length=255, null=False, verbose_name="nombre estado venta")

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name="id de venta")
    fechaVenta = models.DateField(auto_now_add=True, null=True, verbose_name="fecha de venta")
    totalVenta = models.IntegerField(null=False, verbose_name="total de venta")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    estadoVenta = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE, verbose_name="EstadoVenta")

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(primary_key=True, verbose_name="id Detalle Venta")
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="producto")

