from pydoc import describe
from django.db import models


# Create your models here.
class Categoria(models.Model):
    idCategoria = models.AutoField(
        primary_key=True, null=False, verbose_name="id categoria"
    )
    nombreCategoria = models.CharField(
        max_length=255, null=False, verbose_name="nombre categoria"
    )


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="id de producto")
    nombre = models.CharField(
        max_length=255, null=False, verbose_name="Nombre de producto"
    )
    valor = models.IntegerField(null=False, verbose_name="Valor de producto")
    descripcion = models.CharField(
        max_length=1500, null=False, verbose_name="Descripcion de producto"
    )
    stock = models.IntegerField(null=False, default=0, verbose_name="Stock de producto")
    imagen = models.ImageField(null=False, verbose_name="Imagen de producto")
    categoria = models.ForeignKey(
        Categoria,
        null=False,
        verbose_name="Categoria de producto",
        on_delete=models.CASCADE,
    )


class Promocion(models.Model):
    idPromocion = models.AutoField(primary_key=True, verbose_name="id promocion")
    pordesct = models.IntegerField(null=False, verbose_name="porcentaje de descuento")
    descripcion = models.CharField(
        max_length=512, null=True, verbose_name="descripcion de promoción"
    )


class PromocionProducto(models.Model):
    idPromocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
