from django.contrib import admin
from .models import EstadoVenta, Venta, DetalleVenta
# Register your models here.
admin.site.register(EstadoVenta)
admin.site.register(Venta)
admin.site.register(DetalleVenta)