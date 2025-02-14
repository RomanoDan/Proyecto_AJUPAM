from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jugador
from .forms import AgregarJugador, BuscarJugador

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
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            documento = formulario.cleaned_data.get('documento')
            categoria = formulario.cleaned_data.get('categoria')
            
            jugador = Jugador(nombre = nombre,apellido = apellido,documento = documento,categoria = categoria)
            jugador.save()
            
            return redirect('ranking')
            
    return render(request, 'ranking/agregar_jugador.html', {'formulario': formulario})

