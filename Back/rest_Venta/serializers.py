from dataclasses import fields
from rest_framework import serializers
from .models import EstadoVenta, Venta, DetalleVenta


class EstadoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoVenta
        fields = [
            "idEstadoVenta",
            "nombreEstadoVenta"
        ]

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = [
            "idVenta", 
            "fechaVenta",
            "totalVenta",
            "usuario",
            "estadoVenta"
        ]
        
class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = [
            "idDetalleVenta",
            "venta",
            "producto"
        ]