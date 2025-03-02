from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormCreacionUsuario

def login (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login(request, usuario)

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

