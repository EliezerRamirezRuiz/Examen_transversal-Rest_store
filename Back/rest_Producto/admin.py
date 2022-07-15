from django.contrib import admin
from .models import Categoria,Producto,Promocion,PromocionProducto
admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(PromocionProducto)  
admin.site.register(Categoria)

# Register your models here.
