from django.urls import path
from ranking.views import ranking, inicio,agregar_jugador, eliminar_jugador, ver_jugador,ModificarJugador

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ranking', ranking, name="ranking"),
    path('agregar-jugador', agregar_jugador, name="agregar_jugador"),

    path('modificar-jugador/<int:jugador_id>', ver_jugador, name="modificar_jugador"),
]