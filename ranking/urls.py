from django.urls import path
from ranking.views import ranking, inicio,agregar_jugador

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ranking', ranking, name="ranking"),
    path('agregar-jugador', agregar_jugador, name="agregar_jugador"),
]