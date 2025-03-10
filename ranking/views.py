from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from .models import Jugador
from .forms import AgregarJugador, BuscarJugador, ModificarJugador
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def ranking(request):
    jugadores = Jugador.objects.all().order_by('-puntos')  # Ordenado por puntos
    formulario = BuscarJugador(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        categoria_a_buscar = formulario.cleaned_data.get('categoria')
        if categoria_a_buscar == '':
            jugadores = Jugador.objects.filter(nombre__icontains=nombre_a_buscar).order_by('-puntos')
        else:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre_a_buscar, categoria=categoria_a_buscar).order_by('-puntos')
    return render(request, 'ranking/ranking.html', {'jugadores': jugadores, 'formulario': formulario})

def inicio(request):
    return render(request, "ranking/inicio.html")

def about(request):
    return render(request, "ranking/about.html")

@login_required
def agregar_jugador(request):
    formulario = AgregarJugador()
    
    if request.method == 'POST':
        formulario = AgregarJugador(request.POST)
        if formulario.is_valid():
            try:
                nombre = formulario.cleaned_data.get('nombre')
                apellido = formulario.cleaned_data.get('apellido')
                documento = formulario.cleaned_data.get('documento')
                categoria = formulario.cleaned_data.get('categoria')
            
                jugador = Jugador(nombre = nombre,apellido = apellido,documento = documento,categoria = categoria)
                jugador.save()
            except IntegrityError:
                formulario.add_error('documento', "El documento ya existe en la base de jugadores, intente con otro, por favor.")
                return render(request, 'ranking/agregar_jugador.html', {'formulario': formulario})
            
            return redirect('ranking')
            
    return render(request, 'ranking/agregar_jugador.html', {'formulario': formulario})


def ver_jugador(request,jugador_id):
    jugador = Jugador.objects.get(id=jugador_id)
    return render(request, 'ranking/ver_jugador.html', {'jugador': jugador})

# CBV

class ModificarJugadorView(LoginRequiredMixin, UpdateView):
    model = Jugador
    template_name = "ranking/CBV/modificar_jugador.html"
    form_class = ModificarJugador
    success_url = reverse_lazy("ranking")

class EliminarJugadorView(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = "ranking/CBV/eliminar_jugador.html"
    success_url = reverse_lazy("ranking")


# Vistas comunes

    # def modificar_jugador(request,jugador_id):
    #     jugador = Jugador.objects.get(id=jugador_id)    
    #     if request.method == "POST":
    #         formulario = ModificarJugador(request.POST, instance=jugador)
    #         if formulario.is_valid():
    #             formulario.save()
    #             return redirect('ranking')
    #     else:
    #         formulario = ModificarJugador(instance=jugador)  
    #     return render(request,'ranking/modificar_jugador.html', {'formulario': formulario}) 
    # def eliminar_jugador(request,jugador_id):
    #     jugador = Jugador.objects.get(id=jugador_id)
    #     jugador.delete()
    #     return redirect('ranking')