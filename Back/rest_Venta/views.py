import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import EstadoVenta, Venta, DetalleVenta
from .serializers import EstadoVentaSerializer, VentaSerializer, DetalleVentaSerializer

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Estado Venta

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def estadoVentaGetAll(request):

    if request.method == 'GET':
        estadoVenta = EstadoVenta.objects.all()
        serializer = EstadoVentaSerializer(estadoVenta, many=True)
        return Response(serializer.data)
    else:
        data = JSONParser().parse(request)
        if type(data) == dict:
            estadoVenta = EstadoVentaSerializer(data=data)
            if estadoVenta.is_valid():
                estadoVenta.save()
                return Response(estadoVenta.data, status=status.HTTP_201_CREATED)
        else:
            for objEstadoVenta in data:
                estadoVenta = EstadoVentaSerializer(data=objEstadoVenta)
                if estadoVenta.is_valid():
                    estadoVenta.save()
            return Response(estadoVenta.data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def estadoVentaByid(request,idEstadoVenta):
    
    try:
        estadoVenta = EstadoVenta.objects.get(idEstadoVenta=idEstadoVenta)
    except EstadoVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstadoVentaSerializer(estadoVenta)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EstadoVentaSerializer(estadoVenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        estadoVenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Venta

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def ventaGetAll(request):

    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def ventaByid(request,idVenta):
    
    try:
        venta = Venta.objects.get(idVenta=idVenta)
    except EstadoVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Detalle Venta

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def detalleVentaGetAll(request):

    if request.method == 'GET':
        detalleVenta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalleVenta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalleVentaByid(request,idDetalleVenta):
    
    try:
        detalleVenta = DetalleVenta.objects.get(idDetalleVenta=idDetalleVenta)
    except DetalleVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DetalleVentaSerializer(detalleVenta)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(detalleVenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        detalleVenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        