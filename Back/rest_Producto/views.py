from doctest import debug_script
from functools import partial
from pydoc import describe
from typing import final
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.parsers import JSONParser

from .models import Producto, Promocion, Categoria, PromocionProducto
from .serializers import (
    ProductoSerializer,
    CategoriaSerializer,
    PromocionProductoSerializer,
    PromocionSerializer,
)

# Create your views here.
"""

    Productos

"""


@api_view(["GET", "POST"])
def productGetAll(request: HttpRequest):
    if request.method == "GET":
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        if type(data) == dict:
            producto = ProductoSerializer(data=data)
            if producto.is_valid():
                producto.save()
                return Response(producto.data, status=status.HTTP_201_CREATED)
        else:
            for objProducto in data:
                producto = ProductoSerializer(data=objProducto)
                if producto.is_valid():
                    producto.save()
            return Response(producto.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def productById(request: HttpRequest, id: int):
    try:
        producto: Producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        producto.delete()
        return Response(status=status.HTTP_200_OK)


"""
    Categorias
"""


@api_view(["GET", "POST"])
def categoriaGetAll(request: HttpRequest):
    if request.method == "GET":
        categorias: Categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        if type(data) == dict:
            categorias = CategoriaSerializer(data=data)
            if categorias.is_valid():
                categorias.save()
                return Response(categorias.data, status=status.HTTP_201_CREATED)
        else:
            for objCategorias in data:
                categorias = CategoriaSerializer(data=objCategorias)
                if categorias.is_valid():
                    categorias.save()
            return Response(categorias.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def categoriaById(request: HttpRequest, id: int):
    try:
        categoria: Categoria = Categoria.objects.get(idCategoria=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        categoria.delete()
        return Response(status=status.HTTP_200_OK)


"""

    Promocion

"""


@api_view(["GET", "POST"])
def promocionGetAll(request: HttpRequest):
    if request.method == "GET":
        promocion: Promocion = Promocion.objects.all()
        serializerPromocion = PromocionSerializer(promocion, many=True)
        finalList = []
        for promo in serializerPromocion.data:
            print(promo["idPromocion"])
            promocionProducto: PromocionProducto = PromocionProducto.objects.filter(
                idPromocion_id=promo["idPromocion"]
            )
            serializerPromocionProducto = PromocionProductoSerializer(
                promocionProducto, many=True
            )
            finalObject = {
                "idPromocion": promo["idPromocion"],
                "drescipcion": promo["descripcion"],
                "productos": serializerPromocionProducto.data,
            }
            finalList.append(finalObject)

        return Response(finalList, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        promocion = PromocionSerializer(
            data={"pordesct": data["pordesct"], "descripcion": data["descripcion"]}
        )
        if promocion.is_valid():
            promocion.save()

        data = data["productos"]
        idPromocion = promocion.data["idPromocion"]
        for prod in data:
            finalObject = {
                "idPromocion": idPromocion,
                "idProducto": prod,
            }
            promocionProducto = PromocionProductoSerializer(data=finalObject)
            if promocionProducto.is_valid():
                promocionProducto.save()
        return Response(promocion.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def promocionById(request: HttpRequest, id: int):
    try:
        promocion: Promocion = Promocion.objects.get(idPromocion=id)
    except Promocion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PromocionSerializer(promocion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        pordesct = data["pordesct"]
        idProducto = data["producto"]
        if type(idProducto) == int:
            promocion = PromocionSerializer(promocion, data)
            if promocion.is_valid():
                promocion.save()
                return Response(promocion.data, status=status.HTTP_200_OK)
        else:
            for idp in idProducto:
                finalData = {"pordesct": pordesct, "producto": idp}
                promocion = PromocionSerializer(promocion, finalData)
                if promocion.is_valid():
                    promocion.save()
            return Response(promocion.data, status=status.HTTP_200_OK)
    else:
        promocion.delete()
        return Response(status=status.HTTP_200_OK)
