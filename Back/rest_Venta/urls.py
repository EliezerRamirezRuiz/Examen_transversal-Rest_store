from django.urls import path
from .views import estadoVentaGetAll, estadoVentaByid, ventaGetAll, ventaByid, detalleVentaGetAll, detalleVentaByid

urlpatterns = [
    path('estadoVenta/', estadoVentaGetAll, name='estadoVentaGetAll'),
    path('estadoVenta/<idEstadoVenta>', estadoVentaByid, name='estadoVentaByid'),
    path('ventas/', ventaGetAll, name='ventaGetAll'),
    path('ventas/<idVenta>', ventaByid, name='ventaByid'),
    path('detalleVentas/', detalleVentaGetAll, name='detalleVentaGetAll'),
    path('detalleVentas/<idDetalleVenta>', detalleVentaByid, name='detalleVentaByid'),
]