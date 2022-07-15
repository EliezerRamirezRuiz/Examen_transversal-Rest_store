from django.urls import path
from .views import (
    productById,
    productGetAll,
    categoriaGetAll,
    categoriaById,
    promocionGetAll,
    promocionById,
)

urlpatterns = [
    path("productos/", productGetAll, name="productGetAll"),
    path("productos/<id>", productById, name="productById"),
    path("categoria/", categoriaGetAll, name="categoriaGetAll"),
    path("categoria/<id>", categoriaById, name="categoriaById"),
    path("promociones/", promocionGetAll, name="promocionesGetAll"),
    path("promociones/<id>", promocionById, name="promocionesGetById"),
]
