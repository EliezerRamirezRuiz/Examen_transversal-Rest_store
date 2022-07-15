from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from .models import Usuario
from .serializers import UserSerializer, UsuarioSerializer


"""
    Registro de usuario y creación de token
"""

# Create your views here.
@api_view(["POST"])
def singUp(request):
    data = JSONParser().parse(request)
    usuario = UsuarioSerializer(
        data={
            "nombre": data["nombre"],
            "apellidos": data["apellidos"],
            "correo": data["correo"],
            "direccion": data["direccion"],
            "telefono": data["telefono"],
            "comuna": data["comuna"],
            "provincia": data["provincia"],
            "region": data["region"],
            "rut": data["rut"],
            "isSuscrito": data["isSuscrito"],
        }
    )
    if usuario.is_valid():
        data["password"] = make_password(data["password"])
        serializer = UserSerializer(
            data={
                "first_name": data["nombre"],
                "last_name": data["apellidos"],
                "email": data["correo"],
                "password": data["password"],
                "username": data["correo"],
            }
        )
        if serializer.is_valid():
            usuario.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    Inicio de sesión
"""


@api_view(["POST"])
def login(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(username=data["username"])
    except User.DoesNotExist:
        return Response(
            "Usuario no se encuentra en los registros", status=status.HTTP_404_NOT_FOUND
        )
    pass_valido = check_password(data["password"], user.password)
    serialize = UserSerializer(user)
    usuario = Usuario.objects.get(correo=serialize.data["email"])
    serializer = UsuarioSerializer(usuario)
    if not pass_valido:
        return Response("Contraseña incorrecta, intente nuevamente.")
    token, create = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "id": serializer.data["idUsuario"]})


"""
    Cambio de contraseña
"""


@api_view(["PUT"])
def changePassword(request):
    try:
        data = JSONParser().parse(request)
        data["password"] = make_password(data["password"])
        user = User.objects.get(username=data["username"])
    except User.DoesNotExist:
        return Response(
            "Usuario no se encuentra en los registros", status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)


"""
    Usuario
"""


@csrf_exempt
@api_view(["GET"])
def usuariosGetAll(request):
    if request.method == "GET":
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(usuario.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def usuarioById(request, idUsuario):
    """
    Get, update o delete de un Usuario en especifico.
    Recibe el parametro <idUsuario>
    """
    try:
        usuario = Usuario.objects.get(idUsuario=idUsuario)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def validateUser(request):
    data = JSONParser().parse(request)
    try:
        usuario = Usuario.objects.get(correo=data["email"])
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(
    [
        "PUT",
    ]
)
def updateSuscripcion(request):
    data = JSONParser().parse(request)
    try:
        usuario = Usuario.objects.get(correo=data["email"])
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UsuarioSerializer(usuario, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
