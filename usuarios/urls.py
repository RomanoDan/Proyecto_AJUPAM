from django.urls import path
from usuarios.views import login, registro, editar_perfil, ver_perfil, CambiarContraseña
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name= 'usuarios/logout.html'), name = 'logout'),
    path('registro/', registro, name = 'registro'),
    path('editar-perfil/<int:user_id>/', editar_perfil, name = 'editar_perfil'),
    path('editar-perfil/cambiar-pass/', CambiarContraseña.as_view(), name = 'cambiar_pass'),
    path('ver-perfil/<int:user_id>/', ver_perfil, name = 'ver_perfil'),
]
