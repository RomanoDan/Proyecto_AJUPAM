from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.forms import FormCreacionUsuario, FormEdicionUsuario, FormCambioContraseña
from usuarios.models import InfoExtra


def login (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login(request, usuario)
            InfoExtra.objects.get_or_create(user=usuario)

            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = FormCreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormCreacionUsuario()
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def ver_perfil(request,user_id):
    perfil = get_object_or_404(User, id= user_id)
    return render(request, 'usuarios/ver_perfil.html', {'perfil': perfil})

def editar_perfil(request,user_id):

    info_extra = request.user.infoextra

    perfil = get_object_or_404(User, id= user_id)
    if request.method == 'POST':
        formulario = FormEdicionUsuario(request.POST, request.FILES, instance=perfil)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            if formulario.cleaned_data.get('sobre_ti'):
                info_extra.sobre_ti = formulario.cleaned_data.get('sobre_ti')
            
            info_extra.save()
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormEdicionUsuario(instance=perfil)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarContraseña(PasswordChangeView):
    form_class = FormCambioContraseña
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('inicio')