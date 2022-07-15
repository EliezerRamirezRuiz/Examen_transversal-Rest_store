from django.urls import path
from rest_Auth.views import singUp, login, changePassword, validateUser
from .views import usuariosGetAll, usuarioById, updateSuscripcion

urlpatterns = [
    path("signUp", singUp, name="singUp"),
    path("login", login, name="login"),
    path("changePassword", changePassword, name="changePassword"),
    path("validateUser", validateUser, name="validateUser"),
    path("usuarios/", usuariosGetAll, name="usuariosGetAll"),
    path("usuarios/suscribe", updateSuscripcion, name="updateSuscripcion"),
    path("usuarios/byId/<idUsuario>", usuarioById, name="usuarioById"),
]
