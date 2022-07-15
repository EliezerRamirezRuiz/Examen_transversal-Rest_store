from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password','username')
        

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "idUsuario",
            "nombre",
            "apellidos",
            "correo",
            "direccion",
            "telefono",
            "comuna",
            "provincia",
            "region",
            "rut",
            "isSuscrito",
            "fechaSuscrito"
        ]        