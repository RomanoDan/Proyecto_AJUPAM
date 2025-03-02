from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.http import HttpResponse
from .models import Jugador
from .forms import AgregarJugador, BuscarJugador
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from datetime import date

def ranking(request):
    jugadores = Jugador.objects.all().order_by('-puntos')  # Ordenado por puntos
    formulario = BuscarJugador(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        categoria_a_buscar = formulario.cleaned_data.get('categoria')
        if categoria_a_buscar == '':
            jugadores = Jugador.objects.all().order_by('-puntos')
        else:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre_a_buscar).order_by('-puntos')
            jugadores = Jugador.objects.filter(categoria=categoria_a_buscar).order_by('-puntos')
    return render(request, 'ranking/ranking.html', {'jugadores': jugadores, 'formulario': formulario})

def inicio(request):
    return render(request, "ranking/inicio.html")

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
                # Agregar para que se ponga por defecto la fecha de creación.
                # Agregar para que puedan cargar foto
            
                jugador = Jugador(nombre = nombre,apellido = apellido,documento = documento,categoria = categoria)
                jugador.save()
            except IntegrityError:
                formulario.add_error('documento', "El documento ya existe en la base de jugadores, intente con otro, por favor.")
                return render(request, 'ranking/agregar_jugador.html', {'formulario': formulario})
            
            return redirect('ranking')
            
    return render(request, 'ranking/agregar_jugador.html', {'formulario': formulario})

def eliminar_jugador(request,jugador_id):
    ...
    return redirect('listado_jugadores')

def ver_jugador(request,jugador_id):
    jugador = Jugador.objects.get(id=jugador_id)
    return render(request, 'inicio/ver_jugador_html', {'jugador': jugador})

class ModificarJugador(UpdateView):
    model = Jugador
    template_name = "modificar_jugador.html"
    fields ="__all__"
    success_url = reverse_lazy("ranking")